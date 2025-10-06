import os
import subprocess
import pickle
from flask import Flask, request

app = Flask(__name__)

# ❌ Hardcoded secret (should be caught by Semgrep)
API_KEY = "AKIA1234567890FAKEKEY"
"app-key", "7db6ce4a-c63c-4628-9f51-08b277b764b1",
"password\": \"V2VsY29tZUAxMjM=\"",

# ❌ Command Injection vulnerability
@app.route("/run")
def run():
    cmd = request.args.get("cmd")
    os.system(cmd)  # unsafe: user input directly passed to shell

# ❌ Insecure deserialization
@app.route("/load")
def load():
    data = request.args.get("data")
    obj = pickle.loads(data)  # unsafe

# ❌ Subprocess with shell=True
@app.route("/exec")
def exec_cmd():
    user_input = request.args.get("cmd")
    subprocess.call(f"echo {user_input}", shell=True)  # unsafe

if __name__ == "__main__":
    app.run(debug=True)
