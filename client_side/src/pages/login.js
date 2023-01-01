import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

import Navbar from "../components/Navbar";
import LoginForm from "../components/Login";

function Login() {

  let history = useNavigate();

  useEffect(() => {
    const sessionId = localStorage.getItem("sessionId") || 0;
    if (sessionId) {
      history("/");
    } else {
      console.log("something went wrong");
      history("/login");
    }
  }, [history]);

  return (
    <>
      <Navbar />
      <LoginForm />
    </>
  );
}

export default Login;
