import React, { useState } from 'react';
import axios from 'axios';

const SearchComponent = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    try {
      const response = await axios.post('http://backend:5000/search', { query });
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
        className="search-input"
      />
      <button onClick={handleSearch} className="search-button">Search</button>

      <ul className="result-list">
        {results.map((result, index) => (
          <li key={index} className="result-item">
            <h3 className="result-title">{result.title}</h3>
            <p className="result-content">{result.content}</p>
            <p className="result-classification">Classification: {result.classification}</p>
            <h5>Extracted Information:</h5>
            <ul className="entity-list">
              {result.extracted_info.map((entity, idx) => (
                <li key={idx} className="entity-item">
                  <strong>{entity.entity_group}</strong>: {entity.word}
                </li>
              ))}
            </ul>
            <h5>Gathered Information:</h5>
            <ul className="info-list">
              {result.gathered_info.map((info, idx) => (
                <li key={idx} className="info-item">{info}</li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default SearchComponent;