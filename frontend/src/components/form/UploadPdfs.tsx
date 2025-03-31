import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "../../pages/Input/styles.module.css";
import { ResultsProps } from "../../App";
import FileUpload from "../../components/FileUpload";
import { useFlow as formUseFlow } from "../../context/FormContext";

const UploadPdfs: React.FC<ResultsProps> = ({ setResults }) => {
  const { formData, setFormData } = formUseFlow();
  const [files, setFiles] = useState<File[]>([]);

  // Handle input changes
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  return (
    <div className={styles.inputPage}>
      <h1 className={styles.title}> Plan Details</h1>
      <h2 className={styles.subtitle}>
        Please upload at least two PDF files of healthcare plans you are
        considering. This will help us compare and recommend the best option for
        you.
      </h2>
      <div className={styles.line}></div>
      {/* File Upload */}
      <div className={styles.formGroup}>
        <div className={styles.formLabelGroup}>
          Upload PDFs (select multiple at once!)
        </div>
        <div className={styles.formInputGroup}>
          <FileUpload files={files} setFiles={setFiles} />
        </div>
      </div>
      <div className={styles.line}></div>
      <br></br>
    </div>
  );
};
export default UploadPdfs;
