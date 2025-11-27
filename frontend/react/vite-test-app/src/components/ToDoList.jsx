import { useReducer, useState } from "react";

function todoReducer(state, action) {
  switch (action.type) {

    case "REMOVE_ITEM":
      return state.filter((item) => item.id !== action.payload);

    case "ADD_ITEM":
      return [...state,{id: Date.now(),text: action.payload,completed: false}];

    case "COMPLETED_ITEM":
      return state.map((item) =>
        item.id === action.payload? { ...item, completed: !item.completed }: item);

    default:
      return state;
  }
}

const ToDoList = () => {
  const [todos, dispatch] = useReducer(todoReducer, []);
  const [input, setInput] = useState("");

  const handleAdd = () => {
    (input.trim() === "") ? true :  dispatch({ type: "ADD_ITEM", payload: input }); setInput("");
  };

  return (
    <div className="card" style={{ width: "30rem" }}>
      <div className="card-body">
        <h5 className="card-title">ToDo List</h5>

        
        <div className="input-group mb-3">
          <input
            type="text"
            className="form-control"
            placeholder="Enter List Item Names"
            value={input}
            onChange={(e) => setInput(e.target.value)}
          />
          <button
            className="btn btn-outline-secondary"
            type="button"
            onClick={handleAdd}
          >
            Add Todo Items
          </button>
        </div>

        
        <ul className="list-group list-group-flush">
          {todos.map((item) => (
            <li
              key={item.id}
              className="list-group-item"
              onClick={() =>
                dispatch({ type: "COMPLETED_ITEM", payload: item.id })
              }
              style={{
                textDecoration: item.completed ? "line-through" : "none",
                cursor: "pointer",
              }}
            >
              {/* <img src="https://img.icons8.com/?size=32&id=cL95UuXTO0nU&format=png"width={15}alt="icon"/> */}
              {" "}
              {item.text}
              <button
                className="btn btn-outline-secondary btn-remove"
                type="button"
                onClick={(e) => {
                  e.stopPropagation(); 
                  dispatch({ type: "REMOVE_ITEM", payload: item.id });
                }}
              >
                Remove
              </button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default ToDoList;
