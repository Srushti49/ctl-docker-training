# Docker Networking Tutorial

This tutorial provides step-by-step instructions for working with Docker networking concepts, covering the creation of a custom network, launching containers within the network, integrating Grafana with Prometheus, and managing network connections.

## Steps

### 1. Create a Network

```bash
docker network create custom-network --driver bridge
docker network ls
```

### 2. Launch Prometheus Container

Use the `--network` argument to attach the container to the custom network.

```bash
docker run --name prometheus-console -d -p 9090:9090 --network custom-network bitnami/prometheus:latest
```

### 3. Run Grafana Containers

Launch other containers within the same network using the `--network` flag.

```bash
docker run -d --name=grafana -p 3000:3000 --network custom-network grafana/grafana
```

### 4. Fetch IP Address of Grafana and Prometheus

```bash
docker inspect <container_id> | grep IPAddress
```

Example:
- Prometheus: 172.19.0.2
- Grafana: 172.19.0.3

### 5. Integrate Grafana with Prometheus

Configure Grafana to use Prometheus as a data source.

### 6. Validation

Ensure that the data source is working as expected.

### 7. Access Container using Name instead of IP Address

Use the container names as hostnames within the network.

### 8. Add Existing Container to Custom Network

Connect an existing container to the user-defined bridge network without restarting it.

```bash
docker network connect custom-network <container_name>
```

Example:

```bash
docker run -d -p 80:80 --name=webapp1 nginx
docker network connect custom-network webapp1
```

### 9. Disconnect/Connect Prometheus from Custom Network

```bash
docker network disconnect custom-network prometheus-console
docker network connect custom-network prometheus-console
```

### 10. Run Node Exporter

Launch Node Exporter within the custom network.

```bash
docker run -d --name node-exporter-node1 -p 9100:9100 --network custom-network bitnami/node-exporter:latest
```

Feel free to explore and experiment with different Docker networking scenarios using the provided steps.
