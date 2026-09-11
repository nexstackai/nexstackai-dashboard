# NexStackAI DevOps Dashboard

A hands-on Docker project from the **NexStackAI Docker Explained Simply Series**.

This project brings together the Docker concepts covered throughout the series into one real multi-container application.

The application consists of a **Python Flask web application** connected to a **PostgreSQL database**, with the complete environment managed using **Docker Compose**.

---

## What You'll Build

The project demonstrates how multiple Docker building blocks work together in a real application:

* Dockerfile
* Docker Images
* Docker Containers
* Port Mapping
* Environment Variables
* Docker Compose
* Docker Networks
* Container-to-Container Communication
* Docker Volumes
* PostgreSQL
* Health Checks
* Docker Logs
* Persistent Data

---

## Architecture

```text
Browser
   |
   | localhost:8080
   |
   v
+-------------------+
|   Web Container   |
|   Python + Flask  |
+---------+---------+
          |
          | Docker Network
          | DB_HOST=database
          |
          v
+-------------------+
| Database Container|
|   PostgreSQL 16   |
+---------+---------+
          |
          v
+-------------------+
|   Docker Volume   |
|  Persistent Data  |
+-------------------+
```

Docker Compose automatically creates a network for the application, allowing the `web` service to communicate with the `database` service using its service name.

---

## Project Structure

```text
nexstackai-dashboard/
|
├── app/
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── style.css
|
├── requirements.txt
├── init.sql
├── Dockerfile
├── compose.yaml
└── README.md
```

### Application Files

The application files are already provided so you can focus on learning Docker.

`app/app.py` contains the Flask web application and PostgreSQL connection logic.

`app/templates/index.html` contains the dashboard UI.

`app/static/style.css` contains the dashboard styling.

`requirements.txt` contains the required Python dependencies.

`init.sql` initializes PostgreSQL with sample deployment data.

---

# Prerequisites

Before starting, make sure you have:

* Docker Desktop installed.
* Docker Compose available.
* Git installed if you want to clone the repository.
* A web browser.
* A terminal such as PowerShell, Command Prompt, Terminal, or Bash.

Verify Docker:

```bash
docker --version
```

Verify Docker Compose:

```bash
docker compose version
```

---

# Clone the Repository

```bash
git clone https://github.com/nexstackai/nexstackai-dashboard.git
```

Move into the project directory:

```bash
cd nexstackai-dashboard
```

---

# Build the Docker Image

The `Dockerfile` packages the Flask application into a Docker image.

```bash
docker build -t nexstackai-dashboard:v1 .
```

Verify the image:

```bash
docker images
```

You should see:

```text
nexstackai-dashboard    v1
```

---

# Validate the Compose Configuration

Before starting the application, validate the Compose configuration:

```bash
docker compose config
```

This allows Docker Compose to parse the YAML configuration and can help identify configuration or formatting problems.

---

# Start the Application

Start the complete application:

```bash
docker compose up -d
```

Docker Compose will create and start the required services.

Check their status:

```bash
docker compose ps
```

You should see both the web application and PostgreSQL database running.

---

# Open the Dashboard

Open your browser and visit:

```text
http://localhost:8080
```

You should see the **NexStackAI DevOps Dashboard**.

The dashboard is running from the Flask container while its deployment data is retrieved from PostgreSQL running in a separate container.

---

# Container-to-Container Communication

The web application connects to PostgreSQL using:

```text
DB_HOST=database
```

`database` is the Compose service name.

Docker Compose provides internal networking and service-name resolution, so the application does not need to hardcode the database container's IP address.

You can verify name resolution from inside the web container:

```bash
docker compose exec web python -c "import socket; print(socket.gethostbyname('database'))"
```

---

# Verify PostgreSQL Data

Query the database directly:

```bash
docker compose exec database psql -U admin -d dashboard -c "SELECT * FROM deployments;"
```

The deployment records returned by PostgreSQL are the records displayed on the dashboard.

---

# Test Data Persistence

Bring the application down:

```bash
docker compose down
```

The containers are removed, but the named database volume remains.

Check the available volumes:

```bash
docker volume ls
```

Start the application again:

```bash
docker compose up -d
```

Refresh:

```text
http://localhost:8080
```

The deployment records should still be available because PostgreSQL stores its data in a Docker named volume.

---

## Important: Removing the Volume

Running:

```bash
docker compose down
```

removes the containers and Compose network while keeping the named volume.

Running:

```bash
docker compose down -v
```

also removes the named volume.

Use the `-v` option only when you intentionally want to remove the persisted database data.

---

# Troubleshooting

Check container status:

```bash
docker compose ps
```

View the web application logs:

```bash
docker compose logs web
```

View the PostgreSQL logs:

```bash
docker compose logs database
```

Follow the logs continuously:

```bash
docker compose logs -f
```

---

# Stop the Application

To stop and remove the application containers:

```bash
docker compose down
```

To also remove the persistent volume:

```bash
docker compose down -v
```

---

# Docker Concepts Demonstrated

This project brings together concepts covered throughout the **Docker Explained Simply Series**:

```text
Application Code
       |
       v
   Dockerfile
       |
       v
  Docker Image
       |
       v
Docker Compose
   /       \
  v         v
Web       Database
Container  Container
   \         /
    \       /
   Docker Network
         |
         v
   Docker Volume
         |
         v
  Persistent Data
```

Instead of seeing Docker images, containers, networks, volumes, and Compose as separate topics, this project demonstrates how they work together to run a complete application.

---

# Docker Explained Simply Series

This project is the final hands-on project from the **NexStackAI Docker Explained Simply Series**.

The series takes you from the fundamentals of Docker through images, containers, Dockerfiles, volumes, networking, Docker Compose, registries, troubleshooting, and finally this complete application.

## Watch NexStackAI

YouTube:

https://www.youtube.com/@NexStackAI

Subscribe to the YouTube channel and follow along with each episode, step by step!

---

## Repository

https://github.com/nexstackai/nexstackai-dashboard

---

## Built with

* Docker
* Docker Compose
* Python
* Flask
* PostgreSQL

---

## About NexStackAI

**NexStackAI** focuses on making technologies such as Docker, Kubernetes, DevOps, AI, and modern cloud-native tools easier to understand through simple explanations, visual analogies, and hands-on projects.

If this project helped you understand how Docker's building blocks work together, explore the complete Docker Explained Simply Series and continue building with NexStackAI.
