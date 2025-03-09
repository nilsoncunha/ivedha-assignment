from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch

app = Flask(__name__)

# Configuração do Elasticsearch
es = Elasticsearch(hosts=["https://es01:9200"],
                   basic_auth=('elastic', 'elastic'),
                   verify_certs=False)

@app.route('/')
def check_connection():
    try:
        if es.ping():
            return jsonify({"status": "Connected to Elasticsearch"})
        else:
            return jsonify({"status": "Connection failed"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/add', methods=['POST'])
def add_to_elasticsearch():
    data = request.json
    try:
        es.index(index="service_status", body=data)
        return jsonify({"status": "success", "data": data}), 201
    except Exception as e:
        return jsonify({"return": e})

@app.route('/delete/<doc_id>', methods=['GET'])
def delete_index(doc_id):
    try:
        es.delete(index="service_status", id=doc_id)
        return jsonify({"status": "success"}), 201
    except Exception as e:
        return jsonify({"return": e})

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    res = es.search(index="service_status", body={"query": {"match_all": {}}})
    return jsonify(res['hits']['hits'])

@app.route('/healthcheck/<service_name>', methods=['GET'])
def healthcheck_service(service_name):
    res = es.search(index="service_status", body={"query": {"match": {"application_name": service_name}}})
    return jsonify(res['hits'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)