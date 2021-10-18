from flask import Flask, Response

app = Flask(__name__)

@app.route("/test", methods=['GET'])
def test():
    return Response("<h1>I'm alive!</h1>",status=200, mimetype='text/html')

app.run()