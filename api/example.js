// Example CODE
const axios = require('axios');

const hostname = '192.168.22.163'
const port = 5000

const getSquare = async (num) => {
    let response
    try {
        response = await axios.get(`http://${hostname}:${port}/square/${num}`)
    } catch (error) {
        console.error('Error making GET request:', error);
        throw new Error('Error making GET request:', error)
    }
    return response
}

getSquare(4).then(response => {
    console.log(response.data);
});
