import React from 'react'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import logo from './logo.svg';
import './App.css';
import Login from './pages/Login';

function App() {
    return (
        <Router>
            <Switch>
                <Route path="/login" component={Login} />
                {/* Add other routes for Register, Dashboard, etc. */}
            </Switch>
        </Router>
    );
}

export default App;
