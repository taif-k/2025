import { Outlet,NavLink } from 'react-router-dom'

const RootLayout = () => {
  return (
    <div className='container'>
        <div className="row">
            <div className="col-md-3">
                Navigation
                <ul>
                    <li><NavLink to='/'>Home</NavLink></li>
                    <li><NavLink to='/profile'>Profile</NavLink></li>
                    <li><NavLink to='/todo' >Todo List</NavLink></li>
                    <li><NavLink to='/usereduce' >useReducer</NavLink></li>
                    <li><NavLink to='/usestate' >useState</NavLink></li>
                    <li><NavLink to='/reactbootstrap' >React Bootstrap</NavLink></li>
                </ul>
            </div>
            <div className='col-md-9 border border-1'>
                <Outlet/>
            </div>
        </div>
    </div>
  )
}

export default RootLayout
