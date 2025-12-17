import { useContext } from 'react'
import ComponentA from '../components/ComponentA'
import { UserContext } from '../context/Context'

const StateManagement = () => {
    const {name} = useContext(UserContext)
//   const name = "'test name'"
    return (
    <div>
      Name {name} in State Management
      <ComponentA/>
    </div>
  )
}

export default StateManagement
