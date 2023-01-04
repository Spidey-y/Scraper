import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

import Navbar from '../components/Navbar';
import CartComponent from '../components/Cart';

function Cart({ token, cartItems, setCart, counter, setCounter }) {
  
  let history = useNavigate();

  useEffect(() => {
    if (!token) {
      history("/login");
    }
  }, [history, token]);

  return (
    <>
      <Navbar token={token} cartItems={cartItems}/>
      <CartComponent token={token} cartItems={cartItems} setCart={setCart} counter={counter} setCounter={setCounter} />      
    </>
  );
}

export default Cart;