import { Outlet } from 'react-router-dom'

const AuthLayout = () => {
  return (
    <div className='container'>
        <div className='row'>
            <div className='col-12'>
                AuthLayout
                <Outlet/>
            </div>
        </div>
      
    </div>
  )
}

export default AuthLayout
