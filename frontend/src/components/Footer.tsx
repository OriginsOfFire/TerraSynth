import React from 'react';
import {BottomNavigation, BottomNavigationAction} from "@mui/material";
import TelegramIcon from '@mui/icons-material/Telegram';
import GitHubIcon from '@mui/icons-material/GitHub';

function Footer() {
    return (
        <BottomNavigation className={'footer'}
                          sx={{ position: 'fixed', bottom: 0, left: 0, right: 0, backgroundColor: '#d1d1e9' }}>
            <BottomNavigationAction
                href="https://github.com/OriginsOfFire/TerraSynth"
                icon={<GitHubIcon/>}>
            </BottomNavigationAction>
            <BottomNavigationAction
                href="https://t.me/originsOfFire"
                icon={<TelegramIcon/>}>
            </BottomNavigationAction>
        </BottomNavigation>
    );
}

export default Footer;