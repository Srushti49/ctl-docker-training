# Docker Volume Tutorial

This tutorial guides you through creating and managing Docker volumes for an Nginx web server. The tutorial includes steps to set up two Nginx containers, update the index.html file on both hosts, create a new Docker image, push the image to Docker Hub, and set up a new container using the custom image.

## Step 01: Setup 02 Nginx Containers

```bash
docker run -d -p 8081:80 --name web-server-01 nginx
docker run -d -p 8082:80 --name web-server-02 nginx
```

Or using a custom image:

```bash
docker run -d -p 8081:80 --name web-server-01 ctldevopslabs/ctlnginxtest:tagname
```

## Step 02: Update index.html on both hosts

Access the container shell and install the vi package:

```bash
docker exec -it <container_id> bash
apt-get update
apt-get install vim
```

Update the index.html file:

```bash
cd /usr/share/nginx/html/
vi index.html
```

## Step 03: Validation

Validate the changes made to the containers.

## Step 04: Create a New Image

```bash
docker commit <container_id> ctldevopslabs/ctlnginxtest
```

## Step 05: View all Images

```bash
docker image ls
```

## Step 06: Login to Docker Hub Repo

```bash
docker login
```

## Step 07: Push Image to Docker Hub Repo

```bash
docker push ctldevopslabs/ctlnginxtest
```

## Step 08: Stop and Delete Container/Images

```bash
docker stop <container_id>
docker rm <container_id>
docker rmi <image_id>
```

## Step 09: Setup New Container using Custom Image

```bash
docker run -d -p 8081:80 --name web-server-01 nginx
docker run -d -p 8082:80 --name web-server-02 nginx
```

## Step 10: Validation of New Container

Validate the new containers using the web console.
