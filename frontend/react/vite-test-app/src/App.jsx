import './App.css'
import { BrowserRouter } from 'react-router-dom'
import DeclarativeMode from './routes/DeclarativeMode'


export function App() {

  return (
    <>
      <BrowserRouter>
        <DeclarativeMode/>
      </BrowserRouter>
    </>
  )
}


