import React from 'react';
import LogoutIcon from '@mui/icons-material/Logout';
import {IconButton} from "@mui/material";


function Header() {
    const handleLogout = () => {
        if (localStorage.getItem("token")) {
            localStorage.clear();
        }
    }
    return (
        <header className='start'>
            <a href="/providers">Providers</a>
            <a href="/configurations">Configurations</a>
            <a href="/me">Me</a>
            <IconButton sx={{paddingLeft: "50px"}}>
                <LogoutIcon onClick={handleLogout}/>
            </IconButton>
        </header>
    );
}

export default Header;