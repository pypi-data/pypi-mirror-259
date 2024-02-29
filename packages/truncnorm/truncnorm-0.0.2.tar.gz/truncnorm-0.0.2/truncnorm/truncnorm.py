import itertools

import numpy as np
from scipy import stats


def mvdot(A, b):
    return np.einsum("...ik,...k->...i", A, b)


def diag(A):
    return np.einsum("...ii->...i", A)


def integral(mu, Sigma, a, b):
    """P(a<=x<=b) for x~N(mu,Sigma) """

    N = np.shape(mu)[-1]

    # If we don't have an upper bound, flip everything and use the lower bound
    # as the upper bound.
    if b is None:
        # Swap the axes
        b = None if a is None else -a
        a = None
        mu = -mu

    if a is None:
        if b is None:
            # Trivial integral
            return 1

        if N == 1:
            return stats.norm.cdf(b, mu, Sigma[...,0])[...,0]

        # If only upper bound, we can compute P(x<=b) with a single evaluation
        # of CDF
        #
        # TODO: SciPy multivariate normal has no support for arrays, so we need
        # to loop over each ourselves
        sh = np.broadcast_shapes(
            np.shape(b)[:-1],
            np.shape(mu)[:-1],
            np.shape(Sigma)[:-2],
        )
        N = np.shape(mu)[-1]
        b = np.broadcast_to(b, sh + (N,))
        mu = np.broadcast_to(mu, sh + (N,))
        Sigma = np.broadcast_to(Sigma, sh + (N,N))
        p = np.zeros(sh)

        for ind in itertools.product(*(np.arange(s) for s in sh)):
            p[ind] = stats.multivariate_normal.cdf(
                b[ind],
                mean=mu[ind],
                cov=Sigma[ind],
            )

        return p

    if N == 1:
        s = np.sqrt(Sigma)[...,0]
        p = stats.norm.cdf(b, mu, s) - stats.norm.cdf(a, mu, s)
        return p[...,0]

    raise NotImplementedError()

    # TODO: Broadcasting

    y = np.stack([a,b])
    [
        ((1, bi,),) if np.isneginf(ai) else ((0, ai), (1, bi))
        for (ai, bi) in zip(a, b)
    ]

    # To get max benefit of the below optimization, flip dimensions for which
    # a[i]>-inf but b[i]=inf
    # flip = ~np.isneginf(a) & np.isposinf(b)
    # b = np.where(flip, -a, b)
    # a = np.where(flip, -np.inf, a)
    # mu = np.where(flip, -mu, mu)

    # Optimization: skip combinations with any a[i]=-inf
    [
        ((1, bi,),) if np.isneginf(ai) else ((0, ai), (1, bi))
        for (ai, bi) in zip(a, b)
    ]

    P = 0
    for (i, y) in foo:
        # TODO: Maybe discard dimensions with b[i]=inf so it's lower dimensional?
        pass


def _remove_diag(A):
    """Removes diagonal elements from a matrix"""
    # See: https://stackoverflow.com/a/46736275
    return A[~np.eye(A.shape[0],dtype=bool)].reshape(A.shape[0],-1)


def _remove_each_row_and_column(x):
    n = np.shape(x)[-1]
    inds = _remove_diag(
        np.repeat(np.arange(n)[None,:], n, axis=0)
    )
    y = x[...,inds,:]
    return np.take_along_axis(
        y,
        np.broadcast_to(
            inds[...,None,:],
            np.shape(y)[:-1] + (n-1,),
        ),
        axis=-1,
    )


def _remove_each_column(x):
    n = np.shape(x)[-1]
    inds = _remove_diag(
        np.repeat(np.arange(n)[None,:], n, axis=0)
    )
    return x[...,inds]


def _remove_each_row(x):
    n = np.shape(x)[-1]
    inds = _remove_diag(
        np.repeat(np.arange(n)[None,:], n, axis=0)
    )
    return x[...,inds,:]


def _geometric_sum(x, a, b):
    """sum_a^{b-1} x**i"""
    z = 1 - x
    return np.where(
        a >= b,
        0,
        np.where(
            z == 0,
            b - a, # case x==1
            (x**a - x**b) / z,
        )
    )


def _get_g(G, k, N, m):

    # We are interested in G[i][...]
    i = np.sum(k, axis=-1)

    # How many (N-1) length axes there are in total for all G[j] for j<i
    d = np.rint(_geometric_sum(N-1, 0, i)).astype(int)

    v = np.cumsum(np.insert(k, 0, 0, axis=-1), axis=-1)
    r = np.rint(_geometric_sum(N-1, v[...,:-1], v[...,1:])).astype(int)

    inds = (
        # Choose the correct G[i] (each has shape (N-1)^i)
        d +
        # Choose the correct element from each N-1 length axis
        np.sum(np.arange(N-1) * r, axis=-1)
    )

    return G[...,np.arange(N),inds]


def _get_f(F, k, N, ndim):
    sh0 = np.shape(F)
    sh = (
        sh0 if ndim == 0 else
        sh0[:-ndim]
    )
    # Reshape into a vector
    mask = np.any(k < 0, axis=-1, keepdims=True)
    f = np.reshape(F, sh + (-1,))

    v = np.cumsum(
        np.insert(
            np.where(
                mask,
                0,
                k,
            ),
            0,
            0,
            axis=-1,
        ),
        axis=-1,
    )
    # Force convert to integers what they should be anyway
    r = np.rint(_geometric_sum(N, v[...,:-1], v[...,1:])).astype(int)

    inds = np.sum(np.arange(N) * r, axis=-1)
    return np.where(
        mask[...,0],
        0,
        np.reshape(f[...,inds], sh + np.shape(k)[:-1]),
    )


