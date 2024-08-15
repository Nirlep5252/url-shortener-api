{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {
    nativeBuildInputs = [
        (pkgs.python312.withPackages (python-pkgs: [
            python-pkgs.fastapi
            python-pkgs.uvicorn
            python-pkgs.sqlalchemy
            python-pkgs.python-dotenv
            python-pkgs.psycopg2
        ]))
    ];
}
