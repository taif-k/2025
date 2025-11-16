import React, { useState } from 'react'

const Count = () => {
    const [count, setState] = useState(0)
    const add = ()=>{
        count < 20 && setState(count + 1)

        console.log(count)
        return count

    }
    const sub = ()=>{
        count > 0 && setState(count - 1) 
         console.log(count)
        return count

    }
  return (
    <>
       <div>Count Value = {count}</div> 
      <button className='btn btn-outline-primary' onClick={add}>INCREMENT</button>
      <button className='btn btn-outline-primary' onClick={sub}>DECREMENT</button>

    {count === 20 && <p>Maximum limit reached.</p>}
    {count === 0 && <p>Minimum limit reached.</p>}
    </>
  )
}

export default Count
