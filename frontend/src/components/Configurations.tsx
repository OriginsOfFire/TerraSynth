import React, {useEffect, useState} from 'react';
import {Navigate, useNavigate} from "react-router-dom";
import axios from "axios";
import {IConfiguration} from "../models/IConfiguration";
import {Checkbox, IconButton} from "@mui/material";
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import AddIcon from '@mui/icons-material/Add';

function Configurations() {
    // const [authenticated, setAuthenticated] = useState(false);
    // useEffect(() => {
    //    const token = localStorage.getItem("token");
    //    if (token) {
    //        setAuthenticated(true);
    //    }
    // }, []);
    const navigator = useNavigate();
    const [configurations, setConfigurations] = useState([])
    const [checked, setChecked] = useState([])

    useEffect(() => {
        const fetchData = async () => {
            const response = await axios.get(
                "http://localhost:8000/api/v1/configuration",
                {headers: {Authorization: `Bearer ${localStorage.getItem("token")}`}}
            );
            setConfigurations(response.data);
        }
        fetchData().catch(() => {navigator("/login")});
    }, [navigator]);

    if (!localStorage.getItem("token")) {
        return <Navigate to="/login" />;
    } else {
        return (
            <>
                <div className="container">
                    <h3>Your configurations:</h3>
                    <ul>
                        {configurations.map((c: IConfiguration) => {
                            return (
                                <li key={c.id}>
                                    <p>{c.name}</p>
                                    <Checkbox/>
                                    <IconButton>
                                        <EditIcon/>
                                    </IconButton>
                                    <IconButton onClick={() => console.log(c.name)}>
                                        <DeleteIcon/>
                                    </IconButton>
                                </li>
                            )
                        })
                    }
                    </ul>
                    <IconButton>
                        <AddIcon/>
                    </IconButton>
                </div>
            </>
        );
    }
}

export default Configurations;