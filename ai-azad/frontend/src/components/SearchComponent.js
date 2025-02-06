// frontend/src/components/SearchComponent.js

import React, { useState } from 'react';
import axios from 'axios';

const SearchComponent = () => {
    const [query, setQuery] = useState('');
    const [results, setResults] = useState([]);

    const handleSearch = async () => {
        try {
            const response = await axios.post('http://backend:5000/search', { query }, {
                headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
            });
            setResults(response.data);
        } catch (error) {
            console.error('Error fetching search results:', error);
        }
    };

    return (
        <div className="search-container">
            <input
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Enter search query"
                className="form-control mb-3"
            />
            <button onClick={handleSearch} className="btn btn-primary w-100">Search</button>

            <ul className="list-group mt-3">
                {results.map((result, index) => (
                    <li key={index} className="list-group-item">
                        <strong>{result.title}</strong>: {result.content.substring(0, 50)}...
                        <br />
                        Classification: {result.classification}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default SearchComponent;