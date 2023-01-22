import docker

client = docker.from_env()

base_url = "gcr.io/kouyazlab-370817/gcexample"

print(client.images.ge)