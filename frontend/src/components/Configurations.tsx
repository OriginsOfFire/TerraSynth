import React, { useCallback, useEffect, useState } from 'react';
import { Navigate, useNavigate } from 'react-router-dom';
import axios from 'axios';
import { IConfiguration } from '../models/IConfiguration';
import CloudDownloadIcon from '@mui/icons-material/CloudDownload';
import {
  Avatar,
  Button,
  IconButton,
  List,
  ListItem,
  ListItemAvatar,
  ListItemText,
} from '@mui/material';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
// import SourceOutlinedIcon from '@mui/icons-material/SourceOutlined';
import SourceOutlinedIcon from '@mui/icons-material/SourceTwoTone';
import AddIcon from '@mui/icons-material/Add';
import { CreateConfigDialog } from './CreateConfigDialog';
import { ConfigInfoDialog } from './ConfigInfoDialog';

function Configurations() {
  const navigator = useNavigate();
  const [configurations, setConfigurations] = useState<IConfiguration[]>([]);
  const [open, setOpen] = useState(false);
  const [selectedId, setSelectedId] = useState<null | number>(null);

  const updateConfigurations = useCallback(async () => {
    const response = await axios.get('http://localhost:8000/api/v1/configurations', {
      headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
    });
    setConfigurations(response.data);
  }, []);

  useEffect(() => {
    updateConfigurations();
  }, [navigator, updateConfigurations]);

  const handleDelete = async (e: React.MouseEvent<HTMLButtonElement>) => {
    const configId = +e.currentTarget.id;
    await axios.delete(`http://localhost:8000/api/v1/configurations/${configId}`, {
      headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
    });
    const newConfigurations = configurations.filter((n) => n.id !== configId);
    setConfigurations(newConfigurations);
  };

  const handleDownload = async (e: React.MouseEvent<HTMLButtonElement>) => {
    const configId = +e.currentTarget.id;
    await axios.get(`http://localhost:8001/api/v1/resources/generate/${configId}`);
  };

  if (!localStorage.getItem('token')) {
    return <Navigate to="/login" />;
  } else {
    return (
      <div className="config-container">
        <h2>Your configurations:</h2>
        <List sx={{ width: '100%' }}>
          {configurations.map((c: IConfiguration) => {
            return (
              <ListItem
                className="configuration"
                key={c.id}
                sx={{
                  backgroundColor: 'rgba(233, 222, 245, 0.4);',
                  borderRadius: 1,
                  mt: 1,
                }}
                secondaryAction={
                  <>
                    <IconButton
                      onClick={() => {
                        setSelectedId(c.id);
                      }}
                    >
                      <EditIcon />
                    </IconButton>
                    <IconButton id={c.id.toString()} onClick={handleDelete}>
                      <DeleteIcon />
                    </IconButton>
                    <IconButton id={c.id.toString()} onClick={handleDownload}>
                      <CloudDownloadIcon />
                    </IconButton>
                  </>
                }
              >
                <ListItemAvatar>
                  <Avatar sx={{ backgroundColor: 'rgba(233, 222, 245)' }}>
                    <SourceOutlinedIcon sx={{ color: 'black' }} />
                  </Avatar>
                </ListItemAvatar>

                <ListItemText primary={c.name} />
              </ListItem>
            );
          })}
        </List>

        <Button
          variant="contained"
          sx={{
            ':hover': { backgroundColor: '#a46ed9' },
            backgroundColor: '#8a4fc4',
          }}
          endIcon={<AddIcon />}
          onClick={() => setOpen(true)}
        >
          Add Configuration
        </Button>

        <CreateConfigDialog
          open={open}
          handleClose={() => setOpen(false)}
          updateConfigurations={updateConfigurations}
        />
        {!!selectedId && (
          <ConfigInfoDialog
            open={!!selectedId}
            handleClose={() => setSelectedId(null)}
            id={selectedId}
            updateConfigurations={updateConfigurations}
          />
        )}
      </div>
    );
  }
}

export default Configurations;
