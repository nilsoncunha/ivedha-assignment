# Test iVedha

This repo contains scripts to execute test assignment

p.s.: This commands below was executed in S.O based Unix

To reproduce this project is necessary 
1. `docker` and `docker-compose`
2. recommended create a `.venv` 

Create `.venv`
```bash
# create .venv
python -m venv .venv

# activate .venv
source .venv/bin/activate

# install libs with requirements.txt
pip install -r requirements.txt
```

## Test1

To execute test 1, observe if you stay in path test1
```bash
cd test1
```
Start services in Docker, will download images and config containers
```bash
docker-compose up -d
```
When all containers is `running`, its ok to execute other commands.
Access the REST API to know if the service its ok.
- REST API - [http://localhost:5000/](http://localhost:5000/)
- Elasticsearch - [http://localhost:5601/](http://localhost:5601/)
  - user: elastic
  - password: elastic

To get status about services up or down, execute script below.
```bash
docker exec -it rest_service python scripts/monitor_services.py
```
The status files will save in `logs` path.

To write files in Elasticsearch has two methods:
1. Execute with software similar `insomnia` or `postman`

If use with `insomnia`, for exemple, need select method `POST` and insert
address `http://localhost:5000/add`. In body, add the content json e.i:
```json
{
    "application_name": "rabbitmq",
    "application_status": "UP",
    "host_name": "localhost",
    "created_at": "20250309180746"
}
```

2. Write files executing script `insert_logs_es.py`. This process write in Elasticsearch and move the files from `logs`
to `logs/processed` This is good because in other moment don't wrote duplicated files
```bash
docker exec -it rest_service python scripts/insert_logs_es.py
```

After insert data on Elasticsearch, consult data with `insomnia` (method GET) or browser. 
- To consult all data -  [http://localhost:5000/healthcheck](http://localhost:5000/healthcheck)
- To consult specify service - [http://localhost:5000/healthcheck/httpd](http://localhost:5000/healthcheck/httpd)