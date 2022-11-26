import React, { Component }  from 'react';
import {useNavigate} from 'react-router-dom';
import '../login.css';

function LoginPage() {

  //Variables values changes when user inputs into fields
  //Variable initial values ('') should be from user's database
  const [userName, setUserName] = React.useState('');
  const [password, setPassword] = React.useState('');

  function handleSubmit() {
    //Add code here to save values in variables into database
    //preventDefault();
    navigateToDashboard();
  }

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
          <div><input type="text" id="userName" name="userName" value={userName} placeholder="username" onChange={(e) => setUserName(e.target.value)}/></div>
          <div><input type="password" id="password" value={password} name="password" placeholder="password" onChange={(e) => setPassword(e.target.value)}/>
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