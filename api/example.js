// Example CODE
const axios = require('axios');

const hostname = 'localhost'
const port = 5000

class TrainData {
    constructor(routeID, routeStart, routeEnd, routeEstimate, bordingTime, departureTime, arrivalTime) {
        this.routeID = routeID
        this.routeStart = routeStart
        this.routeEnd = routeEnd
        this.routeEstimate = routeEstimate
        this.bordingTime = bordingTime
        this.departureTime = departureTime
        this.arrivalTime = arrivalTime
    }
}

const getTrainData = async (start, end) => {
    let response
    try {
        response = await axios.get(`http://${hostname}:${port}/getalltraindata/${start}/${end}`);
    } catch (error) {
        console.error('Error making GET request:', error);
        throw new Error('Error making GET request:', error)
    }
    return response
}

// getTrainData('Kolkata', 'Delhi').then(response => {
//     console.log(response.data);
// });

// POST request
const insertTrainData = async (trainData) => {
    let response
    try {
        response = await axios.post(`http://${hostname}:${port}/inserttraindata`, trainData);
    } catch (error) {
        console.error('Error making POST request:', error);
        throw new Error('Error making POST request:', error)
    }
    return response
}

insertTrainData(new TrainData(undefined, 'Kolkata', 'Delhi', '12:55', '11:30', '12:00', '12:30')).then(response => {
    console.log(response.data);
});
