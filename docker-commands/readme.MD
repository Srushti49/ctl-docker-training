
1) docker
This command will output a list with all options available for the docker command 
together with a short description.

Example : docker 

2)docker version
This command will output a current docker version.

Example : docker --version 


Selecting An Image
Now that Docker is up and running we’re ready to select an image so that 
we’re able to run our first docker container. 
To select from the list of already existing Docker images go to docker hub portal.
https://hub.docker.com/

3) docker pull
This command is used to pull images from the docker repository(hub.docker.com)
Example : 
docker pull nginix

Output : 
docker pull httpd 
Using default tag: latest
latest: Pulling from library/httpd
66dbba0fb1b5: Already exists 
010da4e05daa: Pull complete 
c036f6f9865d: Pull complete 
3c1643a8fc21: Pull complete 
07102ce9b5e9: Pull complete 
Digest: sha256:f5556d859f39f6019651b7bdf2dbe9a16b00962e7baa75f873a82f6eb8efc84d
Status: Downloaded newer image for httpd:latest
docker.io/library/httpd:latest


4) docker run
There is a shortcut for building a container from an image and running it with the
docker run command. This will create a new container for an image and run it.

Example : 
docker run -it -p 80:80 web-server

docker run -d -p 80:80 nginx
d75e61fcad1e0c0eca69a3f767be6ba28a66625ce4dc42201a8a323e8313c14e

docker run -d -p 8081:80 --name web-server-01 nginx
docker run -d -p 8082:80 --name web-server-02 nginx


Assigning Container Names
docker run -it -p 80:80 --name mynginx01 nginx


5) docker ps
This command is used to list the running containers
Example: docker ps

Usage: docker ps -a
This command is used to show all the running and exited containers

6) docker exec
Usage: docker exec -it <container id> bash
This command is used to access the running container


docker exec -it 938057a5ea6b bash

Use below commands to install vi package
apt-get update
apt-get install vim

update index.html
cd /usr/share/nginx/html/
vi index.html


7) docker stop/start
Usage: docker stop <container id>
This command stops a running container

8) docker kill
Usage: docker kill <container id>
This command kills the container by stopping its execution immediately. 
The difference between ‘docker kill’ and ‘docker stop’ is that ‘docker stop’ gives the 
container time to 
shutdown gracefully, in situations when it is taking too much time for getting the container 
to stop, one can opt to kill it

9) docker images
This command lists all the locally stored docker images

Usage: docker images


nilesh@Nileshs-MacBook-Air .docker % docker images
REPOSITORY              TAG       IMAGE ID       CREATED         SIZE
ctldevopslabs/testimg   latest    35f72fc6b287   6 minutes ago   135MB
nginx                   latest    114aa6a9f203   5 hours ago     135MB
httpd                   latest    754c83c9c9f5   5 hours ago     139MB
hello-world             latest    46331d942d63   11 months ago   9.14kB


10) View Resource Usages Stats 
The docker stats command returns a live data stream for running containers. 
To limit data to one or more specific containers, specify a list of container names or ids 
separated by a space. 

You can specify a stopped container but stopped containers do not return any data.

docker stats

CONTAINER ID        NAME                                    CPU %               MEM USAGE / LIMIT     MEM %               NET I/O             BLOCK I/O           PIDS
b95a83497c91        awesome_brattain                        0.28%               5.629MiB / 1.952GiB   0.28%               916B / 0B           147kB / 0B          9
67b2525d8ad1        foobar                                  0.00%               1.727MiB / 1.952GiB   0.09%               2.48kB / 0B         4.11MB / 0B         2
e5c383697914        test-1951.1.kay7x1lh1twk9c0oig50sd5tr   0.00%               196KiB / 1.952GiB     0.01%               71.2kB / 0B         770kB / 0B          1
4bda148efbc0        random.1.vnc8on831idyr42slu578u3cr      0.00%               1.672MiB / 1.952GiB   0.08%               110kB / 0B          578kB / 0B          2


11) docker commit
This command creates a new image of an edited container on the local system

Usage: docker commit <conatainer id> <username/imagename>

docker commit 0c9cc58f3268 ctldevopslabs/testimg

nilesh@Nileshs-MacBook-Air .docker % docker commit 0c9cc58f3268 ctldevopslabs/testimg
sha256:35f72fc6b287fcc0c3738af2e96480a5e99a02bb3ac6531e369eef6e7176fffe

12) docker login
This command is used to login to the docker hub repository
Example : docker login

nilesh@Nileshs-MacBook-Air .docker % docker login
Authenticating with existing credentials...
Login Succeeded

Logging in with your password grants your terminal complete access to your account. 
For better security, log in with a limited-privilege personal access token. Learn more at https://docs.docker.com/go/access-tokens/


13) docker push
Usage: docker push <username/image name>
This command is used to push an image to the docker hub repository

Example : 
docker push ctldevopslabs/testimg

Output: 
nilesh@Nileshs-MacBook-Air .docker % docker push ctldevopslabs/testimg
Using default tag: latest
The push refers to repository [docker.io/ctldevopslabs/testimg]
95e404c79fbd: Pushed 
d3383d06d865: Mounted from library/nginx 
b7d3f8882351: Mounted from library/nginx 
ad41e6643fa3: Mounted from library/nginx 
5a87d6397f38: Mounted from library/nginx 
d977b4494cec: Mounted from library/nginx 
ace73ce182d1: Mounted from library/httpd 
latest: digest: sha256:76b6189edf40f31dae539c8dfcf48b7a81b912b20d4202532813142bb01346ca size: 1777


14) docker rm
This command is used to delete a stopped container.
Example: docker rm <container id>
docker rm 6f2e4a4711e1

nilesh@Nileshs-MacBook-Air .docker % docker rm 6f2e4a4711e1
6f2e4a4711e1


15) docker rmi
This command is used to delete an image from local storage.

Example : Usage: docker rmi <image-id>

nilesh@Nileshs-MacBook-Air .docker % docker rmi httpd      
Untagged: httpd:latest
Untagged: httpd@sha256:f5556d859f39f6019651b7bdf2dbe9a16b00962e7baa75f873a82f6eb8efc84d
Deleted: sha256:754c83c9c9f511aa7e6e0355090db25492ae32c6ad8022afaf5d246132944c6b
Deleted: sha256:eb0ec8b14f6cd61093af6827cd2a08185bb68a2508a0412a32c79349e77f8074
Deleted: sha256:0bd5e79c7ba59cabb4bd8b07b48ea56a6d70bc3c5d311cb7de3ef7daed7e1161
Deleted: sha256:dec36a46f08bda208c40a70e079fd0bb544b244b1bea7f19c7837db402bdc6d9
Deleted: sha256:44f0c708673e6dec33ae1f9c833b37617b660c183199042969f9c097cf22ed94


16) docker build
Usage: docker build <path to docker file>
This command is used to build an image from a specified docker file.



