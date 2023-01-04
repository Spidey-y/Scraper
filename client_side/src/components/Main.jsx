import { useState, useEffect } from "react";
import axios from "axios";
import Top from "./Ads/Top";
import Side from "./Ads/Side";
import Filter from "./Filter";
import Products from "./Products";

const Main = ({ cartItems, setCart, counter, setCounter }) => {
  const [topAd, setTop] = useState({});
  const [sideAds, setSide] = useState([]);
  const [categories, setCategories] = useState([]);
  const [brands, setBrands] = useState([]);
  const [stores, setStores] = useState([]);
  const [products, setProducts] = useState({});

  useEffect(() => {
    getAds();
    getCategories();
    getBrands();
    getStores();
    getProducts();
  }, [cartItems]);

  const getAds = () => {
    axios.get("http://127.0.0.1:8000/ads").then((res) => {
      let ads = res.data;
      ads = ads.filter((e) => e.is_active);
      setTop(ads.find((e) => e.position === "Top"));
      setSide(ads.filter((e) => e.position === "Side"));
    });
  };

  const getCategories = () => {
    axios.get("http://127.0.0.1:8000/products/get-categories").then((res) => {
      let cat = res.data.map((obj) => ({
        ...obj,
        value: obj.categorie_name,
        label: obj.categorie_name,
      }));
      setCategories(cat);
    });
  };

  const getBrands = () => {
    axios.get("http://127.0.0.1:8000/products/get-brands").then((res) => {
      let brand = res.data.map((obj) => ({
        ...obj,
        value: obj.brand,
        label: obj.brand,
      }));
      setBrands(brand);
    });
  };

  const getStores = () => {
    axios.get("http://127.0.0.1:8000/products/get-stores").then((res) => {
      let store = res.data.map(obj => ({
        ...obj,
        value: obj.original_store,
        label: obj.original_store,
      }));
      setStores(store);
    });
  };

  const getProducts = () => {
    let query = Object.fromEntries(new URLSearchParams(window.location.search));
    axios
      .get("http://127.0.0.1:8000/products/", {
        params: { ...query },
      })
      .then(res => {setProducts(res.data);});
  };

  return (
    <>
      {topAd ? <Top ad={topAd} /> : ""}
      <div className="container mx-auto mt-20 flex flex-row gap-8 justify-center">
        <div className="basis-11/12">
          <Filter categories={categories} brands={brands} stores={stores} />
          <Products products={products} cartItems={cartItems} setCart={setCart} counter={counter} setCounter={setCounter} />
        </div>
        <div className="hidden md:block basis-1/12">
          {sideAds.length ? <Side ads={sideAds} /> : ""}
        </div>
      </div>
    </>
  );
};

export default Main;
