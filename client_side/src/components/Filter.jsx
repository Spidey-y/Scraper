import React from "react";
import { useState } from "react";

import Select from "react-select";
import makeAnimated from "react-select/animated";

import { VscFilterFilled } from "react-icons/vsc";
import { BsSearch } from "react-icons/bs";

const animatedComponents = makeAnimated();

let options = [
  { value: "chocolate", label: "Chocolate" },
  { value: "strawberry", label: "Strawberry" },
  { value: "vanilla", label: "Vanilla" },
];

const Filter = () => {
  let [filter, setFilter] = useState(true);

  const handleClick = () => {
    setFilter(!filter);
    console.log(filter);
  };

  return (
    <div className="h-12 grid grid-col-12 grid-row-3 gap-3 mx-4">
      <button
        className="btn btn-outline btn-accent  col-span-1 row-start-1 justify-self-start w-40"
        onClick={handleClick}
      >
        <VscFilterFilled className="h-5 w-5 mx-2" />
        Filter
      </button>

      <div className="form-control col-span-11 row-start-1">
        <div className="input-group ">
          <input
            type="text"
            placeholder="Search…"
            className="input input-bordered grow"
          />
          <button className="btn btn-square">
            <BsSearch className="h-5 w-5 bold" />
          </button>
        </div>
      </div>
      <div
        className={`my-4 form-control col-span-12 col-start-1 row-start-2 justify-evenly grid-col-12 grid-row-4 gap-x-2 ${
          filter ? "hidden" : "grid"
        } bg-gray-200 bg-opacity-50 p-4 rounded-xl `}
      >
        <div className="my-4 form-control col-span-10 col-start-1 col-end-10 row-span-3">
          <Select
            closeMenuOnSelect={true}
            components={animatedComponents}
            options={options}
            placeholder={"Category"}
            className=" mx-4 my-2 h-14 w-full"
          />
          <Select
            closeMenuOnSelect={false}
            components={animatedComponents}
            isMulti
            options={options}
            placeholder={"Brand"}
            className=" mx-4 my-2 h-14 w-full"
          />
          <Select
            closeMenuOnSelect={false}
            components={animatedComponents}
            isMulti
            options={options}
            placeholder={"Store"}
            className=" mx-4 my-2 h-14 w-full"
          />
        </div>

        <div className="my-4 px-8 form-control col-span-2 col-start-10 justify-self-end row-span-3 gap-6">
          <div className="form-control  left-0">
            <label className="input-group">
              <span className="">Min price</span>
              <input type="number" className="input input-bordered" />
              <span>DZD</span>
            </label>
          </div>

          <div className="form-control">
            <label className="input-group">
              <span className="">Max price</span>
              <input type="number" className="input input-bordered" />
              <span>DZD</span>
            </label>
          </div>

          <div className="form-control">
            <label className="label cursor-pointer">
              <span className="label-text text-xl">Staff pick</span>
              <input type="checkbox" checked className="checkbox" />
            </label>
          </div>
        </div>
        <button className="btn btn-outline btn-accent w-40 justify-self-end col-span-1 col-start-11 row-start-4">
          <BsSearch className="h-5 w-5 mx-2" /> Search...
        </button>
      </div>
    </div>
  );
};

export default Filter;
