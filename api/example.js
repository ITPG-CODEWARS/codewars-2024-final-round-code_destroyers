// Example CODE
const axios = require('axios');

const getSquare = async (num) => {
    let response
    try {
        response = await axios.get(`http://127.0.0.1:5000/square/${num}`)
    } catch (error) {
        console.error('Error making GET request:', error);
        throw new Error('Error making GET request:', error)
    }
    return response
}

getSquare(4).then(response => {
    console.log(response.data);
});
