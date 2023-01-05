import { useState } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

import Login from "./pages/login";
import Home from "./pages/home";
import Register from "./pages/register";
import Profile from './pages/profile';
import Cart from './pages/cart'
import About from "./pages/about";
import Contact from "./pages/contact";

function App() {
  const [token, setToken] = useState(localStorage.getItem("token") || 0);
  const [cartItems, setCart] = useState(JSON.parse(localStorage.getItem('cart')) || []);
  const [counter, setCounter] = useState(JSON.parse(localStorage.getItem('counter'))||{});

  return (
    <Router>
      <div className="App">
        <div className="content">
          <Routes>
            <Route path="/" element={<Home token={token} cartItems={cartItems} setCart={setCart} counter={counter} setCounter={setCounter} />} />
            <Route exact path="/login" element={<Login token={token} setToken={setToken} cartItems={cartItems} />} />
            <Route exact path="/register" element={<Register token={token} setToken={setToken} cartItems={cartItems} />} />
            <Route exact path="/profile" element={<Profile token={token} cartItems={cartItems} />} />
            <Route exact path="/cart" element={<Cart token={token} cartItems={cartItems} setCart={setCart} counter={counter} setCounter={setCounter} />} />
            <Route path="/about" element={<About token={token} cartItems={cartItems} />} />
            <Route path="/contact" element={<Contact token={token} cartItems={cartItems} />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
