import React, { Fragment, useContext } from 'react'
import { Row, Col } from 'react-bootstrap';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import { ProductsData } from '../data/product';
import WishList from './WishList';
import { WishListContext } from '../context/Context';

const Products = () => {
  const { wishListState, wishListDispatch } = useContext(WishListContext)

  const AddToWishListBtn = ({ product }) => {
    const itemPresent = wishListState.wishlistItems.filter((item)=>item.id === product.id).length > 0 ? true : false
    const handleAddToWishList = () => {
      if(itemPresent){
        alert('Already present in Wish List')
      }  else{
          wishListDispatch({ type: "ADD_TO_WISHLIST", payload: product })
      alert('Item added to Wish List')
      }
      
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
                  <AddToWishListBtn product={item} />
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
