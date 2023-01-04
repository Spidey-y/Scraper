import React from "react";
import { useState } from "react";
import axios from "axios";

const Login = ({ setToken }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = () => {
    axios
      .post("http://127.0.0.1:8000/user/login", {
        email: email,
        password: password,
      })
      .then((response) => {
        let token = response.data.Token + " ";
        localStorage.setItem("token", token);
        setToken(token);
        window.location.href = "/";
      })
      .catch((err) => {
        alert("Wrong credentials");
      });
  };

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault();
        handleLogin();
      }}
      className="flex flex-col gap-4 items-center container mx-auto my-8 p-12 border-gray-200 border"
    >
      <span className="text-3xl">Log in</span>

      <div className="form-control">
        <label className="label">
          <span className="label-text">Your Email</span>
        </label>
        <label className="input-group">
          <span>Email</span>
          <input
            value={email}
            onChange={(e) => {
              setEmail(e.target.value);
            }}
            id="email"
            type="email"
            onInput={(e) => e.target.setCustomValidity("")}
            onInvalid={(e) =>
              e.target.setCustomValidity("Please Enter a valid email")
            }
            required
            autoComplete="off"
            placeholder="user@user.com"
            className="input input-bordered"
          />
        </label>
      </div>
      <div className="form-control">
        <label className="label">
          <span className="label-text">Password</span>
        </label>
        <label className="input-group">
          <span>Password</span>
          <input
            value={password}
            onChange={(e) => {
              setPassword(e.target.value);
            }}
            id="password"
            type="password"
            required
            placeholder=""
            className="input input-bordered"
          />
        </label>
      </div>
      <input
        type="submit"
        className="btn btn-outline bg-orange-500 hover:bg-orange-300 hover:text-inherit w-36"
        // onClick={handleLogin}
        value={"Login"}
      />

      <span className="text-xl justify-self-start">
        Don't have an account?
        <a className="underline" href="/register">
          Register
        </a>
      </span>
      {/* </div> */}
    </form>
  );
};

export default Login;
