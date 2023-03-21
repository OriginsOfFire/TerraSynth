import React, {useEffect, useState} from 'react';
import './App.css';
import axios from "axios";
import {Button, Grid, Link} from "@mui/material";
import Footer from "./components/Footer";
import LoginForm from "./components/LoginForm";
import Header from "./components/Header";

function App() {
    //const [users, setUsers] = useState([]);

    // useEffect(() => {
    //     axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
    //     axios.get('http://0.0.0.0:8000/api/v1/user')
    //         .then(res => {
    //             const users = res.data;
    //             console.log(users);
    //             setUsers(users);
    //         })
    //     console.log(users);
    // })

  return (
    <div className="App">
      <Header/>
      <LoginForm/>
      <Footer/>
    </div>
  );
}

export default App;
