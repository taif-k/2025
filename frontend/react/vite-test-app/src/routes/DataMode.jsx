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
import RbBadges from "../components/RbBadges";
import RbButtons from "../components/RbButtons";
import RbButtonGroup from "../components/RbButtonGroup";
import RbCards from "../components/RbCards";
import RbImages from "../components/RbImages";
import RbListGroup from "../components/RbListGroup";
import RbFigures from "../components/RbFigures";
import RbPagination from "../components/RbPagination";
import RbProgressBar from "../components/RbProgressBar";
import RbSpinner from "../components/RbSpinner";
import RbTable from "../components/RbTable";
import RbCloseButton from "../components/RbCloseButton";



export const router = createBrowserRouter([
  {
    path: '/',
    element: <RootLayout />,
    children: [
      { index: true, element: <Home /> },
      { path: '/usereduce', element: <CountWithReducer /> },
      { path: '/usestate', element: <Count /> },
      { path: '/todo', element: <ToDoList /> },
      { path: '/userstatus', element: <UserStatus /> },
      { path: '/headingstyle', element: <HeadingStyle /> },
      { path: '/profile', element: <Profile /> },
      { path: '/avatar', element: <Avatar /> },
      { path: '/reactbootstrap', element: <ReactBootstrap /> },
      { path: '/badges', element: <RbBadges /> },
      { path: '/buttons', element: <RbButtons /> },
      { path: '/buttongroups', element: <RbButtonGroup /> },
      { path: '/cards', element: <RbCards /> },
      { path: '/images', element: <RbImages /> },
      { path: '/listgroup', element: <RbListGroup /> },
      { path: '/figures', element: <RbFigures /> },
      { path: '/pagination', element: <RbPagination /> },
      { path: '/progressbar', element: <RbProgressBar /> },
      { path: '/spinner', element: <RbSpinner /> },
      { path: '/table', element: <RbTable /> },
      { path: '/closebutton', element: <RbCloseButton /> },
    ]
  },
  {
    path: '/',
    element: <AuthLayout />,
    children: [
      { path: '/login', element: <Login /> }
    ]
  }
])