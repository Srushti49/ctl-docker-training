## Docker Networking Concepts

## Steps

1. Create a network

```bash
docker network create custom-network --driver bridge
docker network ls
```
2. Launch the Prometheus container within your network
Use the --network <NETWORK> argument to the docker run command to attach the container to 
the prometheus-network network.

```bash
docker run --name prometheus-console -d -p 9090:9090 --network custom-network bitnami/prometheus:latest

```
3. Run Grafana containers
We can launch other containers using the same flag (--network NETWORK) in the docker run command. If you also set a name to your container, you will be able to use it as hostname in your network.

```bash
docker run -d --name=grafana -p 3000:3000 --network custom-network grafana/grafana
```

4. Fetch IP Address of Grafana and Prometheus 
193e9b8f64ec -- 172.19.0.3  - grafana
3a1a8411fd87 -- 172.19.0.2 - prometheus-console

docker inspect 193e9b8f64ec | grep IPAddress

5.  Integrate Grafana application with Prometheus 

6. Validation (data source working as expected)

7. Access container using name instead of IP Address

8. How to add existing container to custom network 
If you already have a container running, you can to connect it to your new 
user-defined bridge network without having to restart the container. 

For example:
docker network connect custom-network mongodb

docker run -d -p 80:80 --name=webapp1 nginx
docker network connect custom-network webapp1

9. Disconnect/Connect prometheus from custom network 
docker network disconnect custom-network prometheus-console
docker network connect custom-network prometheus-console


10. Run node exporter 
docker run -d --name node-exporter-node1 -p 9100:9100 --network custom-network bitnami/node-exporter:latest