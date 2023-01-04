import { useEffect, useState } from "react";
import { FaCertificate } from "react-icons/fa";

const Products = ({ products, cartItems, setCart, counter, setCounter }) => {
  const [p, setP] = useState(1);
  // const [] = useState({});

  useEffect(() => {
    let s = new URLSearchParams(window.location.search);
    setP(parseInt(s.get("page")) || 1);
  }, []);

  const handlePrev = () => {
    let s = new URLSearchParams(window.location.search);
    s.set("page", p - 1);
    window.location.search = s.toString();
  };
  const handleNext = () => {
    let s = new URLSearchParams(window.location.search);
    s.set("page", p + 1);
    window.location.search = s.toString();
  };

  const addToCart = (prod) => {
    let lcount = {
      ...counter,
      [`${prod.id}`]: cartItems.reduce(
        (count, x) => count + (JSON.stringify(x) === JSON.stringify(prod)),
        1
      ),
    };

    let lcart = [...cartItems, prod];

    localStorage.setItem("cart", JSON.stringify(lcart));
    setCart(lcart);
    localStorage.setItem("counter", JSON.stringify(lcount));
    setCounter(lcount);
  };
  return (
    <div className="flex flex-col mt-8 gap-8">
      {products.results &&
        products.results.map((prod) => (
          <div
            key={prod.id}
            className="w-full bg-gray-100 rounded-xl mb-6 grid grid-col-4 grid-row-4 justify-items-center items-center grid-flow-col auto-cols-fr content-center"
          >
            <img
              className="col-span-1 row-span-4 rounded-l-xl col-start-1 h-72"
              src={prod.photo}
              alt={prod.description}
            ></img>
            <div className="col-span-2 row-span-2 col-start-2 row-start-1 text-lg md:text-xl text-black">
              {prod.full_name}
            </div>
            <div className="col-span-2 row-span-1 col-start-2 row-start-3 md:text-lg justify-self-start ml-4 text-gray-400">
              Description: {prod.description}
            </div>
            <div className="col-span-1 row-span-1 col-start-2 row-start-4 justify-self-start ml-4">
              from{" "}
              <a href={prod.original_link} className="underline">
                {prod.original_store}
              </a>
            </div>
            <div className="col-span-1 row-span-1 col-start-4 row-start-1 inline-flex text-blue-900 font-semibold">
              {prod.staff_pick ? (
                <>
                  <FaCertificate className=" h-5 w-5 mr-2" /> Staff Picked{" "}
                </>
              ) : (
                ""
              )}
            </div>
            <div className="col-span-1 row-span-2 col-start-4 row-start-2 text-xl md:text-2xl font-bold">
              {prod.price} DZD
            </div>
            <div className="col-span-2 row-span-1 col-start-3 row-start-4 justify-self-end flex flex-row justify-end gap-4">
              {counter[`${prod.id}`] ? (
                <p className="text-center self-center">
                  Qte: {counter[`${prod.id}`]}
                </p>
              ) : (
                ""
              )}
              <button
                onClick={() => addToCart(prod)}
                className="bg-orange-500 rounded-lg p-4 text-lg left-0"
              >
                Add to cart
              </button>
            </div>
          </div>
        ))}
      <div className="btn-group self-center mb-20">
        {products.previous && (
          <button onClick={handlePrev} className="btn">
            «
          </button>
        )}
        <button className="btn">Page {p}</button>
        {products.next && (
          <button onClick={handleNext} className="btn">
            »
          </button>
        )}
      </div>
    </div>
  );
};

export default Products;
