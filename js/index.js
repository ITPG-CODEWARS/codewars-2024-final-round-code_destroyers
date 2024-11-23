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

// chat "functionallity"
document.getElementById('send-btn').addEventListener('click', sendMessage);

function sendMessage() {
    let messageInput = document.getElementById('message');
    let message = messageInput.value;

    if (message.trim() === "") {
        return;
    }

    // Create message element
    let messageElement = document.createElement('div');
    messageElement.classList.add('chat-message', 'user');
    messageElement.innerText = message;

    // Append message to chat box
    let chatBox = document.getElementById('chat-box');
    chatBox.appendChild(messageElement);

    // Scroll to bottom
    chatBox.scrollTop = chatBox.scrollHeight;

    // Clear input field
    messageInput.value = "";
}

// Optional: To simulate a bot response
setInterval(() => {
    let botMessage = document.createElement('div');
    botMessage.classList.add('chat-message');
    botMessage.innerText = "Bot: Вашето съобщение беше получено!";

    let chatBox = document.getElementById('chat-box');
    chatBox.appendChild(botMessage);
    chatBox.scrollTop = chatBox.scrollHeight;
}, 5000); // Bot responds every 5 seconds
