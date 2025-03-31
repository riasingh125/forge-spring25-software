import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "../../pages/Input/styles.module.css";
import { ResultsProps } from "../../App";
import FileUpload from "../../components/FileUpload";
import { useFlow } from "../../context/FlowContext";
import { useFlow as formUseFlow } from "../../context/FormContext";

const Address: React.FC<ResultsProps> = ({ setResults }) => {
  const navigate = useNavigate();
  const { formData, setFormData } = formUseFlow();
  const [files, setFiles] = useState<File[]>([]);
  const { setHasSubmittedInput } = useFlow();

  // Handle input changes
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  return (
    <div className={styles.inputPage}>
      <h1 className={styles.title}>Location Details</h1>
      <h2 className={styles.subtitle}>
        Your location helps us find healthcare plans available in your area.
      </h2>
      <div className={styles.line}></div>
      <div className={styles.formContainer}>
        <div className={styles.line}></div>
      </div>
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
    </div>
  );
};
export default Address;
