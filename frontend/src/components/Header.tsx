import LogoutIcon from '@mui/icons-material/Logout';
import { IconButton } from '@mui/material';
import { NavLink, useNavigate } from 'react-router-dom';

function Header() {
  const navigate = useNavigate();
  const handleLogout = () => {
    if (localStorage.getItem('token')) {
      localStorage.clear();
      navigate('/login');
    }
  };
  return (
    <header className="start">
      <NavLink
        to="providers"
        className={({ isActive, isPending }) =>
          isPending ? 'link' : isActive ? 'link-active' : 'link'
        }
      >
        Providers
      </NavLink>
      <NavLink
        to="configurations"
        className={({ isActive, isPending }) =>
          isPending ? 'link' : isActive ? 'link-active' : 'link'
        }
      >
        Configurations
      </NavLink>
      <NavLink
        to="profile"
        className={({ isActive, isPending }) =>
          isPending ? 'link' : isActive ? 'link-active' : 'link'
        }
      >
        Profile
      </NavLink>
      <IconButton sx={{ position: 'absolute', right: 100 }}>
        <LogoutIcon onClick={handleLogout} />
      </IconButton>
    </header>
  );
}

export default Header;
