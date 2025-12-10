import { useState } from "react";
import Accordion from "react-bootstrap/Accordion";
import { PlusCircle, DashCircle } from "react-bootstrap-icons";

const RbAccordion = () => {
  const [openItem, setOpenItem] = useState(null);

  const items = [
    { id: "1", title: "What is the cost of an online course?" },
    { id: "2", title: "Do I need to visit any physical location?" },
    { id: "3", title: "What are the technology requirements?" },
    { id: "4", title: "How can I ask questions or clear doubts?" },
  ];

  const toggleItem = (id) => {
    setOpenItem(openItem === id ? null : id);
  };

  return (
    <Accordion activeKey={openItem}>
      {items.map((item) => {
        const isOpen = openItem === item.id;

        return (
          <Accordion.Item eventKey={item.id} key={item.id}>

            <div className="d-flex justify-content-between align-items-center p-3" onClick={() => toggleItem(item.id)}>
              {item.title}
              {isOpen ? <DashCircle /> : <PlusCircle />}
            </div>

            <Accordion.Body>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            </Accordion.Body>

          </Accordion.Item>
        );
      })}
    </Accordion>
  );
};

export default RbAccordion;
