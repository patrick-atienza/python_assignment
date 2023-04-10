# Financial Data API

This is a small service where you can query the latest financial data and average of the specific data within a certain period of time.

## Tech Stack

### FastAPI

ASGI-based web framework

### Poetry

Dependency management tool

### SQLite

Simple database engine

### peewee

ORM. Due to its lack of support on asynchronous transactions using SQLite, peewee-async wasn't used

### Docker

Platform for shipping and deploying applications.

## Local setup

1. Download and install Docker or [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Put ALPHA_VANTAGE_API_KEY in .env file
3. Run project through the following command:"
   ```commandline
   docker-compose up --build app
   ```
4. Auto-generated FastAPI API documentation `http://localhost:8080/docs`
5. Once finished, execute the following command:
   ```commandline
   docker-compose down
   ```

## How to maintain the Alpha Vantage API Key
The API key should be stored as secret since it is a critical data. Using services like AWS KMS, Kubernetes Secrets (using etcd), OpenShift Secrets (using etcd), and the like. Futhermore, the data can be more secured if etcd encryption is enabled.  Maintaining zero-trust is important.

The API key might be also rotated from time to time, and thus, it is also recommended to monitor the API Key and determine if it's still active or not.

Due to the possibility of the API key to be rotated, it is better to have a separate key for each environment.
