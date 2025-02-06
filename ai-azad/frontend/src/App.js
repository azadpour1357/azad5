// frontend/src/App.js
import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import SearchComponent from './components/SearchComponent';
import AddDocumentComponent from './components/AddDocumentComponent';
import DocumentListComponent from './components/DocumentListComponent';
import TaxCalculatorComponent from './components/TaxCalculatorComponent';
import EditDocumentComponent from './components/EditDocumentComponent';
import DeleteDocumentComponent from './components/DeleteDocumentComponent';
import LoginComponent from './components/LoginComponent';
import ChatBotComponent from './components/ChatBotComponent';
import OCRComponent from './components/OCRComponent';

function App() {
    return (
        <Router>
            <div className="App container mt-5">
                <h1 className="text-center">AI-Tax-Azad System</h1>
                <Switch>
                    {/* توجه: استفاده از "component" به جای "element" */}
                    <Route path="/" exact component={LoginComponent} />
                    <Route path="/search" component={SearchComponent} />
                    <Route path="/add-document" component={AddDocumentComponent} />
                    <Route path="/documents" component={DocumentListComponent} />
                    <Route path="/edit-document" component={EditDocumentComponent} />
                    <Route path="/delete-document" component={DeleteDocumentComponent} />
                    <Route path="/tax-calculator" component={TaxCalculatorComponent} />
                    <Route path="/chatbot" component={ChatBotComponent} />
                    <Route path="/ocr" component={OCRComponent} />
                </Switch>
            </div>
        </Router>
    );
}

export default App;