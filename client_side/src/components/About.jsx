import { AiFillShopping, AiFillBell, AiFillCalendar } from "react-icons/ai";

const About = () => {
  return (
    <div className="mb-4 container mx-auto my-8 p-12 border-gray-200 border-2 w-full">
      <h1 className="text-center text-4xl mb-16"> About us</h1>.
      <div className="text-lg font-medium leading-loose flex flex-row gap-8 justify-around">
        <div className="bg-gray-200 h-full w-full p-8  ">
          <AiFillShopping className="h-1/2 w-1/2 mx-auto" />
          <h3 className="text-3xl text-center mb-4">Lorem1</h3>
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorum
            fugit debitis et enim, ea corrupti repellat odit perspiciatis sed
            quod? Harum nulla voluptatibus libero nostrum praesentium minima
            dolores molestias. Non? Ea quidem libero et, iure, hic sint
            consequuntur, labore nesciunt iusto velit sapiente natus sit nobis
            quibusdam aliquam! Architecto quidem obcaecati, nemo natus molestiae
            cupiditate quod! Similique tempora earum commodi.
          </p>
        </div>
        <div className="bg-gray-200 h-full w-full p-8 transition duration-500 ease-in-out border-8 border-orange-500 transform -translate-y-1 scale-110">
          <AiFillBell className="h-1/2 w-1/2 mx-auto" />
          <h3 className="text-3xl text-center mb-4">Lorem2</h3>
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorum
            fugit debitis et enim, ea corrupti repellat odit perspiciatis sed
            quod? Harum nulla voluptatibus libero nostrum praesentium minima
            dolores molestias. Non? Ea quidem libero et, iure, hic sint
            consequuntur, labore nesciunt iusto velit sapiente natus sit nobis
            quibusdam aliquam! Architecto quidem obcaecati, nemo natus molestiae
            cupiditate quod! Similique tempora earum commodi.
          </p>
        </div>
        <div className="bg-gray-200 h-full w-full p-8 ">
          <AiFillCalendar className="h-1/2 w-1/2 mx-auto" />
          <h3 className="text-3xl text-center mb-4">Lorem3</h3>
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorum
            fugit debitis et enim, ea corrupti repellat odit perspiciatis sed
            quod? Harum nulla voluptatibus libero nostrum praesentium minima
            dolores molestias. Non? Ea quidem libero et, iure, hic sint
            consequuntur, labore nesciunt iusto velit sapiente natus sit nobis
            quibusdam aliquam! Architecto quidem obcaecati, nemo natus molestiae
            cupiditate quod! Similique tempora earum commodi.
          </p>
        </div>
      </div>
    </div>
  );
};

export default About;
