import Button from 'react-bootstrap/Button';
import { useState } from 'react';
import ToggleButton from 'react-bootstrap/ToggleButton';
import ToggleButtonGroup from 'react-bootstrap/ToggleButtonGroup';


const RbButtons = () => {
  const [value, setValue] = useState([1, 3]);
  const handleChange = (val) => setValue(val);
  
  const getTextStyle = () => ({
    fontWeight: value.includes(1) ? "bold" : "normal",
    fontStyle: value.includes(2) ? "italic" : "normal",
    textDecoration: value.includes(3) ? "line-through" : "none",
  });
  return (
    <>
      <div className='m-3 p-1'>
        <p>Button Styles</p>
        <Button type="submit">Normal Button</Button>
        <Button as="input" type="button" value="Edit" />
        <Button variant="outline-info">Outline Button</Button>
        <Button as="input" type="reset" value="Disabled" disabled />
      </div>
      <div className='m-3 p-1'>
        <p>Button Types</p>
        <Button href="#">Link</Button>
        <Button type="submit">Button</Button>
        <Button as="input" type="button" value="Input" />
        <Button as="input" type="submit" value="Submit" />
        <Button as="input" type="reset" value="Reset" />
      </div>


      <div className='m-3 p-1'>
        <p>Toggle Buttons</p>
        <ToggleButtonGroup type="checkbox" value={value} onChange={handleChange}>
          <ToggleButton id="tbg-btn-1" value={1}>
            Bold
          </ToggleButton>
          <ToggleButton id="tbg-btn-2" value={2}>
            Italic
          </ToggleButton>
          <ToggleButton id="tbg-btn-3" value={3}>
            underline
          </ToggleButton>
        </ToggleButtonGroup>
        <p className='m-2' style={getTextStyle()}>
          {/* <p className='m-2'> */}
          Here, the actions of the above buttons will be reflected
        </p>
      </div>
    </>
  )
}

export default RbButtons
