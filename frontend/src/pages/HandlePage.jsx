import React, {useState, useEffect} from "react";
import { useParams, useNavigate, Link } from 'react-router-dom';
import axios from 'axios';
import '../styles/HomePage.css';
import '../styles/PageNotFound.css';

const HandlePage = () => {
  const params = useParams();
  const username = params.username;
  
  const [handle, setHandle] = useState(null)

  useEffect( () =>{
      getData()
  }, [username])

  const navigate = useNavigate();

  const HandleClick = () =>{
    navigate('/');
  }
  let getData = async () => {
      let response = await axios.get(`http://127.0.0.1:8000/handles/${username}`)
      // let response = await axios.get(`https://api.linkedin.com/v1/people-search:(people:(id,first-name,last-name,headline,picture-url,industry,positions:(id,title,summary,start-date,end-date,is-current,company:(id,name,type,size,industry,ticker)),educations:(id,school-name,field-of-study,start-date,end-date,degree,activities,notes)),num-results)?first-name=parameter&last-name=parameter`)
      console.log("Response:", response)
      setHandle(response.data)
  }

  return (
    <>
      {handle && (
        <div>
          <h1 className="text-center mb-3">{handle.username}</h1>
          <div className="handleCard grid grid-cols-2 w-full rounded-lg">
                <div className="imgC ">
                    <Link to={`/handles/${handle.username}`}><img className="imgClass" src={handle.profile_pic} /></Link>
                </div>
                <div className="flex textC flex-col justify-self-center content-center rounded-lg p-8">
                    <a className="aLink underline text-xl" href={'https://www.instagram.com/' + handle.username + '/'} target="_blank">@{handle.username}</a>
                    <p className="font-bold text-lg">{handle.category_name}</p>
                    <p className="font-normal text-lg">Rank in the World: {handle.rank}</p>
                    <p className="font-normal text-lg">Followers: {handle.followers}</p>
                    <p className="font-normal text-lg">Posts: {handle.posts}</p>
                    <p className="font-normal text-lg">Avg Likes: {handle.avg_likes}</p>
                </div>
          </div>
          <button className="button-74 flex flex-col justify-self-center mt-5" onClick={HandleClick}>Go back to Home</button>
        </div>
      )}
    </>
  );
};

export default HandlePage;
