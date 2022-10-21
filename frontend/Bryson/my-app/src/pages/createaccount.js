import React, { Component }  from 'react';
import {useNavigate} from 'react-router-dom';
import '../createaccount.css';

function CreateAccountPage() {


    const navigate = useNavigate();
  
    const navigateToDashboard = () => {
      navigate('/dashboard');
    };

    const navigateToLogin = () => {
        navigate('/login');
      };

  return (
    <div className="main">
      <div className="sub-main">
        <div>
          <h1>Create Account</h1>
          <div><input type="text" placeholder="first name" className="first name"/>
          <input type="text" placeholder="last name" className="last name"/>
          </div>
          <div>
          <input type="text" placeholder="email" className="email"/>
          </div>
          <div>
          <input type="password" placeholder="password" className="passwrod"/>
          </div>
          <div><button onClick={navigateToLogin}>Create Account</button></div>
        </div>
      </div>
    </div>

  );
}

export default CreateAccountPage;