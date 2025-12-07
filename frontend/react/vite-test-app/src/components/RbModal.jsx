import { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import Form from 'react-bootstrap/Form';

const RbModal = () => {
  const [show, setShow] = useState(false);
  const [email, setEmail] = useState('');

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  const handleSubscribe = () => {
    if (email) {
      alert(`Subscribed with: ${email}`);
      setEmail('');
      handleClose();
    } else {
      alert('Please enter a valid email.');
    }
  };

  return (
    <>
      <Button variant="primary" onClick={handleShow}>
        Subscribe
      </Button>

      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Don't Miss Out</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <p>Signup for our newsletter to stay up to date.</p>
          <div className="d-flex">
            <Form.Control
              type="email"
              placeholder="Enter your email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
            <Button 
              variant="primary" 
              onClick={handleSubscribe} 
              className="ms-2"
            >
              Subscribe
            </Button>
          </div>
        </Modal.Body>
      </Modal>
    </>
  );
};

export default RbModal;
