import React from "react";
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
        <table className={styles.fileTable}>
          <thead>
            <tr>
              <th>File</th>
              <th>Monthly Premium ($)</th>
            </tr>
          </thead>
          <tbody>
            {files.map((file, index) => (
              <tr key={index + file.name}>
                <td>{file.name}</td>
                <td>
                  <input
                    type="number"
                    name={`cost-${index}`}
                    id={`cost-${index}`}
                    required
                    min={0}
                    placeholder="e.g. 200"
                    value={planCost[index] ?? ""}
                    onChange={(e) =>
                      handleCostChange(index, Number(e.target.value))
                    }
                    className={styles.inputField}
                  />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default FileUpload;
