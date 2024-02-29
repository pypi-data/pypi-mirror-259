import { createContext, useEffect, useState } from 'react';
import johnData from "../fakeData/john.json"
import jackData from "../fakeData/jack.json"
import johnsonData from "../fakeData/johnson.json"

import jackDetails from "../fakeData/jackDetails.json"
import johnDetails from "../fakeData/johnDetails.json"
import johnsonDetails from "../fakeData/johnsonDetails.json"

const Context = createContext("");

export function RoleStore(props) {
    // let token = localStorage.getItem("komodo");
    const [reactSelect, setReactSelect] = useState({ value: "agent1", label: "agent1" });
    const [chatDetails, setchatDetails] = useState("");
    const [chatList, setChatList] = useState([]);
    const [user, setUser] = useState("");
    useEffect(() => {
        if (reactSelect?.value) {
            handleJsonData(reactSelect?.value)
        }
    }, [reactSelect?.value])
    // useEffect(() => {
    //     if (![null, undefined, ''].includes(token)) {
    //         handleJsonData(reactSelect?.value)
    //     }
    // }, [token, reactSelect?.value])

    const handleJsonData = (value) => {
        switch (reactSelect?.value) {
            case "agent1":
                setChatList(johnData)
                setchatDetails(johnDetails)
                break;
            case "agent2":
                setChatList(jackData)
                setchatDetails(jackDetails)
                break;
            case "agent3":
                setChatList(johnsonData)
                setchatDetails(johnsonDetails)
                break;
        }
    }
    return (
        <Context.Provider
            value={{
                reactSelect,
                chatList,
                chatDetails,
                user,
                ...{
                    setReactSelect,
                    setUser,
                },
            }}
        >
            {props.children}
        </Context.Provider>
    )
}

export default Context;