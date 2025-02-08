import React from "react";
import styles from "./styles.module.css";

const Input: React.FC = () => (
  <div>
    <h1>Welcome</h1>
    <h3>
      Let's get you set up to compare the best insurance plans. We'll need a few
      details to get started.
    </h3>
    <hr></hr>
    <div className={styles.formContainer}>
      <form className={styles.form}>
        <div className={styles.formGroup}>
          <div className={styles.formLabelGroup}>Contact Information</div>
          <div className={styles.formInputGroup}>
            <div>
              <input type="text" placeholder="first name" name="firstName" />
              <input type="text" placeholder="last name" name="lastName" />
            </div>
            <div>
              <input type="email" placeholder="email" name="email" />
            </div>
          </div>
        </div>
        <hr></hr>
        <div className={styles.formGroup}>
          <div className={styles.formLabelGroup}>Address</div>
          <div className={styles.formInputGroup}>
            <div>
              <input type="text" placeholder="city" name="city" />
              <input
                type="text"
                placeholder="state/providince/region"
                name="state"
              />
            </div>
            <div>
              <input type="text" placeholder="zip code" name="zip" />
              <input type="text" placeholder="country" name="country" />
            </div>
          </div>
        </div>
        <hr></hr>
        <div className={styles.formGroup}>
          <div className={styles.formLabelGroup}>Address</div>
          <div className={styles.formInputGroup}>
            <div>
              <input type="text" placeholder="city" name="city" />
              <input
                type="text"
                placeholder="state/providince/region"
                name="state"
              />
            </div>
            <div>
              <input type="text" placeholder="zip code" name="zip" />
              <input type="text" placeholder="country" name="country" />
            </div>
          </div>
        </div>
        <hr></hr>
        <div className={styles.formGroup}>
          <div className={styles.formLabelGroup}>Budget Information</div>
          <div className={styles.formInputGroup}>
            <div>
              <input type="text" placeholder="salary" name="salary" />
              <input
                type="text"
                placeholder="# people in household"
                name="numHousehold"
              />
              <input type="text" placeholder="budget" name="budget" />
            </div>
            <div>
              <input
                type="text"
                placeholder="list and health concerned/additional information here"
                name="concerns"
              />
            </div>
          </div>
        </div>
        <hr></hr>
      </form>
    </div>
  </div>
);

export default Input;
