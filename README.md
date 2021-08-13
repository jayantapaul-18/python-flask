# Setting Up the Flask Application in local:

python3 -m venv python-flask

cd python-flask

activate

pip install -r requirements.txt

export FLASK_APP=server.py

flask run

Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

# Or Docker:

docker build -f Dockerfile -t python-flask:latest .

docker image ls python-flask

docker run -p 5001:5000 python-flask

kubectl apply -f deployment.yaml

# API Testing :

GET http://localhost:5000/app/healthcheck

# Web Page:

http://localhost:5000/home#
