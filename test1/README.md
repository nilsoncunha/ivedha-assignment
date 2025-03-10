# Test1

## Starting Services with Docker
Start the services using Docker Compose:
```bash
docker-compose up -d
```
When all containers are running, access the following services to verify if everything is working correctly:

- **REST API** - http://localhost:5000/
- **Elasticsearch** - http://localhost:5601/
  - Username: `elastic`
  - Password: `elastic`

---

## Monitoring Service Status
To check the status of the services (whether they are up or down), run the following script:
```bash
docker exec -it rest_service python scripts/monitor_services.py
```
The status files will be saved in the `logs` directory.

---

## Writing Data to Elasticsearch
There are two methods to write data into Elasticsearch:

### 1. Using API Tools (Insomnia or Postman)
- Select the **POST** method.
- Set the endpoint to: http://localhost:5000/add
- In the body, add the JSON content, for example:
```json
{
    "application_name": "rabbitmq",
    "application_status": "UP",
    "host_name": "localhost",
    "created_at": "20250309180746"
}
```

### 2. Using a Python Script 
Execute the following script to write data to Elasticsearch and automatically move processed files from `logs` to `logs/processed. 
This helps avoid writing duplicate files in the future.
```bash
docker exec -it rest_service python scripts/insert_logs_es.py
```

---

## Querying Data in Elasticsearch
After inserting data, you can query it using **Insomnia** (with the GET method) or directly via a browser:

- **To retrieve all data** -  [http://localhost:5000/healthcheck](http://localhost:5000/healthcheck)
- **To retrieve data for a specific service:** - [http://localhost:5000/healthcheck/httpd](http://localhost:5000/healthcheck/httpd)