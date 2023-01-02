import React from "react";

const Ad = ({ ad }) => {
  return (
    <>
      <div className="h-72  w-72 border-2 bg-orange-500">
        <img src={`${ad.photo}`} alt={`${ad.title}`} className="h-full w-full" />
      </div>
    </>
  );
};

Ad.defaultProps = {
  ad: {
    id: -1,
    is_active: true,
    photo: "",
    position: "Side",
    title: "Side Ad",
  },
};

export default Ad;
