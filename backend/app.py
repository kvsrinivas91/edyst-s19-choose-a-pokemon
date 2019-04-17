from flask import Flask,jsonify
import json
app = Flask(__name__)
 
@app.route('/api/pokemon')
def hello():
    data={}
    foo=["bulbasaur","charmander","squirtle"]
    data["pokemon"]=foo
    bar=json.dumps(data)
    return bar
 
if __name__ == '__main__':
    app.run(host='localhost' ,port=8006)