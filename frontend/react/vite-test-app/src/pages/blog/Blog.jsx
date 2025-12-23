import React from 'react'
import { Row, Col, Card } from 'react-bootstrap'
import { ProductsData } from '../../data/product'
import { NavLink } from 'react-router-dom'

const Blog = () => {
  return (
    <div>
      <Row>
        {ProductsData.map((item,index)=>{
          return (
            <Col key={index} md={4}>
              <Card>
                <Card.Img src={item.thumbnail}></Card.Img>
                <Card.Body>
                  <h6>{item.title}</h6>
                  <NavLink to={`/blog/${item.id}`}>Read More</NavLink>
                </Card.Body>
              </Card>
            </Col>
          )
        })}
      </Row>
      
    </div>
  )
}

export default Blog
