import { useState } from "react";
import Accordion from "react-bootstrap/Accordion";
import { AccordionButton, AccordionItem, AccordionBody } from "react-bootstrap";
import { PlusCircle, DashCircle } from "react-bootstrap-icons";

const RbAccordion = () => {
  const [activeKey, setActiveKey] = useState("1");

  const accordionItems = [
    { id: "1", title: "What is the cost of an online course", content: "Lorem ipsum dolor sit amet" },
    { id: "2", title: "Do I need to visit any physical location", content: "Lorem ipsum dolor sit amet" },
    { id: "3", title: "What are the technologies requirements", content: "Lorem ipsum dolor sit amet" },
    { id: "4", title: "How can I ask questions or clear doubts", content: "Lorem ipsum dolor sit amet" }
  ];

  return (
    <Accordion activeKey={activeKey} onSelect={(key) => setActiveKey(key)}>
      <style>{`.accordion-button::after { display: none  }`}</style>

      {accordionItems.map((item) => {
        const isOpen = activeKey === item.id;
        return (
          <AccordionItem key={item.id} eventKey={item.id}>
            <AccordionButton className="d-flex justify-content-between">
              {item.title}  
              {isOpen ? <DashCircle /> : <PlusCircle />}
            </AccordionButton>
            <AccordionBody>{item.content}</AccordionBody>
          </AccordionItem>
        );
      })}
    </Accordion>
  );
};

export default RbAccordion;
