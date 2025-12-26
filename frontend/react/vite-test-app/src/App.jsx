import "./assets/style/App.css";
import { RouterProvider } from "react-router-dom";
import { router } from "./routes/DataMode";

import UserProvider from "./provider/UserProvider";
import WishListProvider from "./provider/WishListProvider";
import CartListProvider from "./provider/CartListProvider";

function App() {
  return (
    <UserProvider>
      <WishListProvider>
        <CartListProvider>
          <RouterProvider router={router} />
        </CartListProvider>
      </WishListProvider>
    </UserProvider>
  );
}

export default App;
