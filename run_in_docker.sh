docker build --tag flask_rest_api .
docker run -d -p 5000:5000 flask_rest_api