Step 01:
Setup 02 nginx containers 

Step 02:
docker run -d -p 8081:80 --name web-server-01 nginx
docker run -d -p 8082:80 --name web-server-02 nginx


docker run -d -p 8081:80 --name web-server-01 ctldevopslabs/ctlnginxtest:tagname


Step 03: 
Update index.html on both host 

docker exec -it 938057a5ea6b bash
Use below commands to install vi package
apt-get update
apt-get install vim

update index.html
cd /usr/share/nginx/html/
vi index.html

Step 04: Validation 
Validation 


Step 05: Create new image using below command 
Usage: docker commit  <username/imagename>

docker commit 8e100343621f ctldevopslabs/ctlnginxtest


Step 06: View all images present on local 
docker image ls

Step 07 : Login to Docker Hub Repo 
docker login

Step 08: Push image to Docker Hub Repo
docker push ctldevopslabs/ctlnginxtest

Step 09 : Stop and delete containter/images
docker stop 
docker rm 
docker rmi

Step 10 : Setup new container using custom image 
docker run -d -p 8081:80 --name web-server-01 nginx
docker run -d -p 8082:80 --name web-server-02 nginx

Step 11 : Validation of new container web console 