def _recurrent_integrals(mu, Sigma, a, b, m):

    N = np.shape(mu)[-1]

    # Base case for 1D, that is, scalars
    if N == 1:
        Fs = []
        L = integral(mu, Sigma, a, b)
        Fs.append(L)
        s2 = Sigma[...,0]
        s = np.sqrt(s2)
        for k in range(0, m):
            c1 = 0 if k < 1 else k*s2*Fs[k-1][...,None,None]
            c2 = 0 if a is None else a**k * stats.norm.pdf((a-mu)/s)
            c3 = 0 if b is None else b**k * stats.norm.pdf((b-mu)/s)
            F = (mu * Fs[k][...,None] + c1 + s * (c2 - c3))
            Fs.append(F)
        return Fs

    s2 = diag(Sigma)

    # Compute the lower dimensional integrals
    if m > 0:

        def compute_lower_dimensional_integrals(y):
            Sigmaj = _remove_each_row(Sigma)
            Sigmajj = _remove_each_row_and_column(Sigma)
            muj = _remove_each_column(mu)
            # Shapes:
            #
            # Gs[0] :: (...) + ()
            # Gs[1] :: (...) + (N-1)
            # Gs[2] :: (...) + (N-1,N-1)
            # Gs[3] :: (...) + (N-1,N-1,N-1)
            Gs = _recurrent_integrals(
                muj + np.einsum("...jij,...j->...ji", Sigmaj, (y - mu) / s2),
                Sigmajj - np.einsum("...jaj,...jbj->...jab", Sigmaj, Sigmaj) / s2[...,None,None],
                None if a is None else _remove_each_column(a),
                None if b is None else _remove_each_column(b),
                m - 1,
            )
            # Put all in one huge vector for more efficient accessing
            sh = np.shape(Gs[0])
            return np.concatenate(
                [np.reshape(Gi, sh + (-1,)) for Gi in Gs],
                axis=-1,
            )

        Ga = (
            None if a is None else
            compute_lower_dimensional_integrals(a)
        )
        Gb = (
            None if b is None else
            compute_lower_dimensional_integrals(b)
        )

    # Compute the different total power integrals
    #
    # Shapes:
    #
    # Fs[0] :: (...) + ()
    # Fs[1] :: (...) + (N,)
    # Fs[2] :: (...) + (N,N)
    # Fs[3] :: (...) + (N,N,N)
    # and so on
    Fs = []
    Fs.append(np.asarray(integral(mu, Sigma, a, b)))
    al = a
    bl = b
    mul = mu
    Sigmal = Sigma
    stdl = np.sqrt(s2)
    k = np.zeros(N, dtype=int)
    I = np.eye(N, dtype=int)
    Il = I
    for l in range(1, m+1):
        c1 = (
            np.zeros(N) if l < 2 else
            k * _get_f(Fs[l-2], k[...,None,:] - I, N, ndim=l-2)
        )
        c2 = (
            0 if al is None else
            np.where(
                np.isneginf(al),
                0,
                al**k * stats.norm.pdf(al, mul, stdl) * _get_g(
                    Ga,
                    _remove_each_column(k),
                    N,
                    m-1,
                ),
            )
        )
        c3 = (
            0 if bl is None else
            np.where(
                np.isposinf(bl),
                0,
                bl**k * stats.norm.pdf(bl, mul, stdl) * _get_g(
                    Gb,
                    _remove_each_column(k),
                    N,
                    m-1,
                ),
            )
        )
        c = c1 + c2 - c3
        F = mul * Fs[l-1][...,None] + mvdot(Sigmal, c)
        Fs.append(F)

        # Add new axes for the next iteration round
        al = (None if al is None else al[...,None,:])
        bl = (None if bl is None else bl[...,None,:])
        mul = mul[...,None,:]
        stdl = stdl[...,None,:]
        Sigmal = Sigmal[...,None,:,:]
        k = k + Il
        Il = Il[...,None,:]

    return Fs


def moments(mu, Sigma, a, b, m):

    # Broadcast and convert to arrays
    # sh = np.broadcast_shapes(
    #     np.shape(mu)[:-1],
    #     np.shape(Sigma)[:-2],
    #     () if a is None else np.shape(a)[:-1],
    #     () if b is None else np.shape(b)[:-1],
    # )
    # N = np.shape(mu)[-1]
    # mu = np.broadcast_to(mu, sh + (N,))
    # Sigma = np.broadcast_to(Sigma, sh + (N,N))
    # a = None if a is None else np.broadcast_to(a, sh + (N,))
    # b = None if b is None else np.broadcast_to(b, sh + (N,))

    Fs = _recurrent_integrals(
        np.asarray(mu),
        np.asarray(Sigma),
        None if a is None else np.asarray(a),
        None if b is None else np.asarray(b),
        m,
    )
    L = Fs[0]
    # Treat the first element a bit differently by not dividing as it would give
    # trivial 1. But divide the other elements so you'll get the expectations.
    return [L] + [Fi / L for Fi in Fs[1:]]
