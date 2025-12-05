import { Outlet, NavLink } from 'react-router-dom';
import RbBreadCrumb from '../components/RbBreadCrumbs';
import Accordion from 'react-bootstrap/Accordion';
import Button from 'react-bootstrap/Button';
import { ArrowRight, Columns } from "react-bootstrap-icons";
import { Container, Row, Col } from 'react-bootstrap';



const nonInteractiveLinks = [
  { path: "/badges", label: "Badges" },
  { path: "/breadcrumb", label: "Breadcrumbs" },
  { path: "/buttons", label: "Buttons" },
  { path: "/buttongroups", label: "ButtonGroup" },
  { path: "/cards", label: "Card" },
  { path: "/images", label: "Images" },
  { path: "/listgroup", label: "List Groups" },
  { path: "/figures", label: "Figures" },
  { path: "/pagination", label: "Pagination" },
  { path: "/progressbar", label: "Progress Bars" },
  { path: "/spinner", label: "Spinners" },
  { path: "/table", label: "Tables" },
  { path: "/closebutton", label: "Close Buttons" }
];

const interactiveLinks = [
  { path: "/accordion", label: "Accordion" },
  { path: "/crousel", label: "Crousel" },
  { path: "/dropdown", label: "Dropdown" },
  { path: "/modal", label: "Modal" },
  { path: "/navbar-offcanvas", label: "Navbar Offcanvas" },
  { path: "/navtab", label: "Navtab" },
  { path: "/overlay", label: "Overlay" }
];

const RootLayout = () => {
  return (

    <Container>
      <Row>
        <Col className="p-3 border-end" md={3}>
          <Button variant="primary" className="mb-2">
            Bootstrap Components
          </Button>

          <Accordion defaultActiveKey="0">
            <Accordion.Item eventKey="0">
              <Accordion.Header>Non Interactive</Accordion.Header>
              <Accordion.Body>
                <ul className="list-unstyled">
                  {nonInteractiveLinks.map((item, index) => (
                    <li key={index} className="sidebar-link">
                      <ArrowRight className="me-2 icon-blue" />
                      <NavLink to={item.path}>{item.label}</NavLink>
                    </li>
                  ))}
                </ul>
              </Accordion.Body>
            </Accordion.Item>


            <Accordion.Item eventKey="1">
              <Accordion.Header>Interactive</Accordion.Header>
              <Accordion.Body>
                <ul className="list-unstyled">
                  {interactiveLinks.map((item, index) => (
                    <li key={index} className="sidebar-link">
                      <ArrowRight className="me-2 icon-blue" />
                      <NavLink to={item.path}>{item.label}</NavLink>
                    </li>
                  ))}
                </ul>
              </Accordion.Body>
            </Accordion.Item>
          </Accordion>
        </Col>

        <Col md={9}>
          <RbBreadCrumb />
          <Outlet />
        </Col>
      </Row>
    </Container>
  );
};

export default RootLayout;
