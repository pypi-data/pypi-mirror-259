import React from 'react'
import { useNavigate } from 'react-router-dom';
import * as Yup from 'yup';
import { useFormik } from 'formik';
import Sidebar from '../components/Sidebar';
import { ApiGet } from '../API/API_data';
import { ErrorToast } from '../helpers/Toast';

const Login = () => {
    const navigate = useNavigate()

    const validationSchema = Yup.object().shape({
        email: Yup.string().email('Invalid email').required('Email is required'),
        password: Yup.string().required('Password is required'),
    });

    const formik = useFormik({
        initialValues: {
            email: '',
            password: '',
        },
        validationSchema: validationSchema,
        onSubmit: async (values) => {
            try {
                const checkLogin = await ApiGet("/user-profile", values.email)
                console.log(checkLogin, 'checkLogin')
                if (checkLogin?.status === 200) {
                    localStorage.setItem('komodo', values.email);
                    navigate('/chat');
                    localStorage.setItem("komodoUser", JSON.stringify(checkLogin.data))
                }
            } catch (error) {
                console.log('user details get ::error', error)
                ErrorToast(error?.data?.detail || "Something went wrong")
            }
            // navigate('/chat');
            // localStorage.setItem('komodo', values.email);
            // localStorage.setItem("komodoUser", JSON.stringify({ "email": "ryan@komodoapp.ai", "guid": "1d3b093a-9041-4189-b86a-27027ef17207", "name": "Ryan Oberoi" }))
        },
    });

    return (
        <>
            <div className="grid grid-rows-1">
                <div className="grid grid-cols-12">
                    <div className='col-span-1'>
                        <Sidebar />
                    </div>
                    <div className='col-span-11'>
                        <form onSubmit={formik.handleSubmit} className='flex flex-col justify-center items-center h-[calc(100vh-57px)]'>
                            <div>
                                <h1 className='text-[#495057] text-[23px] font-cerebri leading-[30px]'>Email</h1>
                                <input
                                    type="text"
                                    placeholder='Enter Email'
                                    name="email"
                                    value={formik.values.email}
                                    onChange={formik.handleChange}
                                    onBlur={formik.handleBlur}
                                    className='text-[#495057] text-[16px] font-cerebriregular leading-[20.32px] border border-[#CFD4D8] rounded-md w-[513px] h-[50px] px-3 outline-none mt-1'
                                />
                                {formik.touched.email && formik.errors.email && <p className="text-red-500 mt-2">{formik.errors.email}</p>}
                            </div>
                            <div className='mt-5'>
                                <h1 className='text-[#495057] text-[23px] font-cerebri leading-[30px]'>Password</h1>
                                <input
                                    type="password"
                                    placeholder='Enter Password'
                                    name="password"
                                    value={formik.values.password}
                                    onChange={formik.handleChange}
                                    onBlur={formik.handleBlur}
                                    className='text-[#495057] text-[16px] font-cerebriregular leading-[20.32px] border border-[#CFD4D8] rounded-md w-[513px] h-[50px] px-3  outline-none mt-1'
                                />
                                {formik.touched.password && formik.errors.password && <p className="text-red-500 mt-2">{formik.errors.password}</p>}
                            </div>
                            <button type='submit' className='text-[#fff] text-[19px] font-cerebri leading-[24.13px] text-center bg-[#ED7600] w-[513px] h-[52px]  rounded-md mt-10'>Log In</button>
                        </form>
                    </div>
                </div>
            </div>
        </>
    )
}

export default Login