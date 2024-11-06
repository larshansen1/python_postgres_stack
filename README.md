# Python-Postgres-NGINX Dockerized Application

## Purpose
This project is a simple Dockerized stack that includes:
- A **Python** application (using Flask) that connects to a **PostgreSQL** database to retrieve a sample record.
- An **NGINX** server configured as a reverse proxy to route requests to the Python application.
- A **PostgreSQL** database initialized with a sample table and record.

The setup demonstrates a basic microservice architecture using Docker Compose, making it easy to start, stop, and scale the services.

## Usage

Follow these steps to set up and run the application:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/larshansen1/python_postgres_stack.git
   cd python_postgres_stack
   ```

2. **Copy the .env Template and Fill Out Values**

   Copy the `.env.template` file to create a new `.env` file, then replace placeholder values with your desired configuration:

   ```bash
   cp .env.template .env
   ```

   Open `.env` and set values for:
   - `POSTGRES_USER`
   - `POSTGRES_PASSWORD`
   - `POSTGRES_DB`
   - `DATABASE_URL`

3. **Start the Application with Docker Compose**

   Build and start the services in detached mode:

   ```bash
   docker-compose up --build -d
   ```

4. **Access the Application**

   Once the containers are up, access the Python application through NGINX at [http://localhost:80](http://localhost:80).

   You should see a JSON response with a sample record retrieved from the PostgreSQL database.

## Documentation

### Directory Structure

The directory structure of the project is as follows:

```plaintext
project/
├── docker-compose.yml      # Docker Compose configuration
├── .env.template           # Environment variable template
├── app/                    # Python application
│   ├── Dockerfile          # Dockerfile for Python app
│   ├── main.py             # Flask app to query PostgreSQL
│   └── requirements.txt    # Python dependencies
├── nginx/                  # NGINX configuration
│   └── default.conf        # NGINX reverse proxy settings
└── postgres/               # PostgreSQL initialization
    └── init.sql            # SQL script to initialize database
```

### Notes

- **Environment Variables**: The `.env` file is used to store sensitive information and should not be committed to version control.
- **Persistence**: The PostgreSQL database uses a Docker volume for data persistence.
- **Ports**: Ensure that port `80` is available on your host for NGINX to route requests properly.

Enjoy experimenting with the setup, and feel free to extend it to suit your needs!

