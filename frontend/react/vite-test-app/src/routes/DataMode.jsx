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
// import ReactBootstrap from "../pages/ReactBootstrap";
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
import RbBreadCrumb from "../components/RbBreadCrumbs";
import RbAccordion from "../components/RbAccordion";
import RbCrousel from "../components/RbCrousel";
import RBOverlayToolTip from "../components/RBOverlayToolTip";
import RbModal from "../components/RbModal";
import RbDropdown from "../components/RbDropdown";
import RbNavbarOffCanvas from "../components/RbNavbarOffCanvas";
import RbNavTab from "../components/RbNavTab";
import RhForm from "../forms/RhForm";
import RhFormYup from "../forms/RhFormYup";
import StateManagement from "../pages/StateManagement";
import Products from "../pages/Products";
import WishList from "../pages/WishList";
import Blog from "../pages/blog/Blog"
import BlogDetail from "../pages/blog/BlogDetail"



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
      // { path: '/reactbootstrap', element: <ReactBootstrap /> },
      { path: '/badges', element: <RbBadges /> },
      { path: '/breadcrumb', element: <RbBreadCrumb /> },
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
      { path: '/accordion', element: <RbAccordion /> },
      { path: '/crousel', element: <RbCrousel /> },
      { path: '/overlay', element: <RBOverlayToolTip /> },
      { path: '/modal', element: <RbModal /> },
      { path: '/dropdown', element: <RbDropdown /> },
      { path: '/navbar-offcanvas', element: <RbNavbarOffCanvas /> },
      { path: '/navtab', element: <RbNavTab /> },
      { path: '/rhform', element: <RhForm /> },
      { path: '/rhformyup', element: <RhFormYup /> },
      {path: "/statemanagement", element: <StateManagement/>},
      {path: "/product", element: <Products/>},
      {path: "/wishlist", element: <WishList/>},
      {path: "/blog/:id", element: <BlogDetail/>},
      {path: "/blog", element: <Blog/>},

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