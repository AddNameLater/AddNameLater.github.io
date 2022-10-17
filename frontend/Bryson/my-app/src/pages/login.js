import React, { Component }  from 'react';
import {useNavigate} from 'react-router-dom';
import '../login.css';

function LoginPage() {

    const navigate = useNavigate();
  
    const navigateToDashboard = () => {
      navigate('/dashboard');
    };

  return (
    <div className="main">
      <div className="sub-main">
        <div>
          <h1>Diet Tracker</h1>
          <h1> Login Page</h1>
          <div><input type="text" placeholder="user name" className="name"/></div>
          <div><input type="text" placeholder="password" className="pass"/>
          </div>
          <div><button onClick={navigateToDashboard}>Login</button></div>
          <div>
          </div>
          <button>Forgot Password</button>
          <button>Create Account</button>
        </div>
      </div>
    </div>

  );
}

export default LoginPage;