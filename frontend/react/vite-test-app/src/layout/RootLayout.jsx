import { Outlet, NavLink } from 'react-router-dom';
import RbBreadCrumb from '../components/RbBreadCrumbs';
import Accordion from 'react-bootstrap/Accordion';
import Button from 'react-bootstrap/Button';
import { ArrowRight, Columns } from "react-bootstrap-icons";
import { Container, Row, Col, Badge } from 'react-bootstrap';
import { useContext } from 'react';
import { UserContext, WishListContext } from '../context/Context';


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

const forms = [
  { path: "/rhform", label: "RH Form" },
  { path: "/rhformyup", label: "RH Form Yup" }
];


const management = [
  { path: "/statemanagement", label: "State Management" },
  { path: "/product", label: "Product" },
  { path: "/wishlist", label: "Wish List" }
]

const blogaccordion = [
  { path: "/blog", label: "Blogs" },
  // { path: "/blog/:id", label: "Blog Detail" }
]

const RootLayout = () => {

  const { name } = useContext(UserContext)
  const { wishListState } = useContext(WishListContext)


  return (
    <Container>
      <Row>
        <Col className="p-3 border-end" md={3}>
          <Button variant="primary" className="mb-2">
            Bootstrap Components
          </Button>

          <Accordion defaultActiveKey="4">
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

            <Accordion.Item eventKey="2">
              <Accordion.Header>Forms</Accordion.Header>
              <Accordion.Body>
                <ul className="list-unstyled">
                  {forms.map((item, index) => (
                    <li key={index} className="sidebar-link">
                      <ArrowRight className="me-2 icon-blue" />
                      <NavLink to={item.path}>{item.label}</NavLink>
                    </li>
                  ))}
                </ul>
              </Accordion.Body>
            </Accordion.Item>

            <Accordion.Item eventKey="3">
              <Accordion.Header>Context Api</Accordion.Header>
              <Accordion.Body>
                <ul className="list-unstyled">
                  {management.map((item, index) => (
                    <li key={index} className="sidebar-link">
                      <ArrowRight className="me-2 icon-blue" />
                      <NavLink to={item.path}>{item.label}</NavLink>
                    </li>
                  ))}
                </ul>
              </Accordion.Body>
            </Accordion.Item>

            <Accordion.Item eventKey="4">
              <Accordion.Header>Blogs</Accordion.Header>
              <Accordion.Body>
                <ul className="list-unstyled">
                  {blogaccordion.map((item, index) => (
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
          <NavLink to="/wishlist" variant='outline-primary' className='btn'>Wishlist<Badge className='m-2'>{wishListState.wishlistItems.length}</Badge></NavLink>
          <Outlet />
        </Col>
      </Row>
    </Container>
  );
};

export default RootLayout;
