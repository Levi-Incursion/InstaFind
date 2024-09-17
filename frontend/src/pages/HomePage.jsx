import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import axios from 'axios';
import '../styles/HomePage.css'

const HomePage = () => {
    const [handles, setHandles] = useState([])

    useEffect( () =>{
        getData()
    }, [])

    let getData = async () => {
        let response = await axios.get("http://127.0.0.1:8000/handles/")
        // let response = await axios.get("https://api.linkedin.com/v1/people-search:(people:(id,first-name,last-name,headline,picture-url,industry,positions:(id,title,summary,start-date,end-date,is-current,company:(id,name,type,size,industry,ticker)),educations:(id,school-name,field-of-study,start-date,end-date,degree,activities,notes)),num-results)?first-name=parameter&last-name=parameter")
        console.log("Response:", response)
        setHandles(response.data)
    }

    return (
        <div>
            <h1>Homies Page1</h1>
            <div>
                {handles.map((hand,idx) => (
                    <div key={idx}>
                        {hand.username}
                        <Link to={`/handles/${hand.username}`}>Click</Link>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default HomePage;