import React from 'react';
import Side from './Ads/Side';
import Filter from './Filter';
import Products from './Products';

const Main = () => {
  return (
    <div className='container mx-auto mt-20 flex flex-row justify-between'>
        <div className="basis-11/12">
            <Filter />
            <Products />
        </div>
        <Side className="basis-1/12 right-0" />
    </div>
  )
}

export default Main