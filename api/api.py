from flask import Flask, jsonify, request 
from flask_restful import Resource, Api

from init import loadConfig
import utils
import database
  
config = loadConfig()
app = Flask(__name__) 
api = Api(app)

class GetAllTrainData(Resource):
    def get(self, start, end):
        data = database.get_train_data(start, end)
        if data is None:
            return jsonify({'message': 'No data found'})
        response = []
        for i in data:
            response.append(i.get_as_dict())
            
        return jsonify({'message': response})
    

class insertTrainData(Resource):
    def post(self):
        data = request.get_json()
        data = utils.TrainObj(data["routeStart"], data["routeEnd"], data["routeEstimate"], data["bordingTime"], data["departureTime"], data["arrivalTime"])
        database.insert_train_data(data)
        return jsonify({'message': 'Data inserted successfully'})
            
  

api.add_resource(GetAllTrainData, '/getalltraindata/<string:start>/<string:end>')
api.add_resource(insertTrainData, '/inserttraindata')

def main():
    print(config["host"] + str(config["port"]))
    app.run(debug=True, host=config["host"], port=config["port"])

if __name__ == '__main__': 
    from main import main
    main()