import os
from setuptools import setup, find_packages


if __name__ == "__main__":

    def read(fname):
        return open(os.path.join(os.path.dirname(__file__), fname)).read()

    meta = {}
    base_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(base_dir, 'truncnorm', '_meta.py')) as fp:
        exec(fp.read(), meta)

    setup(
        name="truncnorm",
        author=meta["__author__"],
        author_email=meta["__contact__"],
        description="Moments for doubly truncated multivariate normal distributions",
        project_urls={
            "Homepage": "https://github.com/jluttine/truncnorm",
            "Download": "https://pypi.org/project/truncnorm/",
            "Bug reports": "https://github.com/jluttine/truncnorm/issues",
            "Contributing": "https://github.com/jluttine/truncnorm/pulls",
        },
        packages=find_packages(),
        use_scm_version=True,
        setup_requires=[
            "setuptools_scm",
        ],
        install_requires=[
            "numpy",
            "scipy",
        ],
        classifiers=[
            "Programming Language :: Python :: 3 :: Only",
            "Development Status :: 3 - Alpha",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: {0}".format(meta["__license__"]),
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3 :: Only",
            "Topic :: Scientific/Engineering",
            "Topic :: Software Development :: Libraries",
        ],
        long_description=read('README.md'),
        long_description_content_type="text/markdown",
    )
