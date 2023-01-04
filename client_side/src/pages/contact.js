import Navbar from '../components/Navbar';
import Contact from '../components/Contact'

function Contactus({ token, cartItems }) {
  return (
    <>
      <Navbar token={token} cartItems={cartItems} />
      <Contact />     
    </>
  );
}

export default Contactus;