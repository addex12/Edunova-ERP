import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { 
  TextField, 
  Button, 
  Container, 
  Typography, 
  Select, 
  MenuItem, 
  FormControl, 
  InputLabel,
  Alert,
  Snackbar,
  CircularProgress
} from '@mui/material';

const RegistrationPage = () => {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    role: 'student',
    admissionNumber: '',
    employeeId: ''
  });
  const [errors, setErrors] = useState({});
  const [snackbar, setSnackbar] = useState({ open: false, message: '', severity: 'error' });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const navigate = useNavigate();

  const validateForm = () => {
    const newErrors = {};
    
    if (!formData.username.trim()) {
      newErrors.username = 'Username is required';
    }
    
    if (!formData.email.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)) {
      newErrors.email = 'Invalid email address';
    }
    
    if (formData.password.length < 8) {
      newErrors.password = 'Password must be at least 8 characters';
    }
    
    if (formData.role === 'student' && !formData.admissionNumber) {
      newErrors.admissionNumber = 'Admission number is required';
    }
    
    if (formData.role === 'teacher' && !formData.employeeId) {
      newErrors.employeeId = 'Employee ID is required';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!validateForm()) return;
    
    setIsSubmitting(true);
    
    try {
      const payload = {
        username: formData.username,
        email: formData.email,
        password: formData.password,
        role: formData.role,
        admission_number: formData.admissionNumber,
        employee_id: formData.employeeId
      };

      const response = await axios.post('http://localhost:5000/api/auth/register', payload, {
        headers: { 'Content-Type': 'application/json' }
      });

      if (response.status === 201) {
        setSnackbar({
          open: true,
          message: 'Registration successful! Redirecting to login...',
          severity: 'success'
        });
        setTimeout(() => navigate('/login'), 2000);
      }
    } catch (error) {
      const backendError = error.response?.data?.error || 'Registration failed';
      const errorField = error.response?.data?.field;

      if (errorField) {
        setErrors({ ...errors, [errorField]: backendError });
      } else {
        setSnackbar({
          open: true,
          message: backendError,
          severity: 'error'
        });
      }
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleCloseSnackbar = () => {
    setSnackbar(prev => ({ ...prev, open: false }));
  };

  const handleInputChange = (field) => (e) => {
    setFormData({ ...formData, [field]: e.target.value });
    if (errors[field]) {
      setErrors({ ...errors, [field]: null });
    }
  };

  return (
    <Container maxWidth="sm" sx={{ mt: 4 }}>
      <Typography variant="h4" gutterBottom component="h1">
        Edunova Registration
      </Typography>
      
      <form onSubmit={handleSubmit}>
        <FormControl fullWidth margin="normal" error={!!errors.role}>
          <InputLabel>Role</InputLabel>
          <Select
            value={formData.role}
            onChange={handleInputChange('role')}
            label="Role"
          >
            <MenuItem value="student">Student</MenuItem>
            <MenuItem value="parent">Parent</MenuItem>
            <MenuItem value="teacher">Teacher</MenuItem>
            <MenuItem value="admin">Admin</MenuItem>
          </Select>
        </FormControl>

        <TextField
          label="Username"
          fullWidth
          margin="normal"
          required
          value={formData.username}
          onChange={handleInputChange('username')}
          error={!!errors.username}
          helperText={errors.username}
        />

        <TextField
          label="Email"
          type="email"
          fullWidth
          margin="normal"
          required
          value={formData.email}
          onChange={handleInputChange('email')}
          error={!!errors.email}
          helperText={errors.email}
        />

        <TextField
          label="Password"
          type="password"
          fullWidth
          margin="normal"
          required
          value={formData.password}
          onChange={handleInputChange('password')}
          error={!!errors.password}
          helperText={errors.password || 'Minimum 8 characters'}
        />

        {formData.role === 'student' && (
          <TextField
            label="Admission Number"
            fullWidth
            margin="normal"
            required
            value={formData.admissionNumber}
            onChange={handleInputChange('admissionNumber')}
            error={!!errors.admissionNumber}
            helperText={errors.admissionNumber}
          />
        )}

        {formData.role === 'teacher' && (
          <TextField
            label="Employee ID"
            fullWidth
            margin="normal"
            required
            value={formData.employeeId}
            onChange={handleInputChange('employeeId')}
            error={!!errors.employeeId}
            helperText={errors.employeeId}
          />
        )}

        <Button 
          type="submit" 
          variant="contained" 
          fullWidth 
          sx={{ mt: 3 }}
          disabled={isSubmitting}
        >
          {isSubmitting ? <CircularProgress size={24} /> : 'Register'}
        </Button>
      </form>

      <Snackbar
        open={snackbar.open}
        autoHideDuration={6000}
        onClose={handleCloseSnackbar}
        anchorOrigin={{ vertical: 'top', horizontal: 'center' }}
      >
        <Alert onClose={handleCloseSnackbar} severity={snackbar.severity} sx={{ width: '100%' }}>
          {snackbar.message}
        </Alert>
      </Snackbar>
    </Container>
  );
};

export default RegistrationPage;
