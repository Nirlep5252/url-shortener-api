# URL Shortener API

## Steps to run (NixOS users)

1. Run `nix-shell`
2. Enable [Docker](https://nixos.wiki/wiki/Docker)
3. Run `./database.sh`
4. Run `uvicorn main:app --reload`

## Steps to run (Non-NixOS users)

### For the database

1. Install [Docker](https://www.docker.com/)
2. Start the PostgreSQL database `./database.sh`

### For the API

1. Install [Python3](https://www.python.org/downloads/)
2. Create a virtual environment (Optional): `python3 -m venv venv`
3. Activate the virtual environment.
4. Install Python packages: `python3 -m pip install -r requirements.txt`
