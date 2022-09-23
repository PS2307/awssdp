from flask import flask

app = Flask(__name__)

@app.route("\reva")
def reva_home():
    return{"data": "It's created."}

if __name__=="__main__":
    app.run(debug=True)