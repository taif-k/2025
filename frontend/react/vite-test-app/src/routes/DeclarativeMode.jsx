
import Profile, { Avatar } from '../components/Profile'
// import williamjohnimg from './assets/williamjohn.PNG'
// import williamimg from './assets/william.PNG'
// import noNameImg from './assets/noName.PNG'
import HeadingStyle from '../components/HeadingStyle'
import UserStatus from '../components/UserStatus'
import ToDoList from '../components/ToDoList'
import Count from '../components/Count'
import CountWithReducer from '../components/CountWithReducer'
import RootLayout from '../layout/RootLayout'
import Home from '../components/Home'
import { Routes, Route } from 'react-router-dom'
import AuthLayout from '../layout/AuthLayout'
import Login from '../pages/Login'


const DeclarativeMode = () => {
    return (
        <>
            <Routes>
                <Route path="/" element={<RootLayout />}>
                    <Route index element={<Home />} />
                    <Route path="/usereduce" element={<CountWithReducer />} />
                    <Route path="/usestate" element={<Count />} />
                    <Route path="/todo" element={<ToDoList />} />
                    <Route path="/userstatus" element={<UserStatus />} />
                    <Route path="/headingstyle" element={<HeadingStyle />} />
                    <Route path="/profile" element={<Profile />} />
                    <Route path="/avatar" element={<Avatar />} />
                </Route>
                <Route element={<AuthLayout/>}>
                    <Route path="/login" element={<Login/>} />
                </Route>
            </Routes>
        </>
    )
}

export default DeclarativeMode
