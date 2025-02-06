// frontend/src/components/ChatBotComponent.js

import React, { useState } from 'react';
import axios from 'axios';

const ChatBotComponent = () => {
    const [question, setQuestion] = useState('');
    const [response, setResponse] = useState('');

    const sendMessage = async () => {
        try {
            const res = await axios.post('http://backend:5000/chatbot', { question }, {
                headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
            });
            setResponse(res.data.response);
        } catch (error) {
            console.error('Error fetching chatbot response:', error);
        }
    };

    return (
        <div className="chatbot-container">
            <h2>ChatBot</h2>
            <input
                type="text"
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
                placeholder="Ask a question"
                required
                className="form-control mb-3"
            />
            <button onClick={sendMessage} className="btn btn-primary w-100">Send</button>
            {response && <p className="mt-3">Bot says: {response}</p>}
        </div>
    );
};

export default ChatBotComponent;