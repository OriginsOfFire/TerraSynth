import {
  AppBar,
  Button,
  Dialog,
  Divider,
  IconButton,
  List,
  ListItem,
  ListItemText,
  MenuItem,
  Select,
  SelectChangeEvent,
  TextField,
  Toolbar,
  Typography,
} from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';
import React, { ChangeEvent, useEffect, useState } from 'react';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import axios from 'axios';

interface ConfigInfoDialogProps {
  open: boolean;
  handleClose: () => void;
  id: number;
  updateConfigurations: () => void;
}

export const ConfigInfoDialog = ({
  open,
  handleClose,
  id,
  updateConfigurations,
}: ConfigInfoDialogProps) => {
  const [resources, setResources] = useState<string[]>([]);
  const [name, setName] = useState<string>('');
  const [cloud, setCloud] = React.useState<string>('');

  const handleCloudChange = async (e: SelectChangeEvent) => {
    setCloud(e.target.value as string);
  };

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios.get(`http://localhost:8000/api/v1/configurations/${id}`, {
        headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
      });
      setName(response.data.name);
      setCloud(response.data.cloud_type);
    };

    const fetchResourses = async () => {
      const response = await axios.get(
        `http://localhost:8001/api/v1/resources/initialize?configuration_id=${id}`,
        {
          headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
        }
      );
      setResources(response.data);
    };

    fetchData();
    fetchResourses();
  }, [id]);

  const handleSubmit = async (e: React.MouseEvent<HTMLButtonElement>) => {
    const user = JSON.parse(localStorage.getItem('user') as string);
    const token = localStorage.getItem('token');
    const data = {
      user_id: user.data.id,
      name,
      cloud_type: cloud,
    };
    await axios.put(`http://localhost:8000/api/v1/configurations/${id}`, data, {
      headers: { Authorization: `Bearer ${token}` },
    });
    handleClose();
    updateConfigurations();
  };

  // const resources = [
  //   'container_registry azurerm_container_registry',
  //   'key_vault azurerm_key_vault',
  //   'postgres_database azurerm_postgresql_flexible_server',
  //   'resource_group azurerm_resource_group',
  //   'storage_account azurerm_storage_account',
  //   'sa_data_lake azurerm_storage_data_lake_gen2_filesystem',
  // ];

  return (
    <Dialog
      fullScreen
      open={open}
      onClose={handleClose}
      sx={{ width: 2 / 3, margin: 'auto', height: '95vh' }}
    >
      <AppBar sx={{ position: 'relative', backgroundColor: '#844FBA' }}>
        <Toolbar>
          <IconButton edge="start" color="inherit" onClick={handleClose} aria-label="close">
            <CloseIcon />
          </IconButton>
          <Typography sx={{ ml: 2, flex: 1 }} variant="h6" component="div">
            {name}
          </Typography>
          <Button autoFocus color="inherit" onClick={handleSubmit}>
            save
          </Button>
        </Toolbar>
      </AppBar>
      <List sx={{ width: 3 / 4, margin: 'auto', marginTop: 0 }}>
        <ListItem>
          <TextField
            autoFocus
            margin="dense"
            id="name"
            label="Name"
            type="name"
            fullWidth
            variant="standard"
            value={name}
            onChange={(e: ChangeEvent<HTMLInputElement>) => setName(e.target.value)}
          />
        </ListItem>
        <ListItem>
          <Select
            labelId="demo-simple-select-label"
            id="demo-simple-select"
            value={cloud}
            onChange={handleCloudChange}
            displayEmpty
            required
            sx={{
              width: '100%',
            }}
          >
            <MenuItem>Choose provider...</MenuItem>
            <MenuItem value="AWS">Amazon Web Services</MenuItem>
            <MenuItem value="AZURE">Microsoft Azure</MenuItem>
            <MenuItem value="GCP">Google Cloud Platform</MenuItem>
          </Select>
        </ListItem>

        <ListItem>
          <h3> Resources: </h3>
        </ListItem>
        <ListItem>
          {resources.length ? (
            resources.map((r) => {
              return (
                <>
                  {/* <ListItem>
                <ListItemText primary={r.split(' ')[0]} secondary={r.split(' ')[1]} />
                <IconButton>
                  <EditIcon />
                </IconButton>
                <IconButton>
                  <DeleteIcon />
                </IconButton>
              </ListItem>
              <Divider /> */}
                </>
              );
            })
          ) : (
            <div> No resources yet</div>
          )}
        </ListItem>
      </List>
    </Dialog>
  );
};
