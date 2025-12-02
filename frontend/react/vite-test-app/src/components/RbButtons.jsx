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

  const normalButtons = [
    { type: "submit", children: "Normal Button" },
    { type: "button", as: "input", value: "Edit" },
    { variant: "outline-info", children: "Outline Button" },
    { type: "reset", as: "input", value: "Disabled", disabled: true }
  ];

  const typeButtons = [
    { children: "Link", href: "#" },
    { type: "submit", children: "Button" },
    { type: "button", as: "input", value: "Input" },
    { type: "submit", as: "input", value: "Submit" },
    { type: "reset", as: "input", value: "Reset" }
  ];

  const toggleButtons = [
    { id: "tbg-btn-1", value: 1, label: "Bold" },
    { id: "tbg-btn-2", value: 2, label: "Italic" },
    { id: "tbg-btn-3", value: 3, label: "Underline" },
  ];

  return (
    <>
      <div className='m-3 p-1'>
        <p>Button Styles</p>
        {normalButtons.map((btn, i) => (
          <Button key={i} {...btn}>
            {btn.children}
          </Button>
        ))}
      </div>

      <div className='m-3 p-1'>
        <p>Button Types</p>
        {typeButtons.map((btn, i) => (
          <Button key={i} {...btn}>
            {btn.children}
          </Button>
        ))}
      </div>

      <div className='m-3 p-1'>
        <p>Toggle Buttons</p>
        <ToggleButtonGroup type="checkbox" value={value} onChange={handleChange}>
          {toggleButtons.map((btn, i) => (
            <ToggleButton key={i} id={btn.id} value={btn.value}>
              {btn.label}
            </ToggleButton>
          ))}
        </ToggleButtonGroup>

        <p className='m-2' style={getTextStyle()}>
          Here, the actions of the above buttons will be reflected
        </p>
      </div>
    </>
  );
};

export default RbButtons;
