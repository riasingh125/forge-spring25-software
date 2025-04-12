import React, { useState } from "react";
import styles from "./FileUploadStyles.module.css";

interface FileUploadProps {
  files: File[];
  setFiles: (files: File[]) => void; // change this!
  planCost: number[];
  setPlanCost: (costs: number[]) => void; // change this too
}

const FileUpload: React.FC<FileUploadProps> = ({
  files,
  setFiles,
  planCost,
  setPlanCost,
}) => {
  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const newFiles = event.target.files ? Array.from(event.target.files) : [];
    setFiles(newFiles);
  };

  const handleCostChange = (index: number, value: number) => {
    const updatedCosts = [...planCost];
    updatedCosts[index] = value;
    setPlanCost(updatedCosts);
  };

  return (
    <div>
      <input
        type="file"
        accept="application/pdf"
        multiple
        required
        onChange={handleFileChange}
      />
      {files.length > 0 && (
        <menu className={styles.menuContainer}>
          {files.map((file, index) => (
            <div key={index + file.name}>
              <ol key={index} className={styles.menuItem}>
                {file.name}
              </ol>
              <label htmlFor="cost">Monthly premium</label>
              <input
                type="number"
                id={file.name}
                name="cost"
                required
                onChange={(e) =>
                  handleCostChange(index, Number(e.target.value))
                }
              />
            </div>
          ))}
        </menu>
      )}
    </div>
  );
};

export default FileUpload;
