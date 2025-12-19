import React, { useReducer, useState } from 'react'
import { WishListContext } from '../context/Context'


const WishListProvider = ({ children }) => {

    const WishListReducer = (state, action) => {
        console.log("Current state: " + JSON.stringify(state))
        console.log("Current action: " + JSON.stringify(action))
    }

    const [wishListState, wishListDispatch] = useReducer(WishListReducer, {
        userId: 1,
        wishlistItems: [{
            "id": 1,
            "title": "Essence Mascara Lash Princess",
            "description": "The Essence Mascara Lash Princess is a popular mascara known for its volumizing and lengthening effects. Achieve dramatic lashes with this long-lasting and cruelty-free formula.",
        }, {
            "id": 2,
            "title": "Eyeshadow Palette with Mirror",
            "description": "The Eyeshadow Palette with Mirror offers a versatile range of eyeshadow shades for creating stunning eye looks. With a built-in mirror, it's convenient for on-the-go makeup application.",

        }],
    })
    return (
        <WishListContext.Provider value={{ wishListState, wishListDispatch }}>
            {children}
        </WishListContext.Provider>
    )
}

export default WishListProvider
