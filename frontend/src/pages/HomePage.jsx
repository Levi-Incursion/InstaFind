import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import axios from 'axios';
import '../styles/HomePage.css'

const HomePage = () => {
    const [handles, setHandles] = useState([])
    const [count, setCount] = useState(0)

    useEffect( () =>{
        getData()
    }, []);

    let getData = async (query = '') => {
        try{
            let response = await axios.get(`http://127.0.0.1:8000/handles/?query=${query}`)
            // let response = await axios.get("https://api.linkedin.com/v1/people-search:(people:(id,first-name,last-name,headline,picture-url,industry,positions:(id,title,summary,start-date,end-date,is-current,company:(id,name,type,size,industry,ticker)),educations:(id,school-name,field-of-study,start-date,end-date,degree,activities,notes)),num-results)?first-name=parameter&last-name=parameter")
            // console.log("Response:", response)
            setHandles(response.data)
            setCount(response.data.count)
        } catch (error){
            console.error('Error fetching products:', error);
        }

    }

    let searchData = (e) => {
        e.preventDefault()
        let query = e.target.query.value
        getData(query)
    }

    return (
        <div>
            <h1 className="mt-12 mb-4 text-7xl text-center tracking-tight font-extrabold">InstaFind</h1>
            <h2 className="mt-2 text-3xl text-center mt-4 mb-16 font-semibold">Search Amongst 30 users according to your interest!</h2>
            <div className="mb-12">
                {/* <p className="font-normal text-lg">{count} handles found</p> */}
                <form id='search_form' onSubmit={searchData}>
                    <input type="text" name="query" placeholder="Search Handles...." className="inputC"/>
                    <input type="submit" value="Search" className="inputBtn"/>
                </form>
            </div>
            <div className="flex grid grid-cols-3 gap-7">
                {handles.map((hand,idx) => (
                    <div className="handleCard grid grid-cols-2 w-full rounded-lg" key={idx}>
                        <div className="imgC ">
                            <Link to={`/handles/${hand.username}`}><img className="imgClass" src={hand.profile_pic} /></Link>
                        </div>
                        <div className="flex textC flex-col justify-self-center content-center rounded-lg p-8">
                            <a className="aLink underline text-xl" href={'https://www.instagram.com/' + hand.username + '/'} target="_blank">@{hand.username}</a>
                            <p className="font-bold text-lg">{hand.category_name}</p>
                            <p className="font-normal text-lg">Followers: {hand.followers}</p>
                            <p className="font-normal text-lg">Posts: {hand.posts}</p>
                        </div>
                        
                    </div>
                ))}
            </div>

            <footer className="footer mt-12 text-center items-center footer-center border-t border-slate-200 bg-base-300 text-base-content p-4">
                <aside>
                    <p className="text-sm ">Copyright © {new Date().getFullYear()} - All right reserved by Kirtan Mevada</p>
                </aside>
            </footer>

        {/* <footer class="w-full p-8">
        <p class="block mb-4 text-sm text-center text-slate-500 md:mb-0 border-t border-slate-200 mt-4 pt-4">
            Copyright © 2024&nbsp; 
            <a href="https://material-tailwind.com/" target="_blank" rel="noreferrer">Material Tailwind</a>.
        </p>
        </footer> */}
        </div>
    );
};

export default HomePage;