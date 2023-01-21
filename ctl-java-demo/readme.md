## How to Run Docker CTL Java Demo Project

## Steps

1. Build Docker Image using dockerfile
```bash
docker build -t ctlwebapp
```
2. Start the Docker Container
```bash
docker run -p 80:8080 ctlwebapp
```
3. Validate Application
```bash
http://localhost/CrudDemoWithMySql
```
