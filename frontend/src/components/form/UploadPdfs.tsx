import React, { useState } from "react";
import styles from "./styles.module.css";
import { ResultsProps } from "../../App";
import FileUpload from "../FileUpload";
import { useFlow as formUseFlow } from "../../context/FormContext";

const UploadPdfs: React.FC = () => {
  const { formData, setFormData } = formUseFlow();
  const files = formData.files || [];
  const costs = formData.costs || [];

  const updateFiles = (newFiles: File[]) => {
    setFormData({ ...formData, files: newFiles });
  };

  const updatePlanCost = (newCosts: number[]) => {
    setFormData({ ...formData, costs: newCosts });
  };

  // Handle input changes
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  return (
    <div className={styles.inputPage}>
      <h1 className={styles.title}> Plan Details</h1>
      <br />
      <h2 className={styles.subtitle}>
        Please upload at least two PDF files of healthcare plans you are
        considering. This will help us compare and recommend the best option for
        you.
      </h2>
      <br />
      <div className={styles.line}></div>
      <br />
      {/* File Upload */}
      <div className={styles.formGroup}>
        <div className={styles.formLabelGroup}>
          Upload PDFs (select multiple at once!)
        </div>
        <div className={styles.formInputGroup}>
          <FileUpload
            files={files}
            setFiles={updateFiles}
            planCost={costs}
            setPlanCost={updatePlanCost}
          />
        </div>
      </div>
      <br />
      <div className={styles.line}></div>
      <br />
    </div>
  );
};

export default UploadPdfs;
