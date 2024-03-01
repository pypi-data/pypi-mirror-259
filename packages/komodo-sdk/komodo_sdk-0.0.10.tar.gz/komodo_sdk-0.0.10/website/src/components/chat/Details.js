import React, { useContext, useEffect, useState } from 'react'
import PrimaryLayout from '../../layout/PrimaryLayout'
import profile from '../../images/profile.png'
import wave from '../../images/wave.png'
import send from '../../images/send.png'
import dots from '../../images/dots.png'
import roleContext from "../../contexts/roleContext"

const Details = () => {
    const [prompt, setPrompt] = useState('');
    const [text, setText] = useState('');
    const [chatRes, setChatRes] = useState('');
    const [AllChatData, setAllChatData] = useState('');
    const [newChat, setNewChat] = useState(false);
    const [res, setRes] = useState(false);
    const [setting, setSetting] = useState(false);
    const context = useContext(roleContext)

    const handleUpdate = (data) => {
        setSetting(data);
    };

    const sendPrompt = async () => {
        setNewChat(true)
        setText(prompt)
        setPrompt('')
    };

    const ChatData = async (val) => {
        setAllChatData(val);
        setChatRes(val.enhanced_prompt);
        setNewChat(false)
        setRes(false)
    };


    useEffect(() => {
        if (context?.chatDetails) {
            ChatData(context?.chatDetails)
        }
    }, [context?.chatDetails])


    const handleKeyPress = (e) => {
        if (e.key === 'Enter') {
            sendPrompt();
        }
    };

    return (
        <PrimaryLayout onUpdate={handleUpdate} setNewChat={setNewChat}>
            {/* <div className="flex"> */}
            <div className="w-full">
                {/* <div className={`${imageClicked ? 'w-[95%]' : 'w-full'}`}> */}
                {/* <div className={`${imageClicked ? 'w-[95%]' : 'w-9/12'}`}> */}
                <div className='mt-10 ms-7 pe-8 h-[calc(100vh-218px)] overflow-auto scrollbar'>
                    {newChat === true ?
                        <div className='mb-10'>
                            {text && <div className='flex gap-5 items-center'>
                                <div>
                                    <img src={profile} alt="profile" className='w-[30px] h-[30px]' />
                                </div>
                                <div className='text-[16px] font-cerebriregular rounded-md bg-[#4EAC6D1A] px-4 py-3 text-[#495057]'>
                                    {text}
                                </div>
                            </div>
                            }

                            <div>
                                <div className='mt-10 flex gap-5'>
                                    {res === true ?
                                        <div>
                                            <img src={wave} alt="wave" className='w-[30px] h-[30px]' />
                                        </div>
                                        : ""}
                                </div>
                            </div>

                        </div>
                        :
                        <div className='mb-10'>
                            <div div className='flex gap-5 items-center'>
                                <div>
                                    <img src={profile} alt="profile" className='w-[30px] h-[30px]' />
                                </div>
                                <div className='text-[16px] font-cerebriregular rounded-md bg-[#d38e492b] px-4 py-3 text-[#495057]'>
                                    {AllChatData?.question?.text}
                                </div>
                            </div>

                            <div>
                                <div className='mt-10 flex gap-5'>
                                    <div>
                                        <img src={wave} alt="wave" className='w-[30px] h-[30px]' />
                                    </div>
                                    <div className='w-fit text-[#495057]'>
                                        <p className='font-cerebriregular text-[15px] leading-[34px] cursor-pointer text-justify'

                                            dangerouslySetInnerHTML={{ __html: chatRes?.replace(/\n/g, '<br>') }}></p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    }
                </div>
                <div>
                    <div className="flex gap-4 items-center ps-6 py-5 border-t-[0.5px] border-[#CDCDCD] w-full pe-8">
                        <div className='w-[14px]'>
                            <img src={dots} alt="send" />
                        </div>
                        <input type="text" placeholder="Ask me anything..." value={prompt} onChange={(e) => setPrompt(e.target.value)} onKeyPress={handleKeyPress} className="w-[892px] h-[43px] border border-[#CFD4D8] rounded-md px-4 text-[14px] font-cerebriregular leading-[17.78px] outline-none" />
                        <img src={send} alt="send" onClick={sendPrompt} className='cursor-pointer' />
                    </div>
                </div>
            </div>
            {/* </div> */}
        </PrimaryLayout>
    )
}

export default Details