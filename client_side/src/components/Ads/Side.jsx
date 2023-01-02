import Ad from "./Ad";

const Side = ({ads}) => {
  return (
    <div className="float-right flex flex-col gap-4 ">
      {ads.map((ad)=> 
        <Ad ad={ad} key={ad.id} />
        )}
    </div>
  );
};

export default Side;
