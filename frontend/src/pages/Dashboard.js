import React from 'react';
import { Typography, Container } from '@mui/material';

const Dashboard = () => {
  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Dashboard
      </Typography>
      <Typography paragraph>
        Welcome to your personalized dashboard. Select an option from the menu to get started.
      </Typography>
    </Container>
  );
};

export default Dashboard;
