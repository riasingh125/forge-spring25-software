import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./styles.module.css";
import { ResultsProps } from "../../App";
import FileUpload from "../FileUpload";
import { useFlow as formUseFlow } from "../../context/FormContext";

const UploadPdfs: React.FC<ResultsProps> = ({ setResults }) => {
  const { formData, setFormData } = formUseFlow();
  const [files, setFiles] = useState<File[]>([]);
  const [planCost, setPlanCost] = useState<number[]>([]);

  // Handle input changes
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  return (
    <div className={styles.inputPage}>
      <h1 className={styles.title}> Plan Details</h1>
      <br></br>
      <h2 className={styles.subtitle}>
        Please upload at least two PDF files of healthcare plans you are
        considering. This will help us compare and recommend the best option for
        you.
      </h2>
      <br></br>
      <div className={styles.line}></div>
      <br></br>
      {/* File Upload */}
      <div className={styles.formGroup}>
        <div className={styles.formLabelGroup}>
          Upload PDFs (select multiple at once!)
        </div>
        <div className={styles.formInputGroup}>
          <FileUpload
            files={files}
            setFiles={setFiles}
            planCost={planCost}
            setPlanCost={setPlanCost}
          />
        </div>
      </div>
      <br></br>
      <div className={styles.line}></div>
      <br></br>
    </div>
  );
};
export default UploadPdfs;
