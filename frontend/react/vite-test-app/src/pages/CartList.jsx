import { useContext } from "react";
import { CartListContext } from "../context/Context";
import { Button, Image } from 'react-bootstrap'
const CartList = () => {
    const { cartListState, cartListDispatch } = useContext(CartListContext);

    const totalPrice = cartListState.cartItems.reduce(
        (total, item) => total + item.price * item.qty,
        0
    );

    if (cartListState.cartItems.length === 0) {
        return <h5>Your cart is empty</h5>;
    }

    return (
        <div>
            <h4>My Cart</h4>

            {cartListState.cartItems.map(item => (
                <div key={item.id}>
                    <Image src={item.thumbnail}></Image>
                    <h6>{item.name}</h6>
                    <p>Price: ₹{item.price}</p>
                    
                    <Button size="sm" variant="secondary"
                        onClick={() =>
                            cartListDispatch({ type: "DECREASE_QTY", payload: item.id })}>
                                -
                    </Button>
                    <span className="m-2">{item.qty}</span>
                    <Button className="m-1"  size="sm" variant="secondary"
                        onClick={() =>
                            cartListDispatch({ type: "INCREASE_QTY", payload: item.id })}>
                        +
                    </Button>

                    <Button className="m-1"
                        onClick={() => cartListDispatch({ type: "REMOVE_FROM_CART", payload: item.id })}>
                        Remove
                    </Button>
                </div>
            ))}

            <h5>Total Price: ₹{totalPrice}</h5>
        </div>
    );
};

export default CartList;
