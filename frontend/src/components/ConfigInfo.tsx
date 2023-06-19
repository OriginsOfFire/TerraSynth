import {
    AppBar,
    Button,
    Dialog,
    Divider,
    IconButton,
    List,
    ListItem,
    ListItemText, MenuItem, Select, SelectChangeEvent, TextField,
    Toolbar,
    Typography
} from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';
import React from 'react';
import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete";

const ConfigInfo = () => {
    const [open, setOpen] = React.useState(false);
    const [cloud, setCloud] = React.useState("")

    const handleClickOpen = () => {
        setOpen(true);
    };

    const handleClose = () => {
        setOpen(false);
    };
    const handleChange = async (e: SelectChangeEvent) => {
        setCloud(e.target.value as string);
    }
    const resources = [
        "container_registry azurerm_container_registry",
        "key_vault azurerm_key_vault",
        "postgres_database azurerm_postgresql_flexible_server",
        "resource_group azurerm_resource_group",
        "storage_account azurerm_storage_account",
        "sa_data_lake azurerm_storage_data_lake_gen2_filesystem",
    ]

    return (
        <div>
            <Button variant="outlined" onClick={handleClickOpen}>
                Open full-screen dialog
            </Button>
            <Dialog
                fullScreen
                open={open}
                onClose={handleClose}
                /*TransitionComponent={Transition}*/
            >
                <AppBar sx={{ position: 'relative', backgroundColor: "#844FBA" }}>
                    <Toolbar>
                        <IconButton
                            edge="start"
                            color="inherit"
                            onClick={handleClose}
                            aria-label="close"
                        >
                            <CloseIcon />
                        </IconButton>
                        <Typography sx={{ ml: 2, flex: 1 }} variant="h6" component="div">
                            Azure Test
                        </Typography>
                        <Button autoFocus color="inherit" onClick={handleClose}>
                            save
                        </Button>
                    </Toolbar>
                </AppBar>
                <List>
                    <ListItem>
                        <TextField
                            autoFocus
                            margin="dense"
                            id="name"
                            label="Name"
                            type="name"
                            fullWidth
                            variant="standard"
                        />
                        </ListItem>
                    <ListItem>
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
                    </ListItem>
                    {resources.map( (r )=> {
                        return (<>
                        <ListItem>
                            <ListItemText primary={r.split(' ')[0]} secondary={r.split(' ')[1]} />
                            <IconButton>
                                <EditIcon/>
                            </IconButton>
                            <IconButton>
                                <DeleteIcon/>
                            </IconButton>
                        </ListItem>
                        <Divider />
                        </>)
                    })}
                </List>
            </Dialog>
        </div>);
};

export default ConfigInfo;