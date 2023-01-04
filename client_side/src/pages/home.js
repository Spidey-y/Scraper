import Navbar from '../components/Navbar';
import Main from '../components/Main';

function Home({ token, cartItems, setCart, counter, setCounter }) {

  return (
    <>
      <Navbar token={token} cartItems={cartItems} />
      <Main cartItems={cartItems} setCart={setCart} counter={counter} setCounter={setCounter} />
    </>
  );
}

export default Home;