import React, { useReducer } from 'react'

const CountWithReducer = () => {
    const reducer = (state, action) => {
        switch (action.type) {
            case "INCREMENT":
                return state < 20 ? state + 1 : state;
            case "DECREMENT":
                return state > 0 ? state - 1 : state;
            default:
                return state;
        }

    }
    const [state, dispatch] = useReducer(reducer, 0)
    const actions = [
        { type: "INCREMENT" },
        { type: "DECREMENT" }
    ];
    return (
        <div>
            Count Value = {state}
            <br />

            {actions.map(action => (
                <button
                    className="btn btn-outline-primary"
                    onClick={() => dispatch({ type: action.type })}
                >{action.type}
                </button>
                
            ))}

            {state === 20 && <p>Maximum limit reached.</p>}
            {state === 0 && <p>Minimum limit reached.</p>}
        </div> 
    )
}


export default CountWithReducer
