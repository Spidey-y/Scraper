import { useState, useEffect } from "react";
import axios from "axios";
import Top from "./Ads/Top";
import Side from "./Ads/Side";
import Filter from "./Filter";
import Products from "./Products";

const Main = () => {
  const [topAd, setTop] = useState({});
  const [sideAds, setSide] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/ads").then((res) => {
      let ads = res.data;
      ads = ads.filter((e) => e.is_active);
      setTop(ads.find((e) => e.position === "Top"));
      setSide(ads.filter((e) => e.position === "Side"));
    });
  }, []);

  return (
    <>
      {topAd ? <Top ad={topAd} /> : ""}
      <div className="container mx-auto mt-20 flex flex-row gap-8 justify-between">
        <div className="basis-11/12">
          <Filter />
          <Products />
        </div>
        <div className="basis-1/12">
        {sideAds.length ? <Side ads={sideAds} /> : ""}
        </div>
      </div>
    </>
  );
};

export default Main;
