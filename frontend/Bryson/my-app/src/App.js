import axios from "axios";
import {Routes, Route, useNavigate} from 'react-router-dom';
import './App.css';

export function App() {
  const navigate = useNavigate();

  const navigateToDashboard = () => {
    navigate('/dashboard');
  };

  const navigateToLogin = () => {
    navigate('/');
  };

  const navigateToEditProfile = () => {
    navigate('/editprofile');
  };
}

export default App;
