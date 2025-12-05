import ListGroup from 'react-bootstrap/ListGroup';
import Card from 'react-bootstrap/Card';
import { Facebook, Instagram, Linkedin, TwitterX, Youtube } from 'react-bootstrap-icons';

const RbListGroup = () => {
    const Socials = [
        { id: 1, social: "Facebook", traffic: "20%", icon: <Facebook className='me-1' color='#1877F2' /> },
        { id: 2, social: "Instagram", traffic: "20%", icon: <Instagram className='me-1' color='#1877F2' /> },
        { id: 3, social: "Youtube", traffic: "20%", icon: <Youtube className='me-1' color='#1877F2' /> },
        { id: 4, social: "Twitter X", traffic: "20%", icon: <TwitterX className='me-1' color='#1877F2' /> },
        { id: 5, social: "Linkedin", traffic: "20%", icon: <Linkedin className='me-1' color='#1877F2' /> }
    ];

    return (
        <Card className="border-1">
            <p className='fw-semibold d-flex'>Social Media Traffic</p>
            <ListGroup variant='flush'>
                {Socials.map((s) => (
                    <ListGroup.Item key={s.id} className="d-flex align-items-center justify-content-between py-2 px-3">
                        <div className="d-flex align-items-center">
                            {s.icon}
                            <span className="ms-2">{s.social}</span>
                        </div>
                        <span className="ms-5">{s.traffic}</span>
                    </ListGroup.Item>
                ))}
            </ListGroup>
        </Card>
    );
};

export default RbListGroup;
