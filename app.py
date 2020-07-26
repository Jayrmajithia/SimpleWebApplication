from flask import Flask, request, abort

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
    try:
        if not req_data or "string_to_cut" not in req_data:
            raise
        string_to_cut = req_data["string_to_cut"]
        i = 2
        res = ""
        while i < len(string_to_cut):
            res += string_to_cut[i]
            i += 3
        return {"return_string":res}
    except:
        print("Error No Json string found or Parameter is wrong")
        abort(500)
