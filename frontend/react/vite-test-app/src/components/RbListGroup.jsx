import ListGroup from 'react-bootstrap/ListGroup';
import Card from 'react-bootstrap/Card';
import { Facebook, Instagram, Linkedin, TwitterX, Youtube } from 'react-bootstrap-icons'
import CardBody from 'react-bootstrap/esm/CardBody';

const RbListGroup = () => {
    const Socials = [{
        id: 1,
        social: "Facebook",
        traffic: "20%",
        icon: <Facebook className='me-1' color='#1877F2' />
    },
    {
        id: 2,
        social: "Instagram",
        traffic: "20%",
        icon: <Instagram className='me-1' color='#1877F2' />
    },
    {
        id: 3,
        social: "Youtube",
        traffic: "20%",
        icon: <Youtube className='me-1' color='#1877F2' />
    },
    {
        id: 4,
        social: "Twitter X",
        traffic: "20%",
        icon: <TwitterX className='me-1' color='#1877F2' />
    },
    {
        id: 5,
        social: "Linkedin",
        traffic: "20%",
        icon: <Linkedin className='me-1' color='#1877F2' />
    }]

    return (
        Socials.map((s) => (
            <Card key={s.id} >
                <CardBody>
                    <ListGroup variant='flush'>
                        <ListGroup.Item className='d-flex align-items-center justify-content-between'>
                            <div>
                                {s.icon}
                                {s.social}
                            </div>
                            <span>
                                {s.traffic}
                            </span>
                        </ListGroup.Item>
                    </ListGroup>
                </CardBody>
            </Card >

        ))

    )
}
export default RbListGroup
