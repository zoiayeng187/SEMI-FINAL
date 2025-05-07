from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Ayeng, Zoi Artchelo L. BSIT-||| B "

if __name__ == '__main__':
    app.run(debug=True)