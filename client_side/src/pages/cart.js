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
      {cartItems.length ? <CartComponent token={token} cartItems={cartItems} setCart={setCart} counter={counter} setCounter={setCounter} />   : <div className='text-center text-2xl mt-8'>No items in cart</div>}   
    </>
  );
}

export default Cart;