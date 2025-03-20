import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./styles.module.css";
import { ResultsProps } from "../../App";
import FileUpload from "../../components/FileUpload";

const Input: React.FC<ResultsProps> = ({ setResults }) => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    firstName: "",
    lastName: "",
    email: "",
    city: "",
    state: "",
    zip: "",
    country: "",
    salary: "",
    numHousehold: "",
    budget: "",
    concerns: "",
  });
  const [errors, setErrors] = useState<{ [key: string]: string }>({});
  const [isSubmitting, setIsSubmitting] = useState(false);

  // Handle input changes
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  // Handle form submission
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!validate()) {
      console.log(errors);
      return;
    }
    try {
      navigate("/Rankings");
    } catch (error) {
      setErrors((prevErrors) => ({
        ...prevErrors,
        submit: "Submission failed. Please try again.",
      }));
    } finally {
      setIsSubmitting(false);
    }
  };

  // Validation function
  const validate = () => {
    const newErrors: { [key: string]: string } = {};

    if (!formData.firstName.trim())
      newErrors.firstName = "First name is required.";
    if (!formData.lastName.trim())
      newErrors.lastName = "Last name is required.";
    if (!/\S+@\S+\.\S+/.test(formData.email))
      newErrors.email = "Invalid email address.";
    if (!/^\d{5}$/.test(formData.zip))
      newErrors.zip = "Zip code must be 5 digits.";
    if (Number(formData.salary) <= 0)
      newErrors.salary = "Salary must be greater than zero.";

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  return (
    <div className={styles.inputPage}>
      <h1 className={styles.title}>Welcome</h1>
      <div className={styles.subtitle}>
        <h2>
          Let's get you set up to compare the best insurance plans. We'll need a
          few details to get started.
        </h2>
      </div>

      <div className={styles.line}></div>
      <div className={styles.formContainer}>
        <form className={styles.form} onSubmit={handleSubmit}>
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
          {/* Address Information */}
          <div className={styles.formGroup}>
            <div className={styles.formLabelGroup}>Address</div>
            <div className={styles.formInputGroup}>
              <div className={styles.inputsNextToEachOther}>
                <input
                  type="text"
                  placeholder="City"
                  name="city"
                  value={formData.city}
                  onChange={handleChange}
                  required
                />
                <input
                  type="text"
                  placeholder="State/Province/Region"
                  name="state"
                  value={formData.state}
                  onChange={handleChange}
                  required
                />
              </div>
              <div className={styles.inputsNextToEachOther}>
                <input
                  type="text"
                  placeholder="Zip Code"
                  name="zip"
                  value={formData.zip}
                  onChange={handleChange}
                  required
                />
                <input
                  type="text"
                  placeholder="Country"
                  name="country"
                  value={formData.country}
                  onChange={handleChange}
                  required
                />
              </div>
            </div>
          </div>
          <div className={styles.line}></div>
          {/* Budget Information */}
          <div className={styles.formGroup}>
            <div className={styles.formLabelGroup}>Budget Information</div>
            <div className={styles.formInputGroup}>
              <div className={styles.inputsNextToEachOther}>
                <input
                  type="number"
                  placeholder="Salary"
                  name="salary"
                  value={formData.salary}
                  onChange={handleChange}
                  required
                />
                <input
                  type="number"
                  placeholder="# People in Household"
                  name="numHousehold"
                  value={formData.numHousehold}
                  onChange={handleChange}
                  required
                />
                <input
                  type="number"
                  placeholder="Budget"
                  name="budget"
                  value={formData.budget}
                  onChange={handleChange}
                  required
                />
              </div>
              <div className={styles.inputsNextToEachOther}>
                <input
                  type="text"
                  placeholder="Health concerns/additional information"
                  name="concerns"
                  value={formData.concerns}
                  onChange={handleChange}
                />
              </div>
            </div>
          </div>
          <div className={styles.line}></div>
          {/* File Upload */}
          <div className={styles.formGroup}>
            <div className={styles.formLabelGroup}>Upload PDFs</div>
            <div className={styles.formInputGroup}>
              <FileUpload />
            </div>
          </div>
          <div className={styles.line}></div>
          <br></br>
          {/* Submit Button */}
          <button
            type="submit"
            className={styles.submitButton}
            disabled={isSubmitting}
          >
            Submit
          </button>
          {isSubmitting ? "Submitting..." : "Submit"}
        </form>
      </div>
    </div>
  );
};
export default Input;
