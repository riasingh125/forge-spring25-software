import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "../../pages/Input/styles.module.css";
import { ResultsProps } from "../../App";
import FileUpload from "../../components/FileUpload";
import { useFlow } from "../../context/FlowContext";
import { useFlow as formUseFlow } from "../../context/FormContext";

const ContactInfo: React.FC<ResultsProps> = ({ setResults }) => {
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
      <h1 className={styles.title}>Personal Information</h1>
      <h2 className={styles.subtitle}>
        Let's start with some basic information to help us tailor your
        healthcare plan options.
      </h2>
      <div className={styles.line}></div>
      <div className={styles.formContainer}>
        {/* Contact Information */}
        <div className={styles.formGroup}>
          <div className={styles.formLabelGroup}>Contact Information</div>
          <div className={styles.formInputGroup}>
            <div className={styles.inputsNextToEachOther}>
              <input
                type="text"
                placeholder="First Name"
                name="firstName"
                value={formData.firstName}
                onChange={handleChange}
                required
              />
              <input
                type="text"
                placeholder="Last Name"
                name="lastName"
                value={formData.lastName}
                onChange={handleChange}
                required
              />
            </div>
            <div className={styles.inputsNextToEachOther}>
              <input
                type="email"
                placeholder="Email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                required
              />
            </div>
          </div>
        </div>
        <div className={styles.line}></div>
        
      </div>
    </div>
  );
};
export default ContactInfo;
