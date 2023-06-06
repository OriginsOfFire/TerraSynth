import React from "react";
import {Box, Button, TextField} from "@mui/material";
import axios from "axios";
import {useNavigate} from "react-router-dom";
import {IUser} from "../models/IUser";

function SignUpForm() {
    const navigator = useNavigate();
    return (
        <Box
            sx={{
                marginTop: 15,
                display: 'flex',
                align: 'center',
                flexDirection: 'column',
                alignItems: 'center',
            }}>
            <h3>Fill the following fields to complete your signup:</h3>
            <form>
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
                    id="full_name"
                    label="Full Name"
                    name="full_name"
                    autoComplete="full name"
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
                    autoFocus
                    fullWidth
                />
                <TextField
                    margin="normal"
                    required
                    name="repeat_password"
                    label="Repeat Password"
                    type="password"
                    id="repeat_password"
                    autoComplete="repeat-password"
                    autoFocus
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
                    Sign Up
                </Button>
            </form>
        </Box>
    );
}

export default SignUpForm;