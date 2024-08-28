import axios from 'axios';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { useNavigate } from 'react-router';

function NavBar() {
    const navigate=useNavigate()
    function handlelogout(){
       axios.post("http://127.0.0.1:8000/logout").then(res=>{
        if(res){
            navigate("/login")
        }
       })
    }
  return (
    <>
      <Navbar bg="dark" data-bs-theme="dark">
        <Container>
          <Navbar.Brand href="#home">Navbar</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link href="#home">Home</Nav.Link>
            <Nav.Link href="#features">Cart <label>0</label></Nav.Link>
            <Nav.Link onClick={handlelogout} href="">Logout</Nav.Link>
          </Nav>
        </Container>
      </Navbar>
     

     
    </>
  );
}

export default NavBar;