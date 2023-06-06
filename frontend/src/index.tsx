import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import {BrowserRouter, Route, Routes} from "react-router-dom";
import LoginForm from "./components/LoginForm";
import Configurations from "./components/Configurations";
import Header from "./components/Header";
import Footer from "./components/Footer";
import SignUpForm from "./components/SignUpForm";
import Providers from "./components/Providers";

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
              <Route path="signup" element={<SignUpForm />} />
              <Route path="providers" element={<Providers/>} />
          </Routes>
          <Footer />
      </BrowserRouter>
  </React.StrictMode>
);
