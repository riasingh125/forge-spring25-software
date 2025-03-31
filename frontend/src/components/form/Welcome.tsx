import React from "react";
import styles from "../../pages/Input/styles.module.css";
import { ResultsProps } from "../../App";
import logo from "../../resources/parcel.png";

const Welcome: React.FC<ResultsProps> = ({ setResults }) => {
  return (
    <div className={styles.inputPage}>
      <h1 className={styles.title}>Welcome</h1>
      <h2 className={styles.subtitle}>
        Let us help you find the right insurance plan. We'll need a few details
        to get started.
      </h2>
      <img src={logo} style={{ width: "150px", height: "150px" }}></img>
      <div className={styles.subtitle}></div>
    </div>
  );
};
export default Welcome;
