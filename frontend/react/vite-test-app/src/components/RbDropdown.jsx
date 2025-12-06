import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';
import { Speedometer2, Bell, Gear, BoxArrowRight } from "react-bootstrap-icons";
import Image from 'react-bootstrap/Image';
import avatarImg from "../assets/images/avatar_img.PNG";
import { Person } from "react-bootstrap-icons";


const RbDropdown = () => {

  return (
    <div className="d-flex gap-5">

      <DropdownButton id="dropdown-basic-1" variant="primary"
        title={<span ><Person />Profile</span>}>

        <Dropdown.Item><Speedometer2 className="me-2" /> Dashboard</Dropdown.Item>
        <Dropdown.Item><Bell className="me-2" /> Notification</Dropdown.Item>
        <Dropdown.Item><Gear className="me-2" /> Settings</Dropdown.Item>
        <Dropdown.Item><BoxArrowRight className="me-2" /> Log out</Dropdown.Item>
      </DropdownButton>


      <DropdownButton id="dropdown-basic-1" variant="outline-primary"
        title={<span ><Person />Profile</span>}>
        <Dropdown.Item><Speedometer2 className="me-2" /> Dashboard</Dropdown.Item>
        <Dropdown.Item><Bell className="me-2" /> Notification</Dropdown.Item>
        <Dropdown.Item><Gear className="me-2" /> Settings</Dropdown.Item>
        <Dropdown.Item><BoxArrowRight className="me-2" /> Log out</Dropdown.Item>
      </DropdownButton>


      <Dropdown align="end">
        <Dropdown.Toggle bsPrefix="dropdown-item">
          <Image src={avatarImg} roundedCircle width={45} height={45} />
        </Dropdown.Toggle>

        <Dropdown.Menu>
          <Dropdown.Item><Speedometer2 className="me-2" /> Dashboard</Dropdown.Item>
          <Dropdown.Item><Bell className="me-2" /> Notification</Dropdown.Item>
          <Dropdown.Item><Gear className="me-2" /> Settings</Dropdown.Item>
          <Dropdown.Item><BoxArrowRight className="me-2" /> Log out</Dropdown.Item>
        </Dropdown.Menu>
      </Dropdown>

    </div>
  );
};

export default RbDropdown;
