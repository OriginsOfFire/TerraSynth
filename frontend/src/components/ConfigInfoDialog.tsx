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
  Stack,
  TextField,
  Toolbar,
  Typography,
} from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';
import React, { ChangeEvent, useEffect, useState } from 'react';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import axios from 'axios';
import { IResource } from '../models/IResource';
import AddIcon from '@mui/icons-material/Add';

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
  const [resources, setResources] = useState<IResource[]>([]);
  const [name, setName] = useState<string>('');
  const [cloud, setCloud] = React.useState<string>('');
  const [providerId, setProviderId] = useState<number | undefined>();
  const [availableResourses, setAvailableResourses] = useState<IResource[]>([]);

  console.log(providerId, availableResourses);

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
      setProviderId(response.data.provider_id);
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

  useEffect(() => {
    const fetchAvailableResourses = async () => {
      const response = await axios.get(
        `http://localhost:8001/api/v1/resources/?provider_id=${providerId}}`,
        {
          headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
        }
      );
      setAvailableResourses(response.data);
    };

    providerId && fetchAvailableResourses();
  }, [providerId]);

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
      <Stack sx={{ width: '90%', margin: 'auto', marginTop: 3 }} gap={3}>
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
        <Stack gap={2} alignItems={'flex-start'}>
          <h3> Resources: </h3>

          {resources.length ? (
            <List sx={{ width: '100%' }}>
              {resources.map((res: IResource) => {
                return (
                  <ListItem
                    className="configuration"
                    key={res.name}
                    sx={{
                      backgroundColor: 'rgba(233, 222, 245, 0.4);',
                      borderRadius: 1,
                      mt: 1,
                    }}
                    secondaryAction={
                      <>
                        <IconButton>
                          <EditIcon />
                        </IconButton>
                        <IconButton>
                          <DeleteIcon />
                        </IconButton>
                      </>
                    }
                  >
                    <ListItemText primary={res.name} secondary={res.data_type} />
                  </ListItem>
                );
              })}
            </List>
          ) : (
            <div> No resources yet</div>
          )}
          <Button
            variant="contained"
            sx={{
              ':hover': { backgroundColor: '#a46ed9' },
              backgroundColor: '#8a4fc4',
            }}
            endIcon={<AddIcon />}
          >
            Add Resource
          </Button>
        </Stack>
      </Stack>
    </Dialog>
  );
};
