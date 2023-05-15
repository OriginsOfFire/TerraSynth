import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import {BrowserRouter, Route, Routes} from "react-router-dom";
import LoginForm from "./components/LoginForm";
import Configurations from "./components/Configurations";
import Header from "./components/Header";
import Footer from "./components/Footer";

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
      <BrowserRouter>
          <Header />
          <Routes>
              <Route index element={<App />} />
              <Route path="login" element={<LoginForm />} />
              <Route path="configurations" element={<Configurations/>}/>
          </Routes>
          <Footer />
      </BrowserRouter>
  </React.StrictMode>
);
