## How to build static website using Apache HTTP Docker Container

## Steps

1. Build Docker Image using dockerfile
```bash
docker build -t ctlwebhttpd .
```
2. Start the Docker Container
```bash
docker run -d --name static-web-httpd -p 8888:80 ctlwebhttpd
```
3. Validate Application
```bash
http://localhost:8888/
```
