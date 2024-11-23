from flask import Flask, jsonify, request 
from flask_restful import Resource, Api 

import utils
from init import loadConfig
  
config = loadConfig()
app = Flask(__name__) 
api = Api(app)

class Hello(Resource): 
    def get(self): 
        return jsonify({'message': 'hello world'}) 
  
    def post(self): 
        data = request.get_json()
        return jsonify({'data': data}), 201

  
class Square(Resource):
    def get(self, num):
        return jsonify({'square': num**2}) 
  
  
api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<int:num>')

def main():
    print(config["host"] + str(config["port"]))
    app.run(debug=True, host=config["host"], port=config["port"])

if __name__ == '__main__': 
    from main import main
    main()