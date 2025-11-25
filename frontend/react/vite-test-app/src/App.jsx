import './App.css'
import { BrowserRouter, RouterProvider } from 'react-router-dom'
import {router} from './routes/DataMode'
import DeclarativeMode from './routes/DeclarativeMode'

function App() {

  return (
    <RouterProvider router={router} />

    // <>
    //   <BrowserRouter>
    //     <DeclarativeMode/>
    //   </BrowserRouter>
    // </>
  )
}

export default App



