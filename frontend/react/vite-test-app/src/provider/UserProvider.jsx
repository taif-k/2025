import React, { useState } from 'react'
import { UserContext } from '../context/Context'


const UserProvider = ({children}) => {
    const [name, setName] = useState("'abcdef'")
    
  return (
    <UserContext.Provider value={{name, setName}}> 
        {children}
    </UserContext.Provider>
  )
}

export default UserProvider
