import { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { FiShoppingCart } from "react-icons/fi";
import { RxAvatar, RxHamburgerMenu } from "react-icons/rx";
import { RiArrowDropDownLine, RiArrowDropRightLine } from "react-icons/ri";

const Navbar = ({ token, cartItems }) => {
  // const [token] = useState(localStorage.getItem("token") || 0);
  const [categories, setCategories] = useState();
  const [stores, setStores] = useState();
  let navigate = useNavigate();

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/products/get-categories").then((res) => {
      setCategories(res.data);
    });

    axios.get("http://127.0.0.1:8000/products/get-stores").then((res) => {
      setStores(res.data);
    });
  }, []);

  function logout() {
    localStorage.clear();
    navigate(0);
  }

  const handleStore = (store) => {
    let params = new URLSearchParams();
    let url = new URL(window.location.origin);

    params.set("original_store", store.original_store);

    for (const [key, value] of params.entries()) {
      url.searchParams.set(`${key}`, `${value}`);
    }

    window.location.href = url.href;
  };

  const handleCat = (cat) => {
    let params = new URLSearchParams();
    let url = new URL(window.location.origin);

    params.set("categorie__categorie_name", cat.categorie_name);

    for (const [key, value] of params.entries()) {
      url.searchParams.set(`${key}`, `${value}`);
    }

    window.location.href = url.href;
  };

  return (
    <div className="navbar bg-orange-500 w-full">
      <div className="flex-1">
        <div className="dropdown">
          <label tabIndex={0} className="btn btn-ghost md:hidden">
            <RxHamburgerMenu />
          </label>

          <ul
            tabIndex={0}
            className="menu menu-compact dropdown-content px-1 bg-white rounded-lg"
          >
            <li className="">
              <button>
                Categories
                <RiArrowDropRightLine />
              </button>
              <ul className="p-2 bg-white">
                {categories
                  ? categories.map((cat) => (
                      <li
                        key={cat.id}
                        className=""
                        onClick={() => {
                          handleCat(cat);
                        }}
                      >
                        <button>{cat.categorie_name}</button>
                      </li>
                    ))
                  : ""}
              </ul>
            </li>

            <li tabIndex={0} className="">
              <button>
                Stores
                <RiArrowDropRightLine />
              </button>
              <ul className="p-2 bg-white w-full">
                {stores
                  ? stores.map((store, _) => (
                      <li key={_} className="">
                        <button
                          onClick={() => {
                            handleStore(store);
                          }}
                        >
                          {store.original_store}
                        </button>
                      </li>
                    ))
                  : ""}
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
              <button>
                Categories
                <RiArrowDropDownLine />
              </button>
              <ul className="p-2 bg-white w-full">
                {categories
                  ? categories.map((cat) => (
                      <li key={cat.id} className="">
                        <button
                          className="text-center"
                          onClick={() => {
                            handleCat(cat);
                          }}
                        >
                          {cat.categorie_name}
                        </button>
                      </li>
                    ))
                  : ""}
              </ul>
            </li>

            <li tabIndex={0} className="">
              <button>
                Stores
                <RiArrowDropDownLine />
              </button>
              <ul className="p-2 bg-white w-full">
                {stores
                  ? stores.map((store, _) => (
                      <li key={_} className="">
                        <button
                          className="text-center"
                          onClick={() => {
                            handleStore(store);
                          }}
                        >
                          {store.original_store}
                        </button>
                      </li>
                    ))
                  : ""}
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
      <div className={`navbar-end ${token ? "hidden" : ""}  `}>
        <a
          href="/login"
          className="btn bg-white text-black hover:bg-white border-none mx-4 px-4"
        >
          Login
        </a>
      </div>
      <div className={`flex-none gap-2 ${token ? "" : "hidden"}`}>
        <a href="/cart">
          <div className="btn btn-ghost btn-circle">
            <div className="indicator">
              <FiShoppingCart className="h-5 w-5" />
              <span className="badge badge-sm indicator-item">
                {cartItems.length}
              </span>
            </div>
          </div>
        </a>
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
              <a href="/profile" className="justify-between">
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
export default Navbar;
