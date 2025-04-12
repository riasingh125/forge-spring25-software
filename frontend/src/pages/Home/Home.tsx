import React from "react";
import { useNavigate } from "react-router-dom";
import styles from "./styles.module.css";
import logo from "../../resources/parcel.png";

const Home: React.FC = ({}) => {
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    navigate("/Input");
  };

  return (
    <div className={styles.welcomePage}>
      <h1 className={styles.title}>Welcome</h1>
      <br></br>
      <h2 className={styles.subtitle}>
        At Parcel, we simplify the insurance selection process. Tell us a little
        about your needs, and we'll help you compare plans to find the perfect
        coverage for you and your family.
      </h2>
      <br></br>
      <ul className={styles.checkmark}>
        <li>Compare multiple plans side-by-side</li>
        <li>Find optimal coverage for your budget</li>
        <li>Expert recommendations tailored to you</li>
      </ul>

      <img src={logo} style={{ width: "150px", height: "150px" }}></img>
      <br></br>
      <button type="button" onClick={handleSubmit} className={styles.navButton}>
        Next
      </button>
    </div>
  );
};
export default Home;
