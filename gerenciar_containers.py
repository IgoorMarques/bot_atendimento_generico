import subprocess
import sys
import os

DOCKER_COMPOSE_TEMPLATE = """
version: '3.8'
services:
  rabbitmq_{instance_id}:
    image: "rabbitmq:management"
    ports:
      - "{RABBITMQ_PORT}:5672"
      - "{RABBITMQ_MANAGEMENT_PORT}:15672"
    volumes:
      - rabbitmq_data_{instance_id}:/var/lib/rabbitmq
    networks:
      - network_{instance_id}

  redis_{instance_id}:
    image: "redis:latest"
    ports:
      - "{REDIS_PORT}:6379"
    volumes:
      - redis_data_{instance_id}:/data
    networks:
      - network_{instance_id}

  celery_worker_{instance_id}:
    build: .
    depends_on:
      - rabbitmq_{instance_id}
      - redis_{instance_id}
    environment:
      - CELERY_BROKER_URL=pyamqp://guest:guest@rabbitmq_{instance_id}//
      - CELERY_RESULT_BACKEND=redis://redis_{instance_id}:6379/0
    command: celery -A app.celery_worker worker --loglevel=info --concurrency=10
    networks:
      - network_{instance_id}

  web_{instance_id}:
    build: .
    depends_on:
      - rabbitmq_{instance_id}
      - redis_{instance_id}
    ports:
      - "{WEB_PORT}:5000"
    environment:
      - CELERY_BROKER_URL=pyamqp://guest:guest@rabbitmq_{instance_id}//
      - CELERY_RESULT_BACKEND=redis://redis_{instance_id}:6379/0
    networks:
      - network_{instance_id}

  flower_{instance_id}:
    build: .
    command: celery --broker=pyamqp://guest:guest@rabbitmq_{instance_id}// -A app.celery_worker flower
    ports:
      - "{FLOWER_PORT}:5555"
    networks:
      - network_{instance_id}
      
volumes:
  rabbitmq_data_{instance_id}:
  redis_data_{instance_id}:

networks:
  network_{instance_id}:
    driver: bridge
"""


def create_docker_compose_file(instance_id, rabbitmq_port, rabbitmq_management_port, redis_port, web_port, flower_port):
    content = DOCKER_COMPOSE_TEMPLATE.format(
        instance_id=instance_id,
        RABBITMQ_PORT=rabbitmq_port,
        RABBITMQ_MANAGEMENT_PORT=rabbitmq_management_port,
        REDIS_PORT=redis_port,
        WEB_PORT=web_port,
        FLOWER_PORT=flower_port
    )
    filename = f"docker-compose-{instance_id}.yml"
    with open(filename, "w") as f:
        f.write(content)
    return filename


def start_containers(instance_id):
    # Allocate ports dynamically
    rabbitmq_port = 5672 + instance_id * 10
    rabbitmq_management_port = 15672 + instance_id * 10
    redis_port = 6379 + instance_id * 10
    web_port = 5000 + instance_id * 10
    flower_port = 5555 + instance_id * 10

    compose_file = create_docker_compose_file(instance_id, rabbitmq_port, rabbitmq_management_port, redis_port,
                                              web_port, flower_port)
    subprocess.run(["docker-compose", "-f", compose_file, "up", "-d"])


def stop_containers(instance_id):
    compose_file = f"docker-compose-{instance_id}.yml"
    subprocess.run(["docker-compose", "-f", compose_file, "down"])


def remove_containers(instance_id):
    compose_file = f"docker-compose-{instance_id}.yml"
    subprocess.run(["docker-compose", "-f", compose_file, "down", "-v"])
    if os.path.exists(compose_file):
        os.remove(compose_file)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python gerenciar_containers.py <start|stop|remove> <instance_id>")
        sys.exit(1)

    command = sys.argv[1]
    instance_id = int(sys.argv[2])

    if command == "start":
        start_containers(instance_id)
    elif command == "stop":
        stop_containers(instance_id)
    elif command == "remove":
        remove_containers(instance_id)
    else:
        print("Invalid command. Use 'start', 'stop', or 'remove'.")
