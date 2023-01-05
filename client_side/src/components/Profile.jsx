import { useState, useEffect } from "react";
import { Tab } from "@headlessui/react";
import axios from "axios";

function classNames(...classes) {
  return classes.filter(Boolean).join(" ");
}

export default function Profile({ token }) {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/products/get-order", {
        headers: {
          Authorization: "Token " + token,
        },
      })
      .then((res) => {
        setData(res.data);
      });
  }, [token]);

  let orders = {
    Pending: data.filter((order) => order.status === "pending"),
    Accepted: data.filter((order) => order.status === "accepted"),
    Rejected: data.filter((order) => order.status === "rejected"),
    "On the way": data.filter((order) => order.status === "on_the_way"),
    Canceled: data.filter((order) => order.status === "deleted"),
  };

  const DeleteOrder = (item) => {
    axios.delete(`http://127.0.0.1:8000/products/delete-order/${item.id}`, {
      headers: {
        Authorization: "Token " + token,
      },
    });

    data.forEach(
      (order) => order.id !== item.id || (order.status = "deleted")
    )
    setData([...data]);

    // console.log(data);
  };

  return (
    <div className="font-ordere mt-10">
      <div
        className="w-full max-w-4xl px-2 py-16 sm:px-0 mx-auto"
        id="modal_table"
      >
        <Tab.Group>
          <Tab.List className="flex space-x-1 rounded-xl bg-orange-400 p-1">
            {Object.keys(orders).map((category) => (
              <Tab
                key={category}
                className={({ selected }) =>
                  classNames(
                    "w-full rounded-lg py-2.5 text-base leading-5",
                    "ring-white ring-opacity-40 ring-offset-2 ring-offset-white focus:outline-none focus:ring-2",
                    selected ? "bg-white shadow" : " hover:bg-white/[0.12] "
                  )
                }
              >
                {category}
              </Tab>
            ))}
          </Tab.List>

          <Tab.Panels className="mt-4">
            {Object.values(orders).map((order, id) => (
              <Tab.Panel
                key={id}
                className={classNames(
                  "rounded-xl bg-gray-200 ",
                  "ring-white ring-opacity-60 ring-offset-2 ring-offset-blue-400 focus:outline-none focus:ring-2"
                )}
              >
                {order.map((item, i) => (
                  <div
                    key={i}
                    className="rounded-md py-4 px-12 mx-2 my-4 bg-gray-100 flex flex-row justify-around gap-2"
                  >
                    <div className="flex flex-col gap-4 grow pr-1 border-r-4">
                      {item.products.map((prod, _) => (
                        <div
                          key={_}
                          className="w-full h-20 bg-gray-100 rounded-xl mb-2  grid grid-col-4 grid-row-4 justify-items-center items-center grid-flow-col auto-cols-fr content-center"
                        >
                          <img
                            className="col-span-1 row-span-4 rounded-l-xl col-start-1 h-16"
                            src={"http://127.0.0.1:8000"+prod.photo}
                            alt={prod.description.slice(0, 100)}
                          ></img>
                          <div className="col-span-2 row-span-2 col-start-2 row-start-1 text-black">
                            {prod.full_name.slice(0, 50)}
                          </div>
                          <div className="col-span-2 row-span-1 col-start-2 row-start-3 justify-self-start ml-1 text-gray-400">
                            {/* Description: {prod.description} */}
                          </div>
                          {/* <div className="col-span-1 row-span-1 col-start-2 row-start-4 justify-self-start ml-1">
                            from{" "}
                            <a href={prod.original_link} className="underline">
                              {prod.original_store}
                            </a>
                          </div> */}
                          <div className="col-span-1 row-span-1 col-start-4 row-start-1 inline-flex text-blue-900 font-semibold"></div>
                          <div className="col-span-2 row-span-1 col-start-3 row-start-4 justify-self-end flex flex-row justify-end gap-4"></div>
                          <div className="col-span-1 row-span-2 col-start-4 row-start-2 font-bold">
                            {prod.price} DZD
                          </div>
                        </div>
                      ))}
                    </div>
                    <div
                      className={classNames(
                        "row-span-2  place-self-start ml-2"
                      )}
                    >
                      <p>Name: {item.full_name}</p>
                      <p>Address: {item.address}</p>
                      <p>Phone number: {item.phone_number}</p>
                      <p>Note: {item.description}</p>
                      {item.status === "pending" && (
                        <button
                          onClick={() => DeleteOrder(item)}
                          className="bg-error rounded-lg p-2 w-full mt-4 left-0"
                        >
                          Cancel Order
                        </button>
                      )}
                    </div>
                  </div>
                ))}
              </Tab.Panel>
            ))}
          </Tab.Panels>
        </Tab.Group>
      </div>
    </div>
  );
}
