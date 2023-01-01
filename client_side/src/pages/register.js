import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

import Navbar from '../components/Navbar';
import RegisterForm from '../components/Register';

function Register() {
  
  let history = useNavigate();

  useEffect(() => {
    const sessionId = localStorage.getItem("sessionId") || 0;
    if (sessionId) {
      history("/");
    } else {
      console.log("something went wrong");
      history("/register");
    }
  }, [history]);

  return (
    <>
      <Navbar/>
      <RegisterForm />      
    </>
  );
}

export default Register;