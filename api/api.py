from flask import Flask, jsonify, request 
from flask_restful import Resource, Api

from init import loadConfig
import utils
import database
  
config = loadConfig()
app = Flask(__name__) 
api = Api(app)

# class Hello(Resource): 
#     def get(self): 
#         return jsonify({'message': 'hello world'}) 
  
#     def post(self): 
#         data = request.get_json()
#         return jsonify({'data': data}), 201

  
class Square(Resource):
    def get(self, num):
        return jsonify({'square': num**2})
    

class GetNewTrainData(Resource):
    def get(self):
        data = utils.TrainObj()
        data.set_route_start("Kolkata")
        data.set_route_end("Delhi")
        data.set_route_estimate("10 hours")
        data.set_bording_time("10:00")
        data.set_departure_time("10:30")
        data.set_arrival_time("20:30")
        database.insert_train_data(data)
        return jsonify({'message': data.get_as_dict()})
    
class GetAllTrainData(Resource):
    def get(self, start, end):
        data = database.get_all_train_data()
        response = []
        for i in data:
            response.append(i.get_as_dict())
            
        return jsonify({'message': response})
            
  

api.add_resource(Square, '/square/<int:num>')
api.add_resource(GetNewTrainData, '/getnewtraindata')
api.add_resource(GetAllTrainData, '/getalltraindata/<string:start>/<string:end>')


# data: utils.TrainObj = utils.TrainObj()
# data.set_route_start("Kolkata")
# print(data.get_as_dict())

def main():
    print(config["host"] + str(config["port"]))
    app.run(debug=True, host=config["host"], port=config["port"])

if __name__ == '__main__': 
    from main import main
    main()