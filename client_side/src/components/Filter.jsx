import { useState } from "react";
import Select from "react-select";
import makeAnimated from "react-select/animated";

import { VscFilterFilled } from "react-icons/vsc";
import { BsSearch } from "react-icons/bs";

const Filter = ({ categories, brands, stores }) => {
  const animatedComponents = makeAnimated();

  const [open, setFilter] = useState(true);
  const handleClick = () => {
    setFilter(!open);
  };

  const [query, setQuery] = useState({});
  const [search, setSearch] = useState("");
  const [minPrice, setMin] = useState("");
  const [maxPrice, setMax] = useState("");
  const [checked, setChecked] = useState(false);

  const setQueryParams = () => {
    let params = new URLSearchParams();
    for (const key in query) {
      if (Object.hasOwnProperty.call(query, key)) {
        Array.isArray(query[`${key}`])
          ? query[`${key}`].forEach((e) => {
              params.append(key, e);
            })
          : params.append(key, query[`${key}`]);
      }
    }
    window.location.search = params.toString();
  };

  const handleCheck = () => {
    setChecked(!checked);
  };

  return (
    <div className="grid grid-col-12 grid-row-3 gap-3 mx-4">
      <button
        className="btn btn-outline btn-accent  col-span-1 row-start-1 justify-self-start w-40"
        onClick={handleClick}
      >
        <VscFilterFilled className="h-5 w-5 mx-2" />
        Filter
      </button>

      <div className="form-control col-span-11 md:row-start-1">
        <div className="input-group ">
          <input
          autoFocus
            type="text"
            placeholder="Search…"
            className="input input-bordered grow focus:border-0"
            value={search}
            onChange={e => {
              setSearch(e.target.value);
              setQuery({...query, search: e.target.value})
            }}
          />
          <button className="btn btn-square" onClick={setQueryParams}>
            <BsSearch className="h-5 w-5 bold" />
          </button>
        </div>
      </div>
      <form
        onSubmit={(e) => {
          e.preventDefault();
          setQueryParams();
        }}
        className={`my-4 form-control col-span-12 col-start-1 row-start-2 justify-evenly grid-col-12 grid-row-4 gap-x-2 ${
          open ? "hidden" : "grid"
        } bg-gray-200 bg-opacity-50 p-4 rounded-xl `}
      >
        <div className="form-control col-span-10 col-start-1 col-end-10 row-span-3">
          <Select
            closeMenuOnSelect={true}
            components={animatedComponents}
            options={categories}
            placeholder={"Category"}
            className=" mx-4 my-4 w-full"
            onChange={(e) => setQuery({ ...query, categorie__categorie_name: e.value })}
          />
          <Select
            closeMenuOnSelect={false}
            components={animatedComponents}
            isMulti
            options={brands}
            placeholder={"Brand"}
            className=" mx-4 my-4 w-full"
            onChange={(e) =>
              setQuery({ ...query, brand: e.map((el) => el.value) })
            }
          />
          <Select
            closeMenuOnSelect={false}
            components={animatedComponents}
            isMulti
            options={stores}
            placeholder={"Store"}
            className=" mx-4 my-4 w-full"
            onChange={(e) =>
              setQuery({ ...query, original_store: e.map((el) => el.value) })
            }
          />
        </div>

        <div className="my-4 px-8 form-control col-span-2 col-start-10 justify-self-end row-span-3 gap-6">
          <div className="form-control  left-0">
            <label className="input-group">
              <span className="">Min price</span>
              <input
                type="number"
                className="input input-bordered"
                value={minPrice}
                min={0}
                max={maxPrice}
                onChange={(e) => {
                  setMin(e.target.value);
                  setQuery({ ...query, price__gte: e.target.value });
                }}
              />
              <span>DZD</span>
            </label>
          </div>

          <div className="form-control">
            <label className="input-group">
              <span className="">Max price</span>
              <input
                type="number"
                className="input input-bordered"
                value={maxPrice}
                min={minPrice}
                onChange={(e) => {
                  setMax(e.target.value);
                  setQuery({ ...query, price__lte: e.target.value });
                }}
              />
              <span>DZD</span>
            </label>
          </div>

          <div className="form-control">
            <label className="label cursor-pointer">
              <span className="label-text text-xl">Staff pick</span>
              <input
                type="checkbox"
                className="checkbox"
                checked={checked}
                onChange={() => {
                  handleCheck();
                  setQuery({ ...query, staff_pick: !checked || null });
                }}
              />
            </label>
          </div>
        </div>
        <button className="btn btn-outline btn-accent w-40 justify-self-end col-span-1 col-start-11 row-start-4">
          <BsSearch className="h-5 w-5 mx-2" /> Search...
        </button>
      </form>
    </div>
  );
};

export default Filter;
