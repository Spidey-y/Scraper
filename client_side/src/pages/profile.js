import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

import Navbar from '../components/Navbar';
import Profile from '../components/Profile';

function Register({ token, cartItems }) {
  
  let history = useNavigate();

  useEffect(() => {
    if (!token) {
      history("/login");
    }
  }, [history, token]);

  return (
    <>
      <Navbar token={token} cartItems={cartItems} />
      <Profile token={token} />      
    </>
  );
}

export default Register;