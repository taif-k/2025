import { useState } from 'react';
import Button from 'react-bootstrap/Button';
import ButtonGroup from 'react-bootstrap/ButtonGroup';
import ButtonToolbar from 'react-bootstrap/ButtonToolbar';

const RbButtonGroup = () => {
  const [align, setAlign] = useState("right")
  const getTextDirection = () => {
    return {
      textAlign: align,
    }
  }
  return (
    <>
        <ButtonGroup aria-label="Basic example">
          <Button variant="secondary d-flex align-items-center" onClick={() => setAlign("left")}>Left</Button>
          <Button variant="secondary d-flex align-items-center" onClick={() => setAlign("center")}>Center</Button>
          <Button variant="secondary d-flex align-items-center" onClick={() => setAlign("right")}>Right</Button>
        </ButtonGroup>
        <p className='mt-2' style={getTextDirection()}>
          Here, the actions of the above buttons will be reflected
        </p>
      
    </>
  )
}

export default RbButtonGroup
