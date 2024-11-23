//
const axios = require('axios');

const hostname = 'localhost'
const port = 5000

trainData = [
    { 
        "routeID": "Something DONT NEED TO DISPLAY OR USE",
        "routeStart": "Baltimore, MD",
        "routeEnd": "Washington, DC",
        "departureTime": "TIMESTEMP",
        "arrivalTime": "TIMESTEMP2",
        "bordingTime": "TIMESTEMP3",
        "routeEstimate": "55", // minutes
    },
    {
        "routeID": "Something DONT NEED TO DISPLAY OR USE",
        "routeStart": "Washington, DC",
        "routeEnd": "Baltimore, MD",
        "departureTime": "TIMESTEMP",
        "arrivalTime": "TIMESTEMP2",
        "bordingTime": "TIMESTEMP3",
        "routeEstimate": "55", // minutes
    }
];

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

getTrainData('Kolkata', 'Delhi').then(response => {
    console.log(response.data);
});
