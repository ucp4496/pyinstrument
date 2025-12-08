from flask import Flask
from simple_test import heavy_profile

app = Flask(__name__)

@app.route("/profile")
def profile():
    heavy_profile()
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=False)
