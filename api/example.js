// Example CODE
const axios = require('axios');

const hostname = 'localhost'
const port = 5000

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
