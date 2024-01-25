from flask import Flask

app = Flask(__name__)

# Only one path for this case
@app.route("/")
def index(): 
    return "Hello from flask"

if  __name__ == "__main__":
    app.run()
