## How to build static website using Nginx Docker Container

## Steps

1. Build Docker Image using dockerfile
```bash
docker build -t ctlwebnginx .
```
2. Start the Docker Container
```bash
docker run -d -name=static-web-nginx -p 7777:80 ctlwebnginx
```
3. Validate Application
```bash
http://localhost:8888/
```
