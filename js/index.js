// Smooth scrolling for anchor links
document.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', (event) => {
        event.preventDefault();
        const target = document.querySelector(link.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});


const getSquare = async (num) => {
    let response;
    try {
        //------------------------- edit the local host
        response = await axios.get(`http://127.0.0.1:69420/square/${num}`);
    } catch (error) {
        console.error('Error making GET request:', error);
        throw new Error('Error making GET request:', error);
    }
    return response;
};

// butona da raboti
document.getElementById('square-btn').addEventListener('click', async () => {
    const inputElement = document.getElementById('number-input');
    const resultElement = document.getElementById('result');

    // Get the number from the input field.
    const num = inputElement.value;

    // Validate the input
    if (isNaN(num) || num.trim() === '') {
        resultElement.textContent = 'Please enter a valid number!';
        return;
    }

    try {
        // Fetch the square of the number
        const response = await getSquare(num);
        const square = response.data; // returnJSON

        // Display the result
        resultElement.textContent = `The square of ${num} is ${square}.`;
    } catch (error) {
        resultElement.textContent = 'Error fetching square. Please try again later.';
    }
});
