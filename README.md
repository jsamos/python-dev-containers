# Generic Python Scripting Environment

This is a generic Python scripting environment designed to facilitate the development and execution of Python scripts. It includes a Docker setup for easy environment management and isolation.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

1. **Build and start the Docker containers**:
    ```sh
    docker-compose up --build
    ```

### Running `script.py`

The Dockerfile contains CMD ["tail", "-f", "/dev/null"] to keep it running


To run `script.py` inside the Docker container, use the following command:

```sh
docker-compose exec -it app1 bash
```

Then Execute the script:

```sh
python script.py
```

### Running Tests

```sh
docker-compose exec -it app1 bash
```

```sh
pytest
```