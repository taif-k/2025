import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import { App, Txt } from './App.jsx' // when doing default import(it can be named anything)
import Profile from './components/Profile.jsx'
import MultipleComponenets from './components/MultipleComponenets.jsx'


createRoot(document.getElementById('root')).render(
  <>
    <Profile
      Name="Kevin Williams"
      Email="Kevinwilliams@gmail.com"
      Phone="810-858-3292"
    />
  </>
)
