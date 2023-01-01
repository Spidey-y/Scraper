import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { FiShoppingCart } from "react-icons/fi";
import { RxAvatar, RxHamburgerMenu } from "react-icons/rx";
import { RiArrowDropDownLine } from "react-icons/ri";
import { BsSearch } from "react-icons/bs";

const Navbar = () => {
  const [sessionId] = useState(localStorage.getItem("sessionId") || 0 )
  let navigate = useNavigate();

  function logout() {
    localStorage.clear();
    navigate(0);
  }
  
  return (
    <div className="navbar bg-orange-500">
      <div className="flex-1">
        <div className="dropdown">
          <label tabIndex={0} className="btn btn-ghost md:hidden">
            <RxHamburgerMenu />
          </label>

          <ul tabIndex={0} className="menu menu-compact dropdown-content px-1">
            <li className="">
              <a href="/">
                Categories
                <RiArrowDropDownLine />
              </a>
              <ul className="p-2 bg-base-100">
                <li className="">
                  <a href="/">Submenu 1</a>
                </li>
                <li className="">
                  <a href="/">Submenu 2</a>
                </li>
              </ul>
            </li>

            <li tabIndex={0} className="">
              <a href="/">
                Stores
                <RiArrowDropDownLine />
              </a>
              <ul className="p-2 bg-base-100">
                <li className="">
                  <a href="/">Submenu 1</a>
                </li>
                <li className="">
                  <a href="/">Submenu 2</a>
                </li>
              </ul>
            </li>
            <li className="">
              <a href="/about">About us</a>
            </li>
            <li className="">
              <a href="/contact">Contact us</a>
            </li>
          </ul>
        </div>
        <a
          href="/"
          className="btn normal-case text-base bg-white hover:bg-white text-black border-0"
        >
          Logo
        </a>
        <div className="hidden md:flex">
          <ul tabIndex={0} className="menu menu-horizontal px-1">
            <li className="">
              <a href="/">
                Categories
                <RiArrowDropDownLine />
              </a>
              <ul className="p-2 bg-base-100">
                <li className="">
                  <a href="/">Submenu 11</a>
                </li>
                <li className="">
                  <a href="/">Submenu 2</a>
                </li>
              </ul>
            </li>

            <li tabIndex={0} className="">
              <a href="/">
                Stores
                <RiArrowDropDownLine />
              </a>
              <ul className="p-2 bg-base-100">
                <li className="">
                  <a href="/">Submenu 1</a>
                </li>
                <li className="">
                  <a href="/">Submenu 2</a>
                </li>
              </ul>
            </li>
            <li className="">
              <a href="/about">About us</a>
            </li>
            <li className="">
              <a href="/contact">Contact us</a>
            </li>
          </ul>
        </div>
      </div>
      <div className={`navbar-end ${sessionId ? 'hidden' : '' }  `}>
        <a href="/login" className="btn bg-white text-black hover:bg-white border-none mx-4 px-4">
          Login
        </a>
      </div>
      <div className={`flex-none gap-2 ${sessionId ? '' : 'hidden' }`}>
        <div className="form-control hidden md:flex">
          <div className="input-group">
            <input
              type="text"
              placeholder="Search…"
              className="input input-bordered"
            />
            <button className="btn btn-square">
              <BsSearch className="h-5 w-5 bold" />
            </button>
          </div>
        </div>

        <div className="btn btn-ghost btn-circle">
          <div className="indicator">
            <a href="/">
              <FiShoppingCart className="h-5 w-5" />
            </a>
            <span className="badge badge-sm indicator-item">8</span>
          </div>
        </div>
        <div className="dropdown dropdown-end">
          <label tabIndex={0} className="btn btn-ghost btn-circle avatar">
            <div className="w-8 rounded-full">
              <RxAvatar className="h-8 w-8" />
            </div>
          </label>
          <ul
            tabIndex={0}
            className="menu menu-compact dropdown-content mt-3 p-2 shadow bg-base-100 rounded-box w-52"
          >
            <li className="">
              <a href="/" className="justify-between">
                Profile
              </a>
            </li>
            <li className="">
              <button onClick={logout}>Logout</button>
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
};
export default Navbar