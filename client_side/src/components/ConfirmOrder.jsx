import axios from "axios";
import { useState, useEffect } from "react";

function ConfirmOrder({ token, cartItems, counter, setCart, setCounter }) {
  const [name, setName] = useState("");
  const [addr, setAddr] = useState("");
  const [phone, setPhone] = useState("");
  const [note, setNote] = useState("");

  useEffect(() => {
    let modal = document.getElementById("my-modal");
    let btn = document.getElementById("open-btn");
    let frame = document.getElementById("frame");

    btn.onclick = function () {
      modal.style.display = "flex";
      frame.classList.add("blur");
    };

    window.onclick = function (event) {
      if (event.target === modal) {
        modal.style.display = "none";
        frame.classList.remove("blur");
      }
    };
  });

  const handleCommand = () => {
    axios
      .get("http://127.0.0.1:8000/user/profile", {
        headers: {
          Authorization: "Token " + token,
        },
      })
      .then((res) => {
        axios
          .post(
            "http://127.0.0.1:8000/products/add-order",
            {
              products: cartItems.map(e => e.id),
              full_name: name,
              address: addr,
              phone_number: phone,
              description: note,
              user: res.data.id,
            },
            {
              headers: {
                Authorization: "Token " + token,
              },
            }
          )
          .then((res) => {
            localStorage.removeItem('cart');
            localStorage.removeItem('counter');
            setCart([]);
            setCounter({})
            alert('the order has been passed')
            window.location.href = '/'
          }).catch(err => alert('something went wrong, try again later'));
      });
  };

  return (
    <div>
      <div id="frame">
        <button
          className="bg-orange-500 text-white rounded-md mt-10 mb-5 px-8 py-2"
          id="open-btn"
        >
          Confirm Order
        </button>
      </div>

      <div
        className="fixed hidden inset-0 bg-gray-100 bg-opacity-50  overflow-y-auto h-full items-center justify-center"
        id="my-modal"
      >
        <div className="relative p-5 sm:mx-12 md:mx-8  mx-auto lg:w-1/2 w-full shadow-lg rounded-md bg-gray-300 ">
          <div className="mt-10 sm:mt-0 px-8">
            <div className="p-4 mb-2 sm:px-0 bg-jaune rounded-full mx-24  flex flex-col">
              <h3 className="text-3xl font-bold text-center">
                Total:{" "}
                {Math.trunc(
                  cartItems.reduce((e, x) => e + parseFloat(x.price), 0) * 100
                ) / 100}{" "}
                DZD
              </h3>
              <form
                onSubmit={(e) => {
                  e.preventDefault();
                  handleCommand();
                }}
              >
                <div className="py-4">
                  <label className="block text-lg font-bold text-gray-700">
                    Full name
                  </label>
                  <input
                    type="text"
                    required
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    autoComplete="off"
                    className="formelem mt-1 block w-full rounded-md border border-gray-300 h-8 p-4"
                  />
                </div>

                <div className="py-4">
                  <label className="block text-lg font-bold text-gray-700">
                    Address
                  </label>
                  <input
                    type="text"
                    required
                    value={addr}
                    onChange={(e) => setAddr(e.target.value)}
                    autoComplete="off"
                    className="formelem mt-1 block w-full rounded-md border border-gray-300 h-8 p-4"
                  />
                </div>

                <div className="py-4">
                  <label className="block text-lg font-bold text-gray-700">
                    Phone Number
                  </label>
                  <input
                    type="tel"
                    pattern="0[0-9]{9}"
                    onInput={e => e.target.setCustomValidity('')}
                    onInvalid={e => e.target.setCustomValidity('Please Enter a valid phone number')}
                    required
                    value={phone}
                    onChange={(e) => setPhone(e.target.value)}
                    autoComplete="off"
                    className="formelem mt-1 block w-full rounded-md border border-gray-300 h-8 p-4"
                  />
                </div>

                <div className="py-4">
                  <label className="block text-lg font-bold text-gray-700">
                    Note
                  </label>
                  <input
                    type="text"
                    value={note}
                    onChange={(e) => setNote(e.target.value)}
                    autoComplete="off"
                    className="formelem mt-1 block w-full rounded-md border border-gray-300 h-8 p-4"
                  />
                </div>

                <input
                  type="submit"
                  className="bg-orange-500 rounded-lg mt-4 p-4 text-lg w-full"
                  value="Confirm Order"
                />
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default ConfirmOrder;
