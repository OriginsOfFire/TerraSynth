import {
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle,
  MenuItem,
  Select,
  SelectChangeEvent,
  TextField,
} from '@mui/material';
import { useState } from 'react';
import axios from 'axios';
import { IConfiguration } from '../models/IConfiguration';

interface CreateConfigDialogProps {
  open: boolean;
  handleClose: () => void;
  updateConfigurations: (value: IConfiguration) => void;
}

export const CreateConfigDialog = ({
  open,
  handleClose,
  updateConfigurations,
}: CreateConfigDialogProps) => {
  const [cloud, setCloud] = useState<string | undefined>();
  const [name, setName] = useState('');

  const handleCloudChange = async (e: SelectChangeEvent) => {
    setCloud(e.target.value as string);
  };

  const handleNameChange = async (e: React.ChangeEvent<HTMLTextAreaElement | HTMLInputElement>) => {
    setName(e.currentTarget.value);
    console.log(e.currentTarget.value);
  };

  const handleSubmit = async (e: React.MouseEvent<HTMLButtonElement>) => {
    const user = JSON.parse(localStorage.getItem('user') as string);
    const token = localStorage.getItem('token');
    const data = {
      user_id: user.data.id,
      name,
      cloud_type: cloud,
    };
    const response = await axios.post('http://localhost:8000/api/v1/configurations/', data, {
      headers: { Authorization: `Bearer ${token}` },
    });
    updateConfigurations(response.data);
    handleClose();
  };

  return (
    <Dialog
      open={open}
      onClose={handleClose}
      sx={{
        minWidth: 500,
        maxWidth: 500,
        m: 'auto',
      }}
    >
      <DialogTitle>Create Configuration</DialogTitle>
      <DialogContent>
        <DialogContentText>To create configuration, please fill the fields below</DialogContentText>
        <TextField
          autoFocus
          margin="dense"
          id="name"
          label="Name"
          type="name"
          fullWidth
          variant="standard"
          onChange={handleNameChange}
          required
          sx={{
            width: '100%',
          }}
        />
        <Select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          value={cloud}
          onChange={handleCloudChange}
          displayEmpty
          required
          sx={{
            mt: 3,
            width: '100%',
          }}
        >
          <MenuItem>Choose provider...</MenuItem>
          <MenuItem value="AWS">Amazon Web Services</MenuItem>
          <MenuItem value="AZURE">Microsoft Azure</MenuItem>
          <MenuItem value="GCP">Google Cloud Platform</MenuItem>
        </Select>
      </DialogContent>
      <DialogActions>
        <Button onClick={handleClose}>Cancel</Button>
        <Button onClick={handleSubmit}>Create</Button>
      </DialogActions>
    </Dialog>
  );
};
