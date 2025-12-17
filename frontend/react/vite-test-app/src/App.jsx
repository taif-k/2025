import './assets/style/App.css'
import { BrowserRouter, RouterProvider } from 'react-router-dom'
import {router} from './routes/DataMode'
import DeclarativeMode from './routes/DeclarativeMode'
import UserProvider from './provider/UserProvider'

function App() {

  return (
    <UserProvider>
        <RouterProvider router={router} />
    </UserProvider>
    // <>
    //   <BrowserRouter>
    //     <DeclarativeMode/>
    //   </BrowserRouter>
    // </>
  )
}

export default App



