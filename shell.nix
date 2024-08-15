{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {
    nativeBuildInputs = [
        pkgs.python312
        pkgs.python312Packages.fastapi
    ];
}
