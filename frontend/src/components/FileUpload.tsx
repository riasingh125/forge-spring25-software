import React, { useState } from "react";
import styles from "./FileUploadStyles.module.css";

interface FileUploadProps {
  files: File[];
  setFiles: React.Dispatch<React.SetStateAction<File[]>>;
}

const FileUpload: React.FC<FileUploadProps> = ({ files, setFiles }) => {
  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const newFiles = event.target.files ? Array.from(event.target.files) : [];
    setFiles(newFiles);
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
            <ol key={index} className={styles.menuItem}>
              {file.name}
            </ol>
          ))}
        </menu>
      )}
    </div>
  );
};

export default FileUpload;
