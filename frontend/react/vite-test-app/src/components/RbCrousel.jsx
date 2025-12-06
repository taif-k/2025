import { useRef, useState } from "react";
import Carousel from "react-bootstrap/Carousel";
import Button from "react-bootstrap/Button";

const RbCarousel = () => {
  const [sliderIndex, setSliderIndex] = useState(0);
  const carouselRef = useRef();

  const slides = [
    {
      id: 1,
      src: "https://wowslider.com/sliders/demo-44/data1/images/bridge.jpg",
      title: "First slide label",
      description: "Sample description here."
    },
    {
      id: 2,
      src: "https://wowslider.com/sliders/demo-44/data1/images/bridge.jpg",
      title: "Second slide label",
      description: "Sample description here."
    },
    {
      id: 3,
      src: "https://wowslider.com/sliders/demo-18/data1/images/hongkong1081704.jpg",
      title: "Third slide label",
      description: "Sample description here."
    }
  ];

  return (
    <>
      <Carousel
        ref={carouselRef}
        activeIndex={sliderIndex}
        onSelect={(selectedIndex) => setSliderIndex(selectedIndex)}
        indicators={false} 
      >
        {slides.map((slide) => (
          <Carousel.Item key={slide.id}>
            <img className="d-block w-100" src={slide.src} alt={`Slide ${slide.id}`} />          
            <Carousel.Caption>
              <h3>{slide.title}</h3>
              <p>{slide.description}</p>
            </Carousel.Caption>
          </Carousel.Item>
        ))}
      </Carousel>

      
      <div className="d-flex justify-content-center gap-2 mt-2">
        {slides.map((slide, index) => (
          <div
            key={index}
            className={`dot ${sliderIndex === index ? "active-dot" : ""}`}
            onClick={() => {
              setSliderIndex(index);
              carouselRef.current?.to(index);
            }}
          />
        ))}
      </div>

      <div className="custom-slide-buttons">
        <Button variant="primary" onClick={() => carouselRef.current?.prev()}>
          Prev
        </Button>

        <Button variant="primary" onClick={() => carouselRef.current?.next()}>
          Next
        </Button>
      </div>
    </>
  );
};

export default RbCarousel;
