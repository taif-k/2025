import './assets/style/App.css'
import { BrowserRouter, RouterProvider } from 'react-router-dom'
import {router} from './routes/DataMode'
import DeclarativeMode from './routes/DeclarativeMode'
import UserProvider from './provider/UserProvider'
import WishListProvider from './provider/WishListProvider'

function App() {

  return (
    <UserProvider>
      <WishListProvider>
        <RouterProvider router={router} />
      </WishListProvider>
    </UserProvider>
    // <>
    //   <BrowserRouter>
    //     <DeclarativeMode/>
    //   </BrowserRouter>
    // </>
  )
}

export default App



