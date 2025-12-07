import Figure from 'react-bootstrap/Figure';
import figureimage from '../assets/images/fig.PNG'

const RbFigures = () => {
    return (
        <Figure>
            <Figure.Image fluid
                width={171}
                height={180}
                alt="171x180"
                src={figureimage}
            />
            <Figure.Caption>
                Image Resource: Google.com
            </Figure.Caption>
        </Figure>
    )
}

export default RbFigures
