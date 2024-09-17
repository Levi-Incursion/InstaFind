import React from "react";
import { useNavigate } from "react-router-dom";
import '../styles/PageNotFound.css';

const PageNotFound = () => {
  const navigate = useNavigate();

  const HandleClick = () => {
      navigate('/');
  };

  return (
    <div className="notFound">
      <h1>404 Error, Bad Request</h1>
      <h2 className="c_h2">Page Not Found</h2>
      <button className="button-74" onClick={HandleClick}>Go back to Home</button>
    </div>
  );
};

export default PageNotFound;
