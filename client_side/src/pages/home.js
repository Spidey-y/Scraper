import Navbar from '../components/Navbar';
import Top from '../components/Ads/Top';
import Main from '../components/Main';

function Home() {

  // useEffect(() => {
  //   const sessionId = localStorage.getItem("sessionId") || '0';
  //   console.log(sessionId);
  // }, [])

  return (
    <>
      <Navbar />
      <Top />
      <Main />
    </>
  );
}

export default Home;