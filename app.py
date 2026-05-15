from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Mi app de Facebook"

if __name__=="__main__":
    app.run()