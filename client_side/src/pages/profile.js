import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

import Navbar from '../components/Navbar';
import RegisterForm from '../components/Register';

function Register({ token, cartItems, setCart }) {
  
  let history = useNavigate();

  useEffect(() => {
    if (!token) {
      history("/login");
    }
  }, [history, token]);

  return (
    <>
      <Navbar token={token} cartItems={cartItems} />
      <RegisterForm />      
    </>
  );
}

export default Register;