// frontend/src/components/AddDocumentComponent.js

import React, { useState } from 'react';
import axios from 'axios';

const AddDocumentComponent = () => {
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');
    const [message, setMessage] = useState('');

    // فراخوانی API برای ذخیره مستند
    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://backend:5000/add-document', { title, content });
            setMessage(response.data.message);
            setTitle('');
            setContent('');
        } catch (error) {
            setMessage('Error adding document. Please try again.');
            console.error('Error adding document:', error);
        }
    };

    return (
        <div className="add-document-container">
            <h2>Add New Document</h2>
            {message && <p className={message.includes('Error') ? 'error' : 'success'}>{message}</p>}
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label htmlFor="title">Title:</label>
                    <input
                        type="text"
                        id="title"
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                        placeholder="Enter document title"
                        required
                        className="form-control"
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="content">Content:</label>
                    <textarea
                        id="content"
                        value={content}
                        onChange={(e) => setContent(e.target.value)}
                        placeholder="Enter document content"
                        required
                        className="form-control"
                        rows="5"
                    ></textarea>
                </div>
                <button type="submit" className="btn btn-primary">Add Document</button>
            </form>
        </div>
    );
};

export default AddDocumentComponent;