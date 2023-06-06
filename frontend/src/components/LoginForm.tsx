import React from "react";
import {Box, Button, TextField} from "@mui/material";
import axios from "axios";
import {useNavigate} from "react-router-dom";
import {IUser} from "../models/IUser";

function LoginForm() {
    const navigator = useNavigate();
    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        const data = new FormData(event.currentTarget);
        const token = await axios.post('http://localhost:8000/api/v1/token/', {
            'username': data.get('email'),
            'password': data.get('password')
        },{
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        })
        localStorage.setItem('token', token.data.access_token)
        const user: IUser = await axios.get(
            "http://localhost:8000/api/v1/user/me",
            {headers: {Authorization: `Bearer ${localStorage.getItem("token")}`}}
        )
        localStorage.setItem("user", JSON.stringify(user));
        navigator("/configurations")
    };

    return (
         <Box
          sx={{
            marginTop: 15,
            display: 'flex',
            align: 'center',
            flexDirection: 'column',
            alignItems: 'center',
          }}>
            <h2>Welcome! Please authorize</h2>
            <form onSubmit={handleSubmit}>
                <TextField
                  margin="normal"
                  required
                  id="email"
                  label="Email Address"
                  name="email"
                  autoComplete="email"
                  autoFocus
                  fullWidth
                />
                <TextField
                  margin="normal"
                  required
                  name="password"
                  label="Password"
                  type="password"
                  id="password"
                  autoComplete="current-password"
                  fullWidth
                />
                <Button
                  type="submit"
                  fullWidth
                  variant="contained"
                  sx={{
                      ":hover": {backgroundColor: "#844FBA"},
                      mt: 3,
                      mb: 2,
                      backgroundColor: "#844FBA"
                }}
                >
                  Sign In
                </Button>
            </form>
             <a href="/signup">Don't have an account? Sign up</a>
        </Box>
    );
}

export default LoginForm;