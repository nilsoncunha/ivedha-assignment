import json
import os

from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=["https://es01:9200"],
                   basic_auth=('elastic', 'elastic'),
                   verify_certs=False)

def insert_data_elasticsearch():
    try:
        logs = [f for f in os.listdir('logs') if f.endswith('.json')]
        for log in logs:
            file_path = os.path.join('logs', log)
            with open(file_path) as log_data:
                data = json.load(log_data)
                es.index(index="service_status", body=data)
                print(f"{log} file inserted successfully")
            processed_dir = os.path.join('logs', "processed")
            os.makedirs(processed_dir, exist_ok=True)
            os.rename(file_path, os.path.join(processed_dir, log))
        return "Dados inseridos com sucesso no Elasticsearch."
    except Exception as e:
        return "error", e


if __name__ == "__main__":
    insert_data_elasticsearch()