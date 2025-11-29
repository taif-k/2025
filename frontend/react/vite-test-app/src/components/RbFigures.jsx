import Figure from 'react-bootstrap/Figure';

const RbFigures = () => {
    return (
        <Figure>
            <Figure.Image
                width={171}
                height={180}
                alt="171x180"
                src="holder.js/171x180"
            />
            <Figure.Caption>
                This is a simple text
            </Figure.Caption>
        </Figure>
    )
}

export default RbFigures
