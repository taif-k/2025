import { Outlet } from 'react-router-dom'

const RootLayout = () => {
  return (
    <div className='container'>
        <div className="row">
            <div className="col-md-3">
                Navigation
                <ul>
                    <li><a href='/'>Home</a></li>
                    <li><a href='/profile'>Profile</a></li>
                    <li><a href='/todo' >Todo List</a></li>
                    <li><a href='/usereduce' >useReducer</a></li>
                    <li><a href='/usestate' >useState</a></li>
                </ul>
            </div>
            <div className='col-md-9 border border-1'>
                Component
                <Outlet/>
            </div>
        </div>
    </div>
  )
}

export default RootLayout
