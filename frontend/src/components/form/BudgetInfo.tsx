import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "../../pages/Input/styles.module.css";
import { ResultsProps } from "../../App";
import FileUpload from "../../components/FileUpload";
import { useFlow } from "../../context/FlowContext";
import { useFlow as formUseFlow } from "../../context/FormContext";

const BudgetInfo: React.FC<ResultsProps> = ({ setResults }) => {
  const navigate = useNavigate();
  const { formData, setFormData } = formUseFlow();
  const [files, setFiles] = useState<File[]>([]);

  // Handle input changes
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  return (
    <div className={styles.inputPage}>
      <h1 className={styles.title}>Household and Financial Information</h1>
      <h2 className={styles.subtitle}>
        Understanding your household size and financial situation helps us
        determine the best healthcare coverage options.
      </h2>
      <div className={styles.line}></div>
      <div className={styles.formContainer}>
        {/* Budget Information */}
        <div className={styles.formGroup}>
          <div className={styles.formLabelGroup}>Budget Information</div>
          <div className={styles.formInputGroup}>
            <div className={styles.inputsNextToEachOther}>
              <input
                type="number"
                placeholder="Salary"
                name="salary"
                value={formData.salary}
                onChange={handleChange}
                required
              />
              <input
                type="number"
                placeholder="# People in Household"
                name="numHousehold"
                value={formData.numHousehold}
                onChange={handleChange}
                required
              />
              <input
                type="number"
                placeholder="Budget"
                name="budget"
                value={formData.budget}
                onChange={handleChange}
                required
              />
            </div>
          </div>
        </div>
        <div className={styles.line}></div>
        <div className={styles.formGroup}>
          <div className={styles.formLabelGroup}>
            List any additional concerns
          </div>
          <div className={styles.formInputGroup}>
            <div>
              <input
                type="text"
                placeholder="Health concerns/additional information"
                name="concerns"
                value={formData.concerns}
                onChange={handleChange}
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
export default BudgetInfo;
