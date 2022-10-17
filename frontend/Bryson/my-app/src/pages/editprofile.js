import React, { Component }  from 'react';
import {useNavigate} from 'react-router-dom';
import '../editprofile.css';

function EditProfilePage() {

    const navigate = useNavigate();
  
    const navigateToDashboard = () => {
    navigate('/dashboard');
    };

    return (
      <html>
        <head>
          <title>
            Profile Page
          </title>
        </head>
        
        <body>
          <div className="App-header">
            <header>
              <p>
                Edit Profile
              </p>
            </header>
          </div>
          <div className='App-body'>
            <form>
              <div>              
                <div>Username</div>              
                <input type="text" placeholder="username"/>  
              </div>
              <div>
                <div>Password</div>                              
                <input type="password" placeholder="password"/>  
              </div>
              <div>
                <div>Account Number</div>                            
                <input type="text" placeholder="ID"/>  
              </div>
              <div>
                <div>Height</div>                              
                <input type="text" placeholder="meters"/>  
              </div>
              <div>
                <div>Age</div>
                <input type="text" placeholder="years"/>  
              </div>
              <div>
                <div>Gender</div>
                <input type="text" placeholder="gender"/>  
              </div>
              <div>
                <div>Weight</div>
                <input type="text" placeholder="pounds"/>  
              </div>
              <div>
                <div>Notepad ID</div>                              
                <input type="text" placeholder="ID"/>  
              </div>
              <div>
                <div>Food objects list</div>                              
                <input type="text" placeholder="list"/>  
              </div>
              <div>
                <div>Exercise flag</div>            
                <input type="text" placeholder="integer"/>  
              </div>
              <div className='submit'>
                <input onClick={navigateToDashboard} type="submit" value="Submit"/>
              </div>
            </form>
          </div>
        </body>
      </html>          
    );
  }
  
  export default EditProfilePage;