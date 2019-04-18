from flask import Flask,jsonify,render_template
import json
app = Flask(__name__)
 

@app.route('/api/pokemon')
def hello():
    data={}
    foo=["bulbasaur","charmander","squirtle"]
    data["pokemon"]=foo
    bar=json.dumps(data)
    return bar

@app.errorhandler(404)  
def page_not_found(error=None):
  return ('Error 404`'), 404
 
if __name__ == '__main__':
    app.run(host='localhost' ,port=8006)