import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { IProvider } from '../models/IProvider';

const Providers = () => {
  const [providers, setProviders] = useState([]);
  const navigator = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios.get('http://localhost:8000/api/v1/providers', {
        headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
      });
      setProviders(response.data);
    };
    fetchData().catch(() => {
      navigator('/login');
    });
  }, [navigator]);

  return (
    <div>
      <h3>Available Providers:</h3>
      <ul>
        {providers.map((p: IProvider) => {
          return (
            <li key={p.name}>
              <p>{p.name}</p>
              <p>{p.abbreviation}</p>
            </li>
          );
        })}
      </ul>
    </div>
  );
};

export default Providers;
