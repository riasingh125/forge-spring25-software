import React, { useState } from "react";
import styles from "./styles.module.css";
import Box from "@mui/material/Box";
import { useFlow as formUseFlow } from "../../context/FormContext";
import Select, { SelectChangeEvent } from "@mui/material/Select";
import MenuItem from "@mui/material/MenuItem";

const ContactInfo: React.FC = () => {
  const { formData, setFormData } = formUseFlow();
  const [dropdownError, setDropdownError] = useState(false);

  // Handle input changes
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleDropdownChange = (event: SelectChangeEvent<string>) => {
    const value = event.target.value;
    setFormData({ ...formData, familiarity: value });
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
            <div className={styles.inputsNextToEachOther}>
              <input
                type="phone"
                placeholder="Phone Number"
                name="phone"
                value={formData.phone}
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
                  value={formData.familiarity}
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
