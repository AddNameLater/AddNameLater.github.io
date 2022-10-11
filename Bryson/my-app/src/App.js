import Button from 'react-bootstrap/Button';
import ButtonGroup from 'react-bootstrap/ButtonGroup';
import './App.css';

function DashboardPage() {
  return (
    <>
      <div
        style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center"
      }}>
        <h1 class="header1">Dashboard</h1>
      </div>
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center"
        }}>
      <ButtonGroup className="buttonRow1">
        <a href="https://google.com">
        <Button className="button1" style={{ width: "300px", height: "300px",}}>Tracker</Button>
        </a>
        <a href="https://youtube.com">
        <Button className="button2" style={{ width: "300px", height: "300px",}}>Notepad</Button>
        </a>
      </ButtonGroup>
      </div>
      <br />
      <div
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center"
      }}>
      <ButtonGroup className="buttonRow2">
      <a href="https://youtube.com">
        <Button className="button1" style={{ width: "300px", height: "300px",}}>Edit Profile</Button>
      </a>
      <a href="https://google.com">
        <Button className="button2" style={{ width: "300px", height: "300px",}}>Logout</Button>
      </a>
      </ButtonGroup>
      <br />
      </div>
    </>
  );
}

export default DashboardPage;
