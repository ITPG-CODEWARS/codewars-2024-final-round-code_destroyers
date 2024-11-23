// Example CODE
const axios = require('axios');

const hostname = '192.168.22.163'
const port = 5000

const getRequests = async (resource) => {
    let response
    try {
        response = await axios.get(`http://${hostname}:${port}/getTrainData/${resource}`)
    } catch (error) {
        console.error('Error making GET request:', error);
        throw new Error('Error making GET request:', error)
    }
    return response
}

getRequests('getalltraindata').then(response => {
    console.log(response.data);
});
