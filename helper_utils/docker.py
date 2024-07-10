import docker

client = docker.DockerClient(base_url='unix:///var/run/docker.sock')

def kill_container_by_name(container_name):
    try:
        container = client.containers.get(container_name)
        container.kill()
        print(f"Container {container_name} killed successfully.")
    except docker.errors.NotFound as e:
        print(f"Container {container_name} not found.")
    except docker.errors.APIError as e:
        print(f"Error occurred: {e}")
