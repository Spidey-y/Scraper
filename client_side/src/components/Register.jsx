import React from "react";
import { useState } from "react";
import { Axios } from "axios";

const Register = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [fname, setFname] = useState("");
  const [lname, setLname] = useState("");
  const [tel, setTel] = useState("");
  const [addr, setAddr] = useState("");

  const handleRegister = () => {
    Axios.post("http://127.0.0.1:8000/user/register", {
      first_name: fname,
      last_name: lname,
      phone_number: tel,
      address: addr,
      email: email,
      password: password,
    })
      .then((response) => {
        // console.log();
        let token = response.data.Token + " ";
        localStorage.setItem("sessionId", token);
      })
      .catch((err) => {
        alert("Wrong credentials");
      });
  };
  return (
    <div className="flex flex-col gap-4 items-center container mx-auto my-8 p-12 border-gray-200 border">
      <span className="text-3xl">Register</span>
      {/* <div className=""> */}
      {/* <label className="label item-right">What is your name?</label> */}
      <input
        value={fname}
        onChange={(e) => {
          setFname(e.target.value);
        }}
        id="fname"
        type="text"
        placeholder="Firsr name"
        className="input input-bordered w-full max-w-xs"
      />
      <input
        value={lname}
        onChange={(e) => {
          setLname(e.target.value);
        }}
        id="lname"
        type="text"
        placeholder="Last name"
        className="input input-bordered w-full max-w-xs"
      />
      <input
        value={tel}
        onChange={(e) => {
          setTel(e.target.value);
        }}
        id="tel"
        type="tel"
        placeholder="Phone number"
        className="input input-bordered w-full max-w-xs"
      />
      <input
        value={addr}
        onChange={(e) => {
          setAddr(e.target.value);
        }}
        id="addr"
        type="text"
        placeholder="Address"
        className="input input-bordered w-full max-w-xs"
      />
      <input
        value={email}
        onChange={(e) => {
          setEmail(e.target.value);
        }}
        id="email"
        type="email"
        placeholder="email"
        className="input input-bordered w-full max-w-xs"
      />
      <input
        value={password}
        onChange={(e) => {
          setPassword(e.target.value);
        }}
        id="password"
        type="password"
        placeholder="password"
        className="input input-bordered w-full max-w-xs"
      />
      <button
        className="btn btn-outline bg-orange-500 hover:bg-orange-300 hover:text-inherit w-36"
        onClick={handleRegister}
      >
        Register
      </button>

      <span className="text-xl justify-self-start">
        Already have an account?{" "}
        <a href="/login" className="underline">
          Login
        </a>
      </span>
      {/* </div> */}
    </div>
  );
};

export default Register;
