document.addEventListener('DOMContentLoaded', function() {
    const uploadForm = document.getElementById('upload-form');
    const chatForm = document.getElementById('chat-form');
    const chatMessages = document.getElementById('chat-messages');
    const predictionResult = document.getElementById('prediction-result');

    // Handle image upload and prediction
    uploadForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const fileInput = document.getElementById('image-input');
        const file = fileInput.files[0];
        
        if (!file) {
            showError('Please select an image file');
            return;
        }
        
        const formData = new FormData();
        formData.append('file', file);
        
        try {
            const response = await fetch('/upload', {
                method: 'POST',
                body: formData
            });
            
            const result = await response.json();
            
            if (response.ok) {
                showPrediction(result);
            } else {
                showError(result.error);
            }
        } catch (error) {
            showError('Error uploading file: ' + error.message);
        }
    });

    // Handle chat interactions
    chatForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const userInput = document.getElementById('user-input');
        const message = userInput.value.trim();
        
        if (!message) return;
        
        // Add user message to chat
        addMessage(message, 'user');
        userInput.value = '';
        
        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message })
            });
            
            const result = await response.json();
            
            if (response.ok) {
                addMessage(result.response, 'bot');
            } else {
                showError(result.error);
            }
        } catch (error) {
            showError('Error sending message: ' + error.message);
        }
    });

    // Helper functions
    function showPrediction(result) {
        predictionResult.innerHTML = `
            <div class="success">
                <p><strong>Prediction:</strong> ${result.prediction}</p>
                <p><strong>Confidence:</strong> ${(result.probability * 100).toFixed(2)}%</p>
            </div>
        `;
    }

    function showError(message) {
        predictionResult.innerHTML = `
            <div class="error">
                <p>${message}</p>
            </div>
        `;
    }

    function addMessage(content, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;
        messageDiv.textContent = content;
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});