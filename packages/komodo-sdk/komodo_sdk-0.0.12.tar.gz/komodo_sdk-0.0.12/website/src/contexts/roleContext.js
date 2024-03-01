import { createContext, useEffect, useState } from 'react';
import johnData from "../fakeData/john.json"
import jackData from "../fakeData/jack.json"
import johnsonData from "../fakeData/johnson.json"

import jackDetails from "../fakeData/jackDetails.json"
import johnDetails from "../fakeData/johnDetails.json"
import johnsonDetails from "../fakeData/johnsonDetails.json"
import { ApiGet } from '../API/API_data';
import { API_Path } from '../API/ApiComment';
import { ErrorToast } from "../helpers/Toast"

const Context = createContext("");

export function RoleStore(props) {

    const [reactSelect, setReactSelect] = useState({ value: "agent1", label: "agent1" });
    const [chatDetails, setchatDetails] = useState("");
    const [chatList, setChatList] = useState([]);
    const [user, setUser] = useState("");
    const [agentList, setAgentList] = useState([]);


    useEffect(() => {
        if (user === "") {
            set_user_login_data()
        }
        if (user !== "") {
            agentDetails()
        }
    }, [user])

    const set_user_login_data = () => {
        const userDetails = JSON.parse(localStorage.getItem('komodoUser'))
        setUser(userDetails?.email || "")
    }

    useEffect(() => {
        if (reactSelect?.value) {
            handleJsonData(reactSelect?.value)
        }
    }, [reactSelect?.value])

    const agentDetails = async () => {
        try {
            const agent = await ApiGet(API_Path.agentDetails)
            if (agent?.status === 200) {
                setAgentList(agent?.data?.agents)
                setReactSelect(agent?.data?.agents[0])
            }
        } catch (error) {
            console.log('user details get ::error', error)
            ErrorToast(error?.data?.detail || "Something went wrong")
        }
    }

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
                agentList,
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