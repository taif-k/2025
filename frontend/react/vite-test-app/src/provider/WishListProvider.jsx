import React, { useReducer, useState } from 'react'
import { WishListContext } from '../context/Context'


const WishListProvider = ({ children }) => {

    const WishListReducer = (state, action) => {
        console.log("Current state: " + JSON.stringify(state))
        console.log("Current action: " + JSON.stringify(action))
        const { type, payload } = action
        switch (type) {
            case "ADD_TO_WISHLIST":
                console.log("ADD_TO_WISHLIST: " + JSON.stringify(type))
                return {
                    ...state,
                    wishlistItems: [
                        ...state.wishlistItems,
                        {
                            id: payload?.id,
                            title: payload?.title,
                            thumbnail: payload?.thumbnail
                        }


                    ]
                }
            case "REMOVE_FROM_WISHLIST":
                console.log("REMOVE_FROM_WISHLIST: " + JSON.stringify(type))
                return {
                    ...state,
                    wishlistItems: state.wishlistItems.filter((product => product.id !== payload))
                }
            default:
                return state

        }

    }

    const [wishListState, wishListDispatch] = useReducer(WishListReducer, {
        userId: 1,
        wishlistItems: [],
    })
    return (
        <WishListContext.Provider value={{ wishListState, wishListDispatch }}>
            {children}
        </WishListContext.Provider>
    )
}

export default WishListProvider
