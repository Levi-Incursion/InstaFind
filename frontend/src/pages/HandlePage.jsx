import React, {useState, useEffect} from "react";
import { useParams } from 'react-router-dom';
import axios from 'axios';
import '../styles/HomePage.css';

const HandlePage = () => {
  const params = useParams();
  const username = params.username;
  
  const [handle, setHandle] = useState(null)

  useEffect( () =>{
      getData()
  }, [username])

  let getData = async () => {
      let response = await axios.get(`http://127.0.0.1:8000/handles/${username}`)
      // let response = await axios.get(`https://api.linkedin.com/v1/people-search:(people:(id,first-name,last-name,headline,picture-url,industry,positions:(id,title,summary,start-date,end-date,is-current,company:(id,name,type,size,industry,ticker)),educations:(id,school-name,field-of-study,start-date,end-date,degree,activities,notes)),num-results)?first-name=parameter&last-name=parameter`)
      console.log("Response:", response)
      setHandle(response.data)
  }

  return (
    <>
      {handle && (
        <div className = "home">
          <h1>{handle.username} </h1>
          <p>{handle.bio}</p>
        </div>
      )}
    </>
  );
};

export default HandlePage;
