import React, { Fragment, useContext } from 'react'
import { Row, Col } from 'react-bootstrap';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import { ProductsData } from '../data/product';
import WishList from './WishList';
import { WishListContext } from '../context/Context';

const Products = ({item}) => {
    const { wishListState, wishListDispatch } = useContext(WishListContext)
  
  const AddToWishListBtn = () => {
    const handleAddToWishList = () =>{
      wishListDispatch({type: "ADD_WISHLIST", payload: item})
    }


    return (
      <Button variant="primary" size='sm' onClick={handleAddToWishList}>Wish List</Button>
    )
  }
  return (
    <Fragment>
      <h3>List of Products</h3>
      <Row>
        {ProductsData.map((item, index) => {
          return (
            <Col key={index} md={4} className='p-2'>
              <Card>
                <Card.Img variant="top" src={item.thumbnail} />
                <Card.Body>
                  <Card.Title>{item.title}</Card.Title>
                  <Card.Text>{item.description}</Card.Text>
                </Card.Body>
                <Card.Footer className='d-flex justify-content-between'>
                  <Button variant="primary">Cart</Button>
                  <AddToWishListBtn product = {item}/>
                </Card.Footer>
              </Card>
            </Col>
          )
        })}


      </Row>
    </Fragment>
  )
}

export default Products
