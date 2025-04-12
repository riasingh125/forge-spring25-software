import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./styles.module.css";
import { ResultsProps } from "../../App";
import Box from "@mui/material/Box";
import FileUpload from "../../components/FileUpload";
import { useFlow } from "../../context/FlowContext";
import { useFlow as formUseFlow } from "../../context/FormContext";
import Typography from "@mui/material/Typography";
import Slider from "@mui/material/Slider";
import MuiInput from "@mui/material/Input";
import Select, { SelectChangeEvent } from "@mui/material/Select";
import MenuItem from "@mui/material/MenuItem";

const ContactInfo: React.FC<ResultsProps> = ({ setResults }) => {
  const navigate = useNavigate();
  const { formData, setFormData } = formUseFlow();
  const [files, setFiles] = useState<File[]>([]);
  const [selectedOption, setSelectedOption] = useState("");
  const [dropdownError, setDropdownError] = useState(false);

  // Handle input changes
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleDropdownChange = (event: SelectChangeEvent<string>) => {
    setSelectedOption(event.target.value);
    setDropdownError(false);
  };

  return (
    <div className={styles.inputPage}>
      <h1 className={styles.title}>Personal Information</h1>
      <br></br>
      <h2 className={styles.subtitle}>
        Let's start with some basic information to help us tailor your
        healthcare plan options.
      </h2>
      <br></br>
      <div className={styles.line}></div>
      <br></br>
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
            <br></br>
          </div>
        </div>
        {/* User Experience */}
        <div className={styles.line}></div>
        <br></br>
        <div className={styles.formGroup}>
          <div className={styles.formLabelGroup}>
            Select your level of familiarity with healthcare jargon
          </div>
          <div className={styles.formInputGroup}>
            <div className={styles.inputsNextToEachOther}>
              {/* Dropdown Selection */}
              <Box>
                <Select
                  value={selectedOption}
                  onChange={handleDropdownChange}
                  displayEmpty
                  fullWidth
                  error={dropdownError}
                  className={styles.customDropdown}
                >
                  <MenuItem value="" disabled>
                    Select an option
                  </MenuItem>
                  <MenuItem value="Option 1">Unfamiliar</MenuItem>
                  <MenuItem value="Option 2">Moderately Familiar</MenuItem>
                  <MenuItem value="Option 3">Very Familiar</MenuItem>
                </Select>
              </Box>
            </div>
          </div>
        </div>
        <br></br>
        <div className={styles.line}></div>
      </div>
    </div>
  );
};
export default ContactInfo;
