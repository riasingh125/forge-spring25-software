import React from "react";
import styles from "./styles.module.css";
import { ResultsProps } from "../../App";
import { useFlow as formUseFlow } from "../../context/FormContext";

const Address: React.FC = () => {
  const { formData, setFormData } = formUseFlow();

  // Handle input changes
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  return (
    <div className={styles.inputPage}>
      <h1 className={styles.title}>Location Details</h1>
      <br></br>
      <h2 className={styles.subtitle}>
        Your location helps us find healthcare plans available in your area.
      </h2>
      <br></br>
      <div className={styles.line}></div>
      <br></br>
      {/* Address Information */}
      <div className={styles.formGroup}>
        <div className={styles.formLabelGroup}>Address</div>
        <div className={styles.formInputGroup}>
          <div className={styles.inputsNextToEachOther}>
            <input
              type="text"
              placeholder="City"
              name="city"
              value={formData.city}
              onChange={handleChange}
              required
            />
            <input
              type="text"
              placeholder="State/Province/Region"
              name="state"
              value={formData.state}
              onChange={handleChange}
              required
            />
          </div>
          <div className={styles.inputsNextToEachOther}>
            <input
              type="text"
              placeholder="Zip Code"
              name="zip"
              value={formData.zip}
              onChange={handleChange}
              required
            />
            <input
              type="text"
              placeholder="Country"
              name="country"
              value={formData.country}
              onChange={handleChange}
              required
            />
          </div>
        </div>
      </div>
      <br></br>
      <div className={styles.line}></div>
      <br></br>
    </div>
  );
};
export default Address;
