import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import {App,Txt} from './App.jsx' // when doing default import(it can be named anything)

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Txt/>
    <App/>
  </StrictMode>,
)
