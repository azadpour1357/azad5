// frontend/src/components/DocumentListComponent.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';

const DocumentListComponent = () => {
    const [documents, setDocuments] = useState([]);

    useEffect(() => {
        fetchDocuments();
    }, []);

    const fetchDocuments = async () => {
        try {
            const response = await axios.get('http://backend:5000/get-documents');
            setDocuments(response.data);
        } catch (error) {
            console.error('Error fetching documents:', error);
        }
    };

    return (
        <div className="document-list-container">
            <h2>Document List</h2>
            <ul className="list-group">
                {documents.map((doc, index) => (
                    <li key={index} className="list-group-item">
                        <strong>{doc.title}</strong>: {doc.content.substring(0, 50)}...
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default DocumentListComponent;