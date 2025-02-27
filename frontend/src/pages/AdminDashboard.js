import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Container, Typography, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Button, TextField, Dialog, DialogTitle, DialogContent, DialogActions } from '@mui/material';

const AdminDashboard = () => {
    const [users, setUsers] = useState([]);
    const [features, setFeatures] = useState([]);
    const [openFeatureDialog, setOpenFeatureDialog] = useState(false);
    const [newFeature, setNewFeature] = useState({ name: '', description: '' });

    useEffect(() => {
        fetchDashboardData();
    }, []);

    const fetchDashboardData = async () => {
        try {
            const response = await axios.get('http://localhost:5000/api/admin/dashboard', {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`
                }
            });
            setUsers(response.data.users);
            setFeatures(response.data.features);
        } catch (error) {
            console.error('Error fetching dashboard data:', error);
        }
    };

    const handleAddFeature = async () => {
        try {
            await axios.post('http://localhost:5000/api/admin/features', newFeature, {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`
                }
            });
            setOpenFeatureDialog(false);
            fetchDashboardData(); // Refresh data
        } catch (error) {
            console.error('Error adding feature:', error);
        }
    };

    return (
        <Container>
            <Typography variant="h4" gutterBottom>Admin Dashboard</Typography>

            {/* Users Table */}
            <Typography variant="h6" gutterBottom>Users</Typography>
            <TableContainer component={Paper}>
                <Table>
                    <TableHead>
                        <TableRow>
                            <TableCell>Username</TableCell>
                            <TableCell>Email</TableCell>
                            <TableCell>Role</TableCell>
                            <TableCell>Created At</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {users.map((user) => (
                            <TableRow key={user.id}>
                                <TableCell>{user.username}</TableCell>
                                <TableCell>{user.email}</TableCell>
                                <TableCell>{user.role}</TableCell>
                                <TableCell>{new Date(user.created_at).toLocaleDateString()}</TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>

            {/* Features Table */}
            <Typography variant="h6" gutterBottom sx={{ mt: 4 }}>Features</Typography>
            <Button variant="contained" onClick={() => setOpenFeatureDialog(true)}>
                Add New Feature
            </Button>
            <TableContainer component={Paper} sx={{ mt: 2 }}>
                <Table>
                    <TableHead>
                        <TableRow>
                            <TableCell>Name</TableCell>
                            <TableCell>Description</TableCell>
                            <TableCell>Status</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {features.map((feature) => (
                            <TableRow key={feature.id}>
                                <TableCell>{feature.name}</TableCell>
                                <TableCell>{feature.description}</TableCell>
                                <TableCell>{feature.is_active ? 'Active' : 'Inactive'}</TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>

            {/* Add Feature Dialog */}
            <Dialog open={openFeatureDialog} onClose={() => setOpenFeatureDialog(false)}>
                <DialogTitle>Add New Feature</DialogTitle>
                <DialogContent>
                    <TextField
                        label="Feature Name"
                        fullWidth
                        margin="normal"
                        value={newFeature.name}
                        onChange={(e) => setNewFeature({ ...newFeature, name: e.target.value })}
                    />
                    <TextField
                        label="Description"
                        fullWidth
                        margin="normal"
                        value={newFeature.description}
                        onChange={(e) => setNewFeature({ ...newFeature, description: e.target.value })}
                    />
                </DialogContent>
                <DialogActions>
                    <Button onClick={() => setOpenFeatureDialog(false)}>Cancel</Button>
                    <Button onClick={handleAddFeature}>Add</Button>
                </DialogActions>
            </Dialog>
        </Container>
    );
};

export default AdminDashboard;
