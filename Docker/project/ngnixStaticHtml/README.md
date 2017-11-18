Docker image stored at Docker hub (https://hub.docker.com/)
kalinga/mywebsite

Run steps:
docker pull kalinga/mywebsite:v0.1
docker run -d --name="kalinga.com" -p 8080:80  kalinga/mywebsite:v0.1
chromium-browser http://localhost:8080
firefox http://localhost:8080
