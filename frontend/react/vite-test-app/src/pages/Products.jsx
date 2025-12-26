import { Fragment, useContext } from "react";
import { Row, Col } from "react-bootstrap";
import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";
import { ProductsData } from "../data/product";
import { WishListContext, CartListContext } from "../context/Context";

const Products = () => {
  const { wishListState, wishListDispatch } = useContext(WishListContext);
  const { cartListState, cartListDispatch } = useContext(CartListContext);

  const AddToWishListBtn = ({ product }) => {
    const itemPresent = wishListState.wishlistItems.some(
      (item) => item.id === product.id
    );

    const handleAddToWishList = () => {
      if (itemPresent) {
        alert("Already present in Wish List");
      } else {
        wishListDispatch({
          type: "ADD_TO_WISHLIST",
          payload: product
        });
        alert("Item added to Wish List");
      }
    };

    return (
      <Button
        variant="primary"
        size="sm"
        onClick={handleAddToWishList}
      >
        Wish List
      </Button>
    );
  };


  const handleAddToCart = (product) => {
    cartListDispatch({
      type: "ADD_TO_CART",
      payload: {
        id: product.id,
        name: product.title,
        price: product.price
      }
    });
  };

  return (
    <Fragment>
      <h3 className="mb-3">List of Products</h3>

      <Row>
        {ProductsData.map((item) => {
          const isInCart = cartListState.cartItems.some(
            (cartItem) => cartItem.id === item.id
          );

          return (
            <Col key={item.id} md={4} className="p-2">
              <Card>
                <Card.Img
                  variant="top"
                  src={item.thumbnail}
                  height="200"
                  style={{ objectFit: "cover" }}
                />

                <Card.Body>
                  <Card.Title>{item.title}</Card.Title>
                  <Card.Text>{item.description}</Card.Text>
                  <strong>₹{item.price}</strong>
                </Card.Body>

                <Card.Footer className="d-flex justify-content-between">
                  <Button size="sm" disabled={isInCart}
                    onClick={() => handleAddToCart(item)}>
                    {isInCart ? "Added" : "Add to Cart"}
                  </Button>

                  <AddToWishListBtn product={item} />
                </Card.Footer>
              </Card>
            </Col>
          );
        })}
      </Row>
    </Fragment>
  );
};

export default Products;
