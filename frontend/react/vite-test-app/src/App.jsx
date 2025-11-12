import './App.css'
import Profile, { Avatar } from './components/Profile'
import williamjohnimg from './assets/williamjohn.PNG'
import williamimg from './assets/william.PNG'
import noNameImg from './assets/noName.PNG'
import HeadingStyle from './components/HeadingStyle'
import UserStatus from './components/UserStatus'
import ToDoList from './components/ToDoList'

export function App() {

  return (
    <>
    <ToDoList/>
    <UserStatus status={"false"}/>
    {/* <HeadingStyle/> */}
    {/* <Profile Name='William John' Email='williamjohn@gmail.com' Phone="810-999-3292" imgg = {williamjohnimg}/>
    <Profile Name='Williams' Email='kevinwilliams@gmail.com' Phone="810-858-3292" imgg = {williamimg}/>
    <div className="avatar-left">
      <Avatar imgg={noNameImg} />
    </div> */}
    </>
  )
}


