import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup';
import Button from 'react-bootstrap/Button';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';


const RbCards = () => {
  const headphones = [
    {
      id: 1,
      name: "Bluetooth Headphones",
      description: "Boult Newly flex on ear bluetooth headphones, C type fast charging Boult Newly flex on ear bluetooth headphones, C type fast charging",
      price: "1399",
      mrp: "3990",
      img: "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    {
      id: 2,
      name: "The Ear Gaming Headphones",
      description: "Boult Newly flex on ear bluetooth headphones, C type fast charging Boult Newly flex on ear bluetooth headphones, C type fast charging",
      price: "1399",
      mrp: "3990",
      img: "https://media.istockphoto.com/id/835148968/photo/red-headphones-isolated.jpg?s=612x612&w=0&k=20&c=JAEd1MYVaJjC0Iu1cZ4LPHRigRGZ-NJNjIXXs87me1E="
    },
  ]


return (
  <Row className="g-3">
    {headphones.map((headphone) => (
      <Col key={headphone.id} md={6} lg={4}>
        <Card style={{ width: '100%' }}>
          <Card.Title className='mt-2 ps-2'>{headphone.name}</Card.Title>
          <Card.Img variant="top" src={headphone.img} />
          <Card.Body>
            <Card.Text>{headphone.description}</Card.Text>
            <p>
              {headphone.price}
              <span className='ms-2 text-decoration-line-through'>
                MRP {headphone.mrp}
              </span>
            </p>
          </Card.Body>
          <Card.Footer className='d-flex justify-content-between'>
            <Button variant='outline-primary' size='sm'>Add to Cart</Button>
            <Button variant='primary' size='sm'>Buy Now</Button>
          </Card.Footer>
        </Card>
      </Col>
    ))}
  </Row>
);
}

export default RbCards
