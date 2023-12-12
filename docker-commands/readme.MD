# Docker Commands In-Depth Reference

This in-depth reference guide explains various Docker commands, providing detailed information and examples to help you better understand their usage.

## 1. `docker`

The `docker` command is the entry point for interacting with Docker. Running `docker` without any arguments provides a list of available options and commands.

```bash
docker
```

This command serves as a starting point to explore available Docker commands and options.

## 2. `docker version`

The `docker version` command provides information about the Docker installation, including the client and server versions.

```bash
docker --version
```

This command helps ensure that Docker is installed and provides insights into the installed version.

## 3. Selecting an Image

To run containers, you need to select an image. Docker Hub is a popular repository for Docker images.

### 3.1 `docker pull`

The `docker pull` command downloads images from Docker Hub to your local machine.

```bash
docker pull nginx
```

This example pulls the Nginx image from Docker Hub.

## 4. `docker run`

The `docker run` command creates and runs a container based on a specified image.

### Examples:

```bash
docker run -it -p 80:80 web-server
```

- `-it`: Runs the container interactively.
- `-p 80:80`: Maps port 80 on the host to port 80 on the container.
- `web-server`: Image name.

```bash
docker run -d -p 80:80 nginx
```

- `-d`: Runs the container in the background.

### Naming Containers:

```bash
docker run -it -p 80:80 --name mynginx01 nginx
```

This example assigns a custom name (`mynginx01`) to the container.

## 5. `docker ps`

The `docker ps` command lists running containers.

```bash
docker ps
```

To list all containers (including stopped ones):

```bash
docker ps -a
```

This command helps monitor the status of running containers.

## 6. `docker exec`

The `docker exec` command allows access to a running container.

```bash
docker exec -it <container_id> bash
```

This example enters the container shell interactively.

## 7. Container Management

### `docker stop/start`

Stop a running container:

```bash
docker stop <container_id>
```

### `docker kill`

Kill a container immediately:

```bash
docker kill <container_id>
```

These commands control the lifecycle of containers.

## 8. `docker images`

The `docker images` command lists locally stored Docker images.

```bash
docker images
```

This command provides an overview of available images on the local machine.

## 9. View Resource Usage Stats

```bash
docker stats
```

The `docker stats` command provides live data streams for resource usage in running containers.

## 10. `docker commit`

The `docker commit` command creates a new image from an edited container.

```bash
docker commit <container_id> <username/imagename>
```

This example creates a new image based on changes made to a container.

## 11. `docker login`

The `docker login` command is used to authenticate with the Docker Hub repository.

```bash
docker login
```

This command allows you to push and pull images to and from your Docker Hub account.

## 12. `docker push`

The `docker push` command uploads an image to the Docker Hub repository.

```bash
docker push <username/image_name>
```

This example pushes a locally created image to Docker Hub.

## 13. Container Cleanup

### `docker rm`

The `docker rm` command deletes a stopped container.

```bash
docker rm <container_id>
```

### `docker rmi`

The `docker rmi` command deletes an image from local storage.

```bash
docker rmi <image_id>
```

These commands help clean up containers and images.

## 14. `docker build`

The `docker build` command builds an image from a specified Dockerfile.

```bash
docker build .
```

This command is used to create custom images based on a Dockerfile.

Feel free to explore and experiment with these Docker commands based on your specific use cases and requirements.
