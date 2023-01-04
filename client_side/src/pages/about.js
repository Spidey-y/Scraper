import Navbar from '../components/Navbar';
import About from '../components/About'

function Aboutus({ token, cartItems }) {
  return (
    <>
      <Navbar token={token} cartItems={cartItems} />
      <About />
    </>
  );
}

export default Aboutus;