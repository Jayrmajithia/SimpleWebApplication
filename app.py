from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the index page for Lyft apprenticeship program"

@app.route("/hi")
def who():
    return "Who are you?"

@app.route("/hi/<username>")
def greet(username):
    return f"Hi there, {username} welcome to the Lyft apprenticeship application!"

@app.route("/test", methods=["POST"])
def test():
    req_data = request.get_json()
    if not req_data or not req_data["string_to_cut"]:
        return {"Error":"Error No Json string found"}
    string_to_cut = req_data["string_to_cut"]
    i = 2
    res = ""
    while i < len(string_to_cut):
        res += string_to_cut[i]
        i += 3
    return {"return_string":res}
