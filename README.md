# Setting Up the Flask Application in local:

```bash
python3 -m venv .venv
. .venv/bin/activate

pip install -r requirements.txt

export FLASK_APP=server.py

flask run

Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

# Or Docker:

```bash
docker build -f Dockerfile -t python-flask:latest .

docker image ls python-flask

docker run -p 5001:5000 python-flask

kubectl apply -f deployment.yaml
```

# API Testing :

GET http://localhost:5000/app/healthcheck

# Web Page:

http://localhost:5000/home#

## Running pre-commit checks

pre-commit installs git hooks configured in .pre-commit-config.yaml

Install pre-commit and commitizen to use

```bash
brew install commitizen
brew install pre-commit

pre-commit install
pre-commit install --hook-type commit-msg
pre-commit run --all-files

git add .
git status
pre-commit run --all-files
cz c
git commit -m 'feat: health check api with backend api status response'
git push origin main --force
```
