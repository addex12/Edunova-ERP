import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
import AdminDashboard from './pages/AdminDashboard';
import Dashboard from './pages/Dashboard'; // Add this
import TeacherDashboard from './pages/TeacherDashboard'; // Add this
import ProtectedRoute from './components/ProtectedRoute'; // Add this import
import RegistrationPage from './pages/RegistrationPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegistrationPage />} />
        {/* Other routes */}
      </Routes>
    </Router>
  );
}

export default App;
