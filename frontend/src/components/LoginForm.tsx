import React from "react";
import {Box, Button, TextField} from "@mui/material";

function LoginForm() {
    return (
         <Box
          sx={{
            marginTop: 15,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}>
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
                      mt: 3,
                      mb: 2,
                      backgroundColor: "#844FBA" }}
                >
                  Sign In
                </Button>
            </form>
        </Box>
    );
}

export default LoginForm;