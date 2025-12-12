import { TabContainer, TabContent } from 'react-bootstrap';
import Nav from 'react-bootstrap/Nav';
import Tab from 'react-bootstrap/Tab';
import { Calendar, Clock, CurrencyRupee } from "react-bootstrap-icons";

const tabItems = [
  { key: "overview", label: "Overview" },
  { key: "scope", label: "Project Scope" },
  { key: "team", label: "Team Members" },
  { key: "tasks", label: "Tasks" },
  { key: "chat", label: "Chats" },
];

const contentInfo = [
  { icon: <Calendar className="me-2 text-primary" size={16} />, title: "Start Date", value: "01 Jul, 2025" },
  { icon: <Calendar className="me-2 text-primary" size={16} />, title: "End Date", value: "31 Dec, 2025" },
  { icon: <Clock className="me-2 text-primary" size={16} />, title: "Estimated Time", value: "5 months" },
  { icon: <CurrencyRupee className="me-2 text-primary" size={16} />, title: "Estimated Cost", value: "5,80,000" },
];

const RbNavTab = () => {
  return (
    <div className='bg-white p-2'>
      <TabContainer id='left-tab-example' defaultActiveKey="overview">
        <Nav variant="underline"  className="gap-4">
          {tabItems.map((tab) => (
            <Nav.Item key={tab.key}>
              <Nav.Link eventKey={tab.key}>{tab.label}</Nav.Link>
            </Nav.Item>
          ))}
        </Nav>

        <TabContent className='mt-3'>
          {tabItems.map((tab) => (
            <Tab.Pane key={tab.key} eventKey={tab.key}>
              <TabContentUI />
            </Tab.Pane>
          ))}
        </TabContent>

      </TabContainer>
    </div>
  );
};

const TabContentUI = () => (
  <>
    <p className="mb-3">
      Lorem ipsum dolor sit amet consectetur adipisicing elit.
      Lorem ipsum dolor sit amet consectetur adipisicing elit.
      Lorem ipsum dolor sit.
    </p>

    {contentInfo.map((item, index) => (
      <div key={index} className="info-row d-flex align-items-center mt-2 w-100 p-1 fw-semibold">
        {item.icon}
        <p className="d-flex justify-content-between align-items-center w-100 mb-0">
          {item.title}
          <span>{item.value}</span>
        </p>
      </div>
    ))}
  </>
);

export default RbNavTab;
