import { useState } from "react";
import CloseButton from "react-bootstrap/CloseButton";

const RbCloseButton = () => {
  const [isShown, setIsVisible] = useState(true);
  let closeBtn = () => setIsVisible(false)

  return (
    <>
      {isShown && (
        <div data-bs-theme="dark" className='bg-dark p-2 d-flex align-items-center gap-2'>
          <span className="text-white">Close This Button</span>
          <CloseButton onClick={closeBtn} />
        </div>
      )}
    </>
  );
};

export default RbCloseButton;
