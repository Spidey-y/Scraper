import axios from "axios";
import { useEffect, useState } from "react";
import { AiFillShopping, AiFillCalendar } from "react-icons/ai";

const About = () => {
  const [about, setAbout] = useState({});
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/aboutus/")
      .then((res) => setAbout(res.data));
  }, []);
  return (
    <div className="mb-4 container mx-auto my-8 p-12 border-gray-200 border-2 w-full">
      <h1 className="text-center text-4xl mb-16"> About us</h1>.
      <div className="text-lg font-medium leading-loose flex flex-row gap-8 justify-around">
        <div className="bg-gray-200 h-full w-full p-8  text-center ">
          <AiFillShopping className="h-1/2 w-1/2 mx-auto" />
          <p>{about.about_us_1}</p>
        </div>
        <div className="bg-gray-200 h-full w-full p-8 ">
          <AiFillCalendar className="h-1/2 w-1/2 mx-auto" />
          <p>{about.about_us_2}</p>
        </div>
      </div>
    </div>
  );
};

export default About;
