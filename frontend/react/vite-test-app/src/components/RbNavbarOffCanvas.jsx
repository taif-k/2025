import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import Modal from 'react-bootstrap/Modal';
import { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Offcanvas from 'react-bootstrap/Offcanvas';
import { NavLink } from 'react-router-dom';
import { Globe, Envelope, Telephone } from "react-bootstrap-icons";

const RbNavbarOffCanvas = () => {

  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);


  return (
    <div className='d-flex gap-5' style={{ height: "4.5rem" }}>
      <Navbar expand="lg" className="bg-body-tertiary">
        <Container>
          <Navbar bg="dark" data-bs-theme="dark">
            <Container>
              <Navbar.Brand href="#home" >RB</Navbar.Brand>
            </Container>
          </Navbar>

          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link href="#home">Home</Nav.Link>
              <Nav.Link href="#link">Services</Nav.Link>
              <NavDropdown title="Company" id="basic-nav-dropdown">
                <NavDropdown.Item href="#action/3.1">About us</NavDropdown.Item>
                <NavDropdown.Item href="#action/3.2">
                  Our Team
                </NavDropdown.Item>
                <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item href="#action/3.4">
                  Infrastructure
                </NavDropdown.Item>
              </NavDropdown>
            </Nav>

            <Nav className='p-5 d-flex gap-2'>
              <NavLink><Button>Login</Button></NavLink>
              <NavLink><Button variant='outline-primary'>Sign-up</Button></NavLink>
              <NavLink><Button variant='outline-dark' className='bg-dark text-white' onClick={handleShow}>Contact</Button></NavLink>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>


      <Offcanvas show={show} onHide={handleClose} placement="end">
        <Offcanvas.Header closeButton>
          <Offcanvas.Title>Contact Us</Offcanvas.Title>
        </Offcanvas.Header>

        <Offcanvas.Body >
          <h3 className='info-row fw-semibold'>We’re here to help you!</h3>

          <h4 className="mb-5 fw-semibold">Indixpert</h4>

          <div className="mt-3 contact-section">
            <h6>Our Office</h6>
            <p className="d-flex align-items-center mb-3">
              <Globe className="me-2" />
              1. Address 1
            </p>

            <h6>Email</h6>
            <p className="d-flex align-items-center mb-3">
              <Envelope className="me-2" />
              Sample Email
            </p>
            <h6>Phone</h6>
            <p className="d-flex align-items-center mb-3">
              <Telephone className="me-2" />
              Sample Phone
            </p>
          </div>
        </Offcanvas.Body>
      </Offcanvas>
    </div>
  )
}

export default RbNavbarOffCanvas
