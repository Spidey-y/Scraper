import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

import Navbar from "../components/Navbar";
import RegisterForm from "../components/Register";

function Register({ token, setToken, cartItems }) {
  let history = useNavigate();

  useEffect(() => {
    if (token) {
      history("/");
    }
  }, [history, token]);

  return (
    <>
      <Navbar token={token} cartItems={cartItems} />
      <RegisterForm setToken={setToken} />
    </>
  );
}

export default Register;
