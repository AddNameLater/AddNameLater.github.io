import React, { Component }  from 'react';
import {useNavigate} from 'react-router-dom';
import '../login.css';

function LoginPage() {



    const navigate = useNavigate();
  
    const navigateToDashboard = () => {
      navigate('/dashboard');
    };

    const navigateToCreateAccount = () => {
      navigate('/createaccount');
    };

  return (
    <div className="main">
      <div className="sub-main">
        <div>
          <h1>Diet Tracker</h1>
          <h1> Login Page</h1>
          <div><input type="text" placeholder="email" className="email"/></div>
          <div><input type="password" placeholder="password" className="password"/>
          </div>
          <div><button onClick={navigateToDashboard}>Login</button></div>
          <div>
          </div>
          <div><button onClick={navigateToCreateAccount}>Create Account</button></div>
        </div>
      </div>
    </div>

  );
}

export default LoginPage;