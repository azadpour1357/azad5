import React from 'react';
import ReactDOM from 'react-dom';
//import '@mui/material/styles';
import './index.css';  // اگر قبلاً فایل index.css وجود داشت، آن را حذف کنید
import './styles.css';  // اضافه کردن فایل styles.css
import App from './App';
import 'bootstrap/dist/css/bootstrap.min.css';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);