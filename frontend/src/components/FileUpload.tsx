import React, { useState } from "react";

const FileUpload = () => {
  const [files, setFiles] = useState<File[]>([]); // Define state as an array of File objects

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const newFiles = event.target.files ? Array.from(event.target.files) : [];
    setFiles((prevFileList) => [...prevFileList, ...newFiles]);
    console.log(newFiles);
  };

  return (
    <div>
      <input
        type="file"
        accept="application/pdf"
        multiple
        onChange={handleFileChange}
      />
      <menu>
        {files.map((file, index) => (
          <li key={index}>{file.name}</li>
        ))}
      </menu>
    </div>
  );
};

export default FileUpload;
