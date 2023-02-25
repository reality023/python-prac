from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    return "TEST Code 입니다"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)