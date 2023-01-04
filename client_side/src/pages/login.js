import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Navbar from "../components/Navbar";
import LoginForm from "../components/Login";

function Login({ token, setToken, cartItems }) {

  const history = useNavigate();
  useEffect(() => {
    if (token) {
      history("/");
    }
  }, [history, token]);

  return (
    <>
      <Navbar token={token} cartItems={cartItems} />
      <LoginForm setToken={setToken} />
    </>
  );
}

export default Login;
