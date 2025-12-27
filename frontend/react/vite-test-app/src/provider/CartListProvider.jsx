import React, { useReducer } from "react";
import { CartListContext } from "../context/Context";

const CartListReducer = (state, action) => {
  switch (action.type) {

    case "ADD_TO_CART": {
      const itemExists = state.cartItems.find(
        item => item.id === action.payload.id
      );

      if (itemExists) {
        return {
          ...state,
          cartItems: state.cartItems.map(item =>
            item.id === action.payload.id
              ? { ...item, qty: item.qty + 1 }
              : item
          )
        };
      }

      return {
        ...state,
        cartItems: [...state.cartItems, { ...action.payload, qty: 1 }]
      };
    }

    case "INCREASE_QTY":
      return {
        ...state,
        cartItems: state.cartItems.map(item =>
          item.id === action.payload
            ? { ...item, qty: item.qty + 1 }
            : item
        )
      };

    case "DECREASE_QTY":
      return {
        ...state,
        cartItems: state.cartItems
          .map(item =>
            item.id === action.payload
              ? { ...item, qty: item.qty - 1 }
              : item
          )
          .filter(item => item.qty > 0)
      };

    case "REMOVE_FROM_CART":
      return {
        ...state,
        cartItems: state.cartItems.filter(item => item.id !== action.payload)
      };

    default:
      return state;
  }
};

const CartListProvider = ({ children }) => {
  const [cartListState, cartListDispatch] = useReducer(CartListReducer, {
    userId: 1,
    cartItems: []
  });

  return (
    <CartListContext.Provider value={{ cartListState, cartListDispatch }}>
      {children}
    </CartListContext.Provider>
  );
};

export default CartListProvider;
