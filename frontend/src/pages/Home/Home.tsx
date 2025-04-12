import React from "react";
import { useNavigate } from "react-router-dom";
import styles from "../Input/styles.module.css";
import { ResultsProps } from "../../App";
import logo from "../../resources/parcel.png";

const Home: React.FC<ResultsProps> = ({}) => {
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    navigate("/Input");
  };

  return (
    <div className={styles.inputPage}>
      <h1 className={styles.title}>Welcome</h1>
      <h2 className={styles.subtitle}>
        Let us help you find the right insurance plan. We'll need a few details
        to get started.
      </h2>
      <img src={logo} style={{ width: "150px", height: "150px" }}></img>
      <div className={styles.subtitle}></div>
      <button type="button" onClick={handleSubmit} className={styles.navButton}>
        Next
      </button>
    </div>
  );
};
export default Home;
