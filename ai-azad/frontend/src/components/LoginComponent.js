// frontend/src/components/LoginComponent.js

import React, { useState } from 'react';
import axios from 'axios';

const LoginComponent = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = async () => {
        try {
            const response = await axios.post('http://backend:5000/login', { username, password });
            localStorage.setItem('token', response.data.access_token);
        } catch (error) {
            console.error('Login failed:', error);
        }
    };

    return (
        <div className="login-container">
            <h2>Login</h2>
            <input
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Username"
                required
                className="form-control mb-3"
            />
            <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Password"
                required
                className="form-control mb-3"
            />
            <button onClick={handleLogin} className="btn btn-primary w-100">Login</button>
        </div>
    );
};

export default LoginComponent;