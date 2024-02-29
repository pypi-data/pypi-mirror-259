let
  pkgs = import <nixpkgs> { };
  ps = pkgs.python3Packages;
in
ps.buildPythonPackage rec {
  name = "truncnorm";
  doCheck = false;
  src = ./.;
  postShellHook = ''
    export PYTHONPATH=$(pwd):$PYTHONPATH
  '';
  depsBuildBuild = with ps; [
    ipython
    pip
    setuptools_scm
    pkgs.git
  ];
  propagatedBuildInputs = with ps; [
    numpy
    scipy
  ];

}
