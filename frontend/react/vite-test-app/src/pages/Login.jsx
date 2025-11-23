import React from 'react'

const Login = () => {
  return (
    <div>
        Enter username and password here
        <div className='row'>
            <div className='col-12 mb-2'>
                Username: <input></input>
            </div>
            <div className='col-12'>
                Password: <input type='password'></input>
            </div>
            <div className='col-12'>
                <Link to='/login' className='btn btn-primary'>Login</Link>
            </div>
        </div>
    </div>
  )
}

export default Login
