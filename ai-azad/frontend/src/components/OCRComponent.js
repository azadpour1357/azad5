// frontend/src/components/OCRComponent.js

import React, { useState } from 'react';
import axios from 'axios';

const OCRComponent = () => {
    const [file, setFile] = useState(null);
    const [text, setText] = useState('');

    const handleUpload = async (e) => {
        e.preventDefault();
        if (!file) return;

        const formData = new FormData();
        formData.append('file', file);

        try {
            const res = await axios.post('http://backend:5000/extract-text', formData, {
                headers: { Authorization: `Bearer ${localStorage.getItem('token')}`, 'Content-Type': 'multipart/form-data' }
            });
            setText(res.data.text);
        } catch (error) {
            console.error('Error extracting text:', error);
        }
    };

    return (
        <div className="ocr-container">
            <h2>OCR Document Upload</h2>
            <form onSubmit={handleUpload}>
                <input
                    type="file"
                    onChange={(e) => setFile(e.target.files[0])}
                    required
                    className="form-control mb-3"
                />
                <button type="submit" className="btn btn-primary w-100">Upload and Extract Text</button>
            </form>
            {text && <pre className="mt-3">{text}</pre>}
        </div>
    );
};

export default OCRComponent;