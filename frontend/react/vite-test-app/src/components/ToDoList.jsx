import React from 'react'

const ToDoList = () => {
    return (
        <div className="card" style={{ 'width': '30rem' }}>
            <div className="card-body">
                <h5 className="card-title">ToDo List</h5>
                <div class="input-group mb-3">
                    <input type="text" className="form-control" placeholder="Enter List Item Names" aria-label="List Item Names " aria-describedby="button-addon2" />
                    <button className="btn btn-outline-secondary" type="button" id="button-addon2">Add Todo Items</button>
                </div>
                <ul className="list-group list-group-flush">
                    <li className="list-group-item">
                        <img src='https://img.icons8.com/?size=32&id=cL95UuXTO0nU&format=png' width={15} />Learn HTML, CSS & JS
                        <button className="btn btn-outline-secondary btn-remove" type="button" id="button-addon2">Remove</button></li>
                    <li className="list-group-item">
                        <img src='https://img.icons8.com/?size=60&id=78597&format=png' width={15} />Learn React
                        <button className="btn btn-outline-secondary btn-remove" type="button" id="button-addon2">Remove</button></li>
                    <li className="list-group-item">
                        <img src='https://img.icons8.com/?size=60&id=78597&format=png' width={15} />Create Projects
                        <button className="btn btn-outline-secondary btn-remove" type="button" id="button-addon2">Remove</button></li>
                    <li className="list-group-item">
                        <img src='https://img.icons8.com/?size=60&id=78597&format=png' width={15} />Upload on Github
                        <button className="btn btn-outline-secondary btn-remove" type="button" id="button-addon2">Remove</button></li>
                    <li className="list-group-item">
                        <img src='https://img.icons8.com/?size=60&id=78597&format=png' width={15} />Create Portfolio
                        <button className="btn btn-outline-secondary btn-remove" type="button" id="button-addon2">Remove</button></li>
                    <li className="list-group-item">
                        <img src='https://img.icons8.com/?size=60&id=78597&format=png' width={15} />Create Resume
                        <button className="btn btn-outline-secondary btn-remove" type="button" id="button-addon2">Remove</button></li>
                    <li className="list-group-item">
                        <img src='https://img.icons8.com/?size=60&id=78597&format=png' width={15} />Apply For a Job
                        <button className="btn btn-outline-secondary btn-remove" type="button" id="button-addon2">Remove</button></li>
                </ul>
            </div>
        </div>
    )
}

export default ToDoList
