import { useState } from 'react';
import ProgressBar from 'react-bootstrap/ProgressBar';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Badge from 'react-bootstrap/Badge';


const RbProgressBar = () => {
    const [value, setValue] = useState(0)
    const handleIncrease = () => setValue(value + 5)
    const handleDecrease = () => setValue(value - 5)

    return (
        <>
            <div className="text-start w-100">
                <Button onClick={handleIncrease} className='me-2'>Progress 5+</Button>
                <Button onClick={handleDecrease}>Progress 5-</Button>

                <p className='fw-bold mt-2 pt-2'>Completed {value}%</p>

                <ProgressBar now={value} label={`${value}%`} striped animated variant='success' className="mb-2" />
                <ProgressBar now={value} striped variant='danger' />
            </div>

            <Card style={{ width: '18rem' }} className='m-3'>
                <Card.Body className="text-start">
                    <Card.Title>Bootstrap Dashboard Application</Card.Title>
                    <Card.Subtitle className="mb-2 text-muted">Web Development</Card.Subtitle>
                    <Card.Text>
                        Some quick example text to build on the card title
                    </Card.Text>
                    <Badge bg='info'>In Progress</Badge>
                    <ProgressBar label='5%' className="my-2" />


                    <div className="d-flex gap-3 mt-2">
                        <Card.Text>Due Date: 1 Jan, 2022</Card.Text>
                        <Card.Text>Budget: $123,000</Card.Text>
                    </div>
                </Card.Body>
            </Card>


        </>
    )
}

export default RbProgressBar
