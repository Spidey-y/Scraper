import ConfirmOrder from "./ConfirmOrder";
const Cart = ({ token, cartItems, setCart, counter, setCounter }) => {
  const DeleteItem = (item, i) => {
    let lcart = cartItems;
    lcart.splice(i, 1);

    let lcount = {
      ...counter,
      [`${item.id}`]: counter[`${item.id}`] - 1,
    };

    lcount[`${item.id}`] === 0 && delete lcount[`${item.id}`];

    localStorage.setItem("cart", JSON.stringify(lcart));
    localStorage.setItem("counter", JSON.stringify(lcount));

    setCounter(lcount);
    setCart(lcart);
  };
  return (
    <>
      <div className="container flex flex-col mx-auto place-items-center">
        <ConfirmOrder token={token} cartItems={cartItems} counter={counter} setCart={setCart} setCounter={setCounter}/>
        {/* <ConfirmOrder/> */}
        {cartItems.map((prod, _) => (
          <div
            key={_}
            className="w-full h-40 bg-gray-100 rounded-xl mb-6 grid grid-col-4 grid-row-4 justify-items-center items-center grid-flow-col auto-cols-fr content-center"
          >
            <img
              className="col-span-1 row-span-4 rounded-l-xl col-start-1 h-36"
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
            <div className="col-span-1 row-span-1 col-start-4 row-start-1 inline-flex text-blue-900 font-semibold"></div>
            <div className="col-span-1 row-span-2 col-start-4 row-start-2 text-xl md:text-2xl font-bold">
              {prod.price} DZD
            </div>
            <div className="col-span-2 row-span-1 col-start-3 row-start-4 justify-self-end flex flex-row justify-end gap-4">
              <button
                onClick={() => DeleteItem(prod, _)}
                className="bg-error rounded-lg p-4 text-lg left-0"
              >
                Delete
              </button>
            </div>
          </div>
        ))}
      </div>
    </>
  );
};

export default Cart;
