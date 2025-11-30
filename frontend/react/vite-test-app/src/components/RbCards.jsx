import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup';
import Button from 'react-bootstrap/Button';

const RbCards = () => {
  const headphones = [
    {
      id: 1,
      name: "Bluetooth Headphones",
      description: "simple text 1 ",
      price: "1399",
      mrp: "3990",
    },
    {
      id: 2,
      name: "The Ear Gaming Headphones",
      description: "simple text 2",
      price: "1399",
      mrp: "3990",
    },
  ]


  return (
    headphones.map((headphone) => (
      <Card style={{ width: '18rem' }}>
        <Card.Title className='mt-2 ps-2'>{headphone.name}</Card.Title>
        <Card.Img variant="top" src="holder.js/100px180?text=Image cap" />
        <Card.Body>
          <Card.Text>
            {headphone.description}
          </Card.Text>
          <p>{headphone.price}<span className='ms-2 text-decoration-line-through'>{headphone.mrp}</span></p>
        </Card.Body>
        <Card.Footer className='d-flex justify-content-between'>
          <Button variant='outline-primary' size='sm'>Add to Cart</Button>
          <Button variant='primary' size='sm'>Buy Know</Button>
        </Card.Footer>
      </Card>
    ))

  )
}

export default RbCards
