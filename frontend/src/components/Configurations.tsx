import React, {useEffect, useState} from 'react';
import {Navigate, useNavigate} from "react-router-dom";
import axios from "axios";
import {IConfiguration} from "../models/IConfiguration";
import CloudDownloadIcon from '@mui/icons-material/CloudDownload';
import {
    Button,
    Dialog,
    DialogActions,
    DialogContent,
    DialogContentText,
    DialogTitle,
    IconButton, MenuItem, Select, SelectChangeEvent,
    TextField
} from "@mui/material";
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import AddIcon from '@mui/icons-material/Add';

function Configurations() {
    const navigator = useNavigate();
    const [configurations, setConfigurations] = useState<IConfiguration[]>([])
    const [open, setOpen] = useState(false)
    const [cloud, setCloud] = useState("")

    const handleClickOpen = () => {
        setOpen(true);
    }

    const handleClose = () => {
        setOpen(false);
    }

    useEffect(() => {
        const fetchData = async () => {
            const response = await axios.get(
                "http://localhost:8000/api/v1/configurations",
                {headers: {Authorization: `Bearer ${localStorage.getItem("token")}`}}
            );
            setConfigurations(response.data);
        }
        fetchData().catch(() => {
            navigator("/login")
        });
    }, [navigator]);

    const handleDelete = async (e: React.MouseEvent<HTMLButtonElement>) => {
        const configId = +e.currentTarget.id;
        await axios.delete(
            `http://localhost:8000/api/v1/configurations/${configId}`,
            {
                headers: {Authorization: `Bearer ${localStorage.getItem("token")}`},
            }
        )
        const newConfigurations = configurations.filter((n) => n.id !== configId)
        setConfigurations(newConfigurations);
    }

    const handleChange = async (e: SelectChangeEvent) => {
        setCloud(e.target.value as string);
    }
    if (!localStorage.getItem("token")) {
        return <Navigate to="/login"/>;
    } else {
        return (
            <div className="container">
                <h2>Your configurations:</h2>
                <ul>
                    {configurations.map((c: IConfiguration) => {
                        return (
                            <li className="configuration" key={c.id}>
                                <p>{c.name}</p>
                                <IconButton>
                                    <EditIcon/>
                                </IconButton>
                                <IconButton id={c.id.toString()} onClick={handleDelete}>
                                    <DeleteIcon/>
                                </IconButton>
                                <IconButton>
                                    <CloudDownloadIcon/>
                                </IconButton>
                            </li>
                        )
                    })
                    }
                </ul>
                <IconButton>
                    <AddIcon onClick={handleClickOpen}/>
                </IconButton>
                <Dialog open={open} onClose={handleClose}>
                    <DialogTitle>Create Configuration</DialogTitle>
                    <DialogContent>
                        <DialogContentText>
                            To create configuration, please fill the fields below
                        </DialogContentText>
                        <TextField
                            autoFocus
                            margin="dense"
                            id="name"
                            label="Name"
                            type="name"
                            fullWidth
                            variant="standard"
                        />
                        <Select
                            labelId="demo-simple-select-label"
                            id="demo-simple-select"
                            label="Age"
                            value={cloud}
                            onChange={handleChange}
                        >
                            <MenuItem value="AWS">Amazon Web Services</MenuItem>
                            <MenuItem value="AZURE">Microsoft Azure</MenuItem>
                            <MenuItem value="GCP">Google Cloud Platform</MenuItem>
                        </Select>
                    </DialogContent>
                    <DialogActions>
                        <Button onClick={handleClose}>Cancel</Button>
                        <Button onClick={handleClose}>Create</Button>
                    </DialogActions>
                </Dialog>
            </div>
        );
    }
}


export default Configurations;