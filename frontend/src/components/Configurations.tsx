import React, {useEffect, useState} from 'react';
import {Navigate, useNavigate} from "react-router-dom";
import axios from "axios";
import {IConfiguration} from "../models/IConfiguration";

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
    useEffect(() => {
        const fetchData = async () => {
            const response = await axios.get(
                "http://localhost:8000/api/v1/configuration",
                {headers: {Authorization: `Bearer ${localStorage.getItem("token")}`}}
            );
            setConfigurations(response.data);
        }

        fetchData().catch(() => {navigator("/login")});
    }, []);

    if (!localStorage.getItem("token")) {
        return <Navigate to="/login" />;
    } else {
        return (
            <>
                <h3>Your configurations:</h3>
                <li>
                    {configurations.map((c: IConfiguration) => {
                    console.log(c.id);
                    return <ul key={c.id}>{c.id}</ul>
                })}
                </li>
            </>
        );
    }
}

export default Configurations;