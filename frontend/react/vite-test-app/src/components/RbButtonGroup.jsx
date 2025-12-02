import { useState } from 'react';
import Button from 'react-bootstrap/Button';
import ButtonGroup from 'react-bootstrap/ButtonGroup';

const RbButtonGroup = () => {
  const [align, setAlign] = useState("center");

  const buttonOptions = [
    { label: "Left", value: "left" },
    { label: "Center", value: "center" },
    { label: "Right", value: "right" }
  ];

  return (
    <>
      <ButtonGroup aria-label="Alignment Buttons">
        {buttonOptions.map((btn, index) => (
          <Button
            key={index}
            variant="secondary d-flex align-items-center"
            onClick={() => setAlign(btn.value)}
          >
            {btn.label}
          </Button>
        ))}
      </ButtonGroup>

      <div className="w-100">
        <p className="mt-2" style={{ textAlign: align }}>
          Sample Text
        </p>
      </div>
    </>
  );
};

export default RbButtonGroup;
