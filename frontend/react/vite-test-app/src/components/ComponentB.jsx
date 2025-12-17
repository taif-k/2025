import ComponentC from './ComponentC'
import { UserContext } from '../context/Context'
import { useContext } from 'react'

const ComponentB = () => {
    const {name} = useContext(UserContext)

  return (
    <div>
      Name {name} in Component B
      <ComponentC />
    </div>
  )
}

export default ComponentB
