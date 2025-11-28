import Count from "../components/Count";
import CountWithReducer from "../components/CountWithReducer";
import HeadingStyle from "../components/HeadingStyle";
import Home from "../components/Home";
import Profile, { Avatar } from "../components/Profile";
import ToDoList from "../components/ToDoList";
import UserStatus from "../components/UserStatus";
import AuthLayout from "../layout/AuthLayout";
import RootLayout from "../layout/RootLayout";
import Login from "../pages/Login";
import { createBrowserRouter } from "react-router-dom";
import ReactBootstrap from "../pages/ReactBootstrap";


  export const router = createBrowserRouter([
    {
      path: '/',
      element: <RootLayout />,
      children: [
        { index: true, element: <Home/>},
        { path: '/usereduce', element: <CountWithReducer /> },
        { path: '/usestate', element: <Count /> },
        { path: '/todo', element: <ToDoList /> },
        { path: '/userstatus', element: <UserStatus /> },
        { path: '/headingstyle', element: <HeadingStyle /> },
        { path: '/profile', element: <Profile /> },
        { path: '/avatar', element: <Avatar /> },
        { path: '/reactbootstrap', element: <ReactBootstrap /> },
      ]
    },
    {
        path: '/',
        element: <AuthLayout/>,
        children: [
            {path: '/login', element: <Login/>}
        ]
    }
  ])