import React from "react";
import styles from "./styles.module.css";
import { useFlow as formUseFlow } from "../../context/FormContext";

const BudgetInfo: React.FC = () => {
  const { formData, setFormData } = formUseFlow();

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  return (
    <div className={styles.inputPage}>
      <h1 className={styles.title}>Household and Financial Information</h1>
      <br></br>
      <h2 className={styles.subtitle}>
        Understanding your household size and financial situation helps us
        determine the best healthcare coverage options.
      </h2>
      <br></br>
      <div className={styles.line}></div>
      <br></br>
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
            </div>
            <div className={styles.inputsNextToEachOther}>
              <input
                type="number"
                placeholder="Budget"
                name="budget"
                value={formData.budget}
                onChange={handleChange}
                required
              />
              <input
                type="number"
                placeholder="age"
                name="age"
                value={formData.age}
                onChange={handleChange}
                required
              />
            </div>
          </div>
        </div>
        <br></br>
        <div className={styles.line}></div>
        <br></br>
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
        <br></br>
        <div className={styles.line}></div>
        <br></br>
      </div>
    </div>
  );
};
export default BudgetInfo;
