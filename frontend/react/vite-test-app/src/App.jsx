import './App.css'
import Profile, { Avatar } from './components/Profile'
import williamjohnimg from './assets/williamjohn.PNG'
import williamimg from './assets/william.PNG'
import noNameImg from './assets/noName.PNG'

export function App() {

  return (
    <>
    <Profile Name='Williams' Email='kevinwilliams@gmail.com' Phone="810-999-3292" imgg = {williamjohnimg}/>
    <Profile Name='Kevin Williams' Email='kevinwilliams@mail.com' Phone="810-858-3292" imgg = {williamimg}/>
    <div className="avatar-left">
      <Avatar imgg={noNameImg} />
    </div>
    </>
  )
}


