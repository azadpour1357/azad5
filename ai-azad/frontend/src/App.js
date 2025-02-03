// frontend/src/App.js

import React from 'react';
import SearchComponent from './components/SearchComponent';
import AddDocumentComponent from './components/AddDocumentComponent';
import DocumentListComponent from './components/DocumentListComponent';

function App() {
    return (
        <div className="App container mt-5">
            <h1 className="text-center">Document Management System</h1>
            <hr />
            <SearchComponent />
            <hr />
            <AddDocumentComponent />
            <hr />
            <DocumentListComponent />
        </div>
    );
}

export default App;