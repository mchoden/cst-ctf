"""
Internal Service — Port 5002
Simulates internal microservices. Targets for SSRF and Microservices labs.
"""
import os, json, hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)

def _flag(name):
    _s = os.environ.get("FLAG_SECRET", "cst-workshop-2026-bhutan")
    return "FLAG{" + hashlib.sha256(f"{_s}:{name}".encode()).hexdigest()[:24] + "}"

FLAGS = {k: _flag(k) for k in ["ssrf_1","ssrf_2","ssrf_3","micro_1","micro_2","micro_3"]}

@app.route("/")
def index():
    return jsonify({"service":"Internal Network","status":"running"})

@app.route("/admin")
def admin():
    return jsonify({"service":"Admin Panel","flag":FLAGS["ssrf_1"],
                    "users":["admin","alice","bob","charlie"]})

@app.route("/secret-service-7890")
def secret_svc():
    return jsonify({"service":"Analytics","flag":FLAGS["ssrf_2"]})

@app.route("/latest/meta-data/")
def meta_root():
    return "ami-id\nhostname\niam/", 200, {"Content-Type":"text/plain"}

@app.route("/latest/meta-data/iam/")
def meta_iam():
    return "security-credentials/", 200, {"Content-Type":"text/plain"}

@app.route("/latest/meta-data/iam/security-credentials/")
def meta_list():
    return "workshop-ec2-role", 200, {"Content-Type":"text/plain"}

@app.route("/latest/meta-data/iam/security-credentials/workshop-ec2-role")
def meta_creds():
    return jsonify({"Code":"Success","AccessKeyId":"AKIA"+FLAGS["ssrf_3"],
                    "SecretAccessKey":"wJalrXUtnFEMI/FAKE/KEY","flag":FLAGS["ssrf_3"]})

@app.route("/user-service/users")
def user_svc():
    return jsonify({"service":"User Service","flag":FLAGS["micro_1"],
                    "users":[{"id":1,"username":"admin","role":"admin"},
                             {"id":2,"username":"alice","role":"user"}]})

@app.route("/debug")
def debug_ep():
    return jsonify({"service":"Debug","flag":FLAGS["micro_2"],
                    "env":{"DB_HOST":"internal-db.prod","DB_PASS":"super-secret-123",
                           "JWT_SECRET":"workshop-jwt-secret-123"}})

@app.route("/payment-service/process", methods=["POST","PUT","PATCH"])
def payment():
    data = json.loads(request.get_data() or "{}")
    return jsonify({"service":"Payment","flag":FLAGS["micro_3"],"processed":data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
