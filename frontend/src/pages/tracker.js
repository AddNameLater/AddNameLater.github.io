import React, { Component }  from 'react';
import {useNavigate} from 'react-router-dom';
import '../tracker.css';

function TrackerPage() {

    const navigate = useNavigate();
  
    const navigateToDashboard = () => {
    navigate('/dashboard');
    };

    return (
      <html>
        <head>
          <title>
            Tracker Page
          </title>
        </head>
        
        <body>
          <div className="App-header">
            <header>
              <p>
                Tracker
              </p>
            </header>
          </div>
          <div className='App-body'>
            <form>
              <div>              
                <div>Daily Caloric Intake</div>              
                <input type="text" placeholder="calories"/>  
              </div>
              <div>
                <div>
                <input type="text" placeholder=""/>
                </div>
              </div>
              <div>Manual input</div>
              <div className='box'>
                <div className='box-child'>
                    <input type="text" placeholder="calories"/>
                    <input type="text" placeholder="protein"/>  
                </div>
                <div className='box-child'>
                    <input type="text" placeholder="carbs"/>
                    <input type="text" placeholder="fat"/>  
                </div> 
              </div>
              <div className='button-group'>
                <div className='button'>
                    <input type="button" value="Enter"/>
                </div>
                <div className='button'>
                    <input onClick={navigateToDashboard} type="button" value="Save"/>
                    <input type="button" value="Load"/>
                </div>
                <div className='button'>
                    <input type="button" value="Barcode"/>
                </div>
              </div> 
            </form>
          </div>
        </body>
      </html>          
    );
  }
  
  export default TrackerPage;