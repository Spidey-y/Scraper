
const Top = ({ad}) => {
  return (
    <div className="container mx-auto my-8  border-gray-200 border-4 h-52">
      <img src={`${ad.photo}`} alt={`${ad.title}`} className="h-full w-full" />
    </div>
  );
};

Top.defaultProps = {
  ad: {
    id: -1,
    is_active: true,
    photo: "",
    position: "Top",
    title: "Top Ad",
  },
}


export default Top;
