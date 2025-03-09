from datetime import datetime
import docker
import json

def get_containers_status(container_names: list, host: str):
    client = docker.DockerClient(base_url='unix://var/run/docker.sock')
    for name in container_names:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        try:
            container = client.containers.get(name)  # Busca o container pelo nome
            service_info = {
                "application_name": container.name,
                "application_status": "UP" if container.status == "running" else "DOWN",  # "running", "exited", etc.
                "host_name": host,
                "created_at": timestamp
            }
        except docker.errors.NotFound:
            service_info = {
                "application_name": name,
                "application_status": "not found",
                "host_name": host,
                "created_at": timestamp
            }
        except Exception as e:
            service_info = {
                "application_name": name,
                "application_status": f"error: {str(e)}",
                "host_name": host,
                "created_at": timestamp
            }

        json_output = json.dumps(service_info, indent=4)
        print(json_output)
        with open(f"logs/{name}-status-{timestamp}.json", "w") as f:
            f.write(json_output)


if __name__ == "__main__":
    # Lista de containers que queremos monitorar
    CONTAINERS_TO_MONITOR = ["httpd", "rabbitmq", "postgres"]
    get_containers_status(CONTAINERS_TO_MONITOR, "localhost")
