from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "success":True,
        "msg":"Welcome to BookMark API"
    })

#Serve the application
if __name__ == '__main__':
    app.run(debug=True)
