'use client'
import React, { useContext, useEffect, useState } from 'react';
import Select from 'react-select';
import roleContext from "../contexts/roleContext"


const Header = () => {
    const selectContext = useContext(roleContext)
    // const userEmail = localStorage.getItem('komodo');
    const options = [
        { value: 'agent1', label: 'agent1' },
        { value: 'agent2', label: 'agent2' },
        { value: 'agent3', label: 'agent3' },
    ]

    // useEffect(() => {
    //     if (userEmail) {
    //         setOptions([...options, { value: userEmail, label: userEmail }]);
    //         setSelectedOption({ value: userEmail, label: userEmail });
    //     }
    // }, [userEmail]);

    function handleChange(val) {
        selectContext?.setReactSelect(val)
    }

    const style = {
        control: base => ({
            ...base,
            border: "1px solid #CDCDCD",
            boxShadow: "none",
            " &: hover": {
                border: "1px solid #CDCDCD",
            }
        }),
        option: (base, { isSelected }) => ({
            ...base,
            backgroundColor: isSelected ? "#ed76002b" : "#ffffff",
            color: isSelected ? "#333" : "#000",
            " &:hover": {
                backgroundColor: "#ed76008e"
            }
        })
    };

    return (
        <div className="flex justify-between border-b-[0.5px] border-[#CDCDCD] h-[93px] items-center px-5">
            {/* <div>
                <h1 className="text-[15px] leading-[19.05px] font-cerebriregular text-[#495057]">{selectContext?.reactSelect?.value?.toUpperCase()}</h1>
            </div> */}
            <div className='w-[300px]'>
                <Select value={selectContext?.reactSelect} onChange={handleChange} options={options} className='text-[15px] font-cerebriregular' styles={style} />
            </div>
        </div>
    );
};

export default Header;
