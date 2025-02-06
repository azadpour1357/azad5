// frontend/src/components/TaxCalculatorComponent.js

import React, { useState } from 'react';
import axios from 'axios';

const TaxCalculatorComponent = () => {
    const [income, setIncome] = useState('');
    const [taxRate, setTaxRate] = useState('');
    const [taxAmount, setTaxAmount] = useState(null);

    const calculateTax = async () => {
        try {
            const response = await axios.post('http://backend:5000/calculate-tax', { income, tax_rate: taxRate }, {
                headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
            });
            setTaxAmount(response.data.tax_amount);
        } catch (error) {
            console.error('Error calculating tax:', error);
        }
    };

    return (
        <div className="tax-calculator-container">
            <h2>Tax Calculator</h2>
            <input
                type="number"
                value={income}
                onChange={(e) => setIncome(e.target.value)}
                placeholder="Enter income"
                required
                className="form-control mb-3"
            />
            <input
                type="number"
                value={taxRate}
                onChange={(e) => setTaxRate(e.target.value)}
                placeholder="Enter tax rate (%)"
                required
                className="form-control mb-3"
            />
            <button onClick={calculateTax} className="btn btn-primary w-100">Calculate Tax</button>
            {taxAmount !== null && (
                <p className="mt-3">Your tax amount: {taxAmount}</p>
            )}
        </div>
    );
};

export default TaxCalculatorComponent;