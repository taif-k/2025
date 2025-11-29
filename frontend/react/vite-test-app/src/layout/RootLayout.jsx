import { Outlet, NavLink } from 'react-router-dom'

const RootLayout = () => {
    return (
        <div className='container'>
            <div className="row">
                {/* <div className="col-md-3">
                    Navigation
                    <ul>
                        <li><NavLink to='/'>Home</NavLink></li>
                        <li><NavLink to='/profile'>Profile</NavLink></li>
                        <li><NavLink to='/todo' >Todo List</NavLink></li>
                        <li><NavLink to='/usereduce' >useReducer</NavLink></li>
                        <li><NavLink to='/usestate' >useState</NavLink></li>
                        <li><NavLink to='/reactbootstrap' >React Bootstrap</NavLink></li>
                    </ul>
                </div> */}
                <div className="col-md-3">
                    Components
                    <ul>
                        <li><NavLink to='/badges'>Badges</NavLink></li>
                        <li><NavLink to='/breadcrumbs'>Breadcrumbs</NavLink></li>
                        <li><NavLink to='/buttons' >Buttons</NavLink></li>
                        <li><NavLink to='/buttongroups' >ButtonGroup</NavLink></li>
                        <li><NavLink to='/cards' >Card</NavLink></li>
                        <li><NavLink to='/images' >Images</NavLink></li>
                        <li><NavLink to='listgroup'>List Groups</NavLink></li>
                        <li><NavLink to='/figures'>Figures</NavLink></li>
                        <li><NavLink to='/pagination' >Pagination</NavLink></li>
                        <li><NavLink to='/progressbar' >Progress Bars</NavLink></li>
                        <li><NavLink to='/spinner' >Spinners</NavLink></li>
                        <li><NavLink to='/table' >Tables</NavLink></li>
                        <li><NavLink to='/closebutton' >Close Buttons</NavLink></li>
                    </ul>
                </div>
                <div className='col-md-9 border border-1'>
                    <Outlet />
                </div>
            </div>
        </div>
    )
}

export default RootLayout
