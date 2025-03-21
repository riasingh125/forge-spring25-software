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
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  // Handle input changes
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  // Handle form submission
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setLoading(true);
    try {
      const validationError = validateFormData(formData);

      if (validationError) {
        throw new Error(validationError);
      }

      navigate("/Rankings", { state: { formData } });
    } catch (err) {
      console.error("Submission error:", err);
      setError(
        err instanceof Error
          ? err.message
          : "Unexpected error. Please try again."
      );
    } finally {
      setLoading(false);
    }
  };

  type FormDataType = {
    firstName: string;
    lastName: string;
    email: string;
    city: string;
    state: string;
    zip: string;
    country: string;
    salary: string;
    numHousehold: string;
    budget: string;
    concerns: string;
  };

  const validateFormData = (data: FormDataType): string | null => {
    const trimmedData = Object.fromEntries(
      Object.entries(data).map(([key, value]) => [key, value.trim()])
    );

    const requiredFields = [
      "firstName",
      "lastName",
      "email",
      "city",
      "state",
      "zip",
      "country",
      "salary",
      "numHousehold",
      "budget",
    ];

    for (let field of requiredFields) {
      if (!trimmedData[field as keyof FormDataType]) {
        return `Please fill out the "${field}" field.`;
      }
    }

    // Email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(trimmedData.email)) {
      return "Please enter a valid email address.";
    }

    // Zip code validation
    if (!/^\d{5}(-\d{4})?$/.test(trimmedData.zip)) {
      return "Please enter a valid zip code.";
    }

    // Salary, numHousehold, and budget should be positive numbers
    const numericFields = ["salary", "numHousehold", "budget"];
    for (let field of numericFields) {
      const value = parseFloat(trimmedData[field as keyof FormDataType]);
      if (isNaN(value) || value <= 0) {
        return `Please enter a valid positive number for "${field}".`;
      }
    }

    return null;
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
          {/* Show Errors */}
          {error && (
            <div
              style={{ color: "red", textAlign: "center", marginTop: "1rem" }}
            >
              {error}
            </div>
          )}
          {/* Submit Button */}
          <button
            type="submit"
            className={styles.submitButton}
            disabled={loading}
          >
            {loading ? "Submitting..." : "Submit"}
          </button>
        </form>
      </div>
    </div>
  );
};
export default Input;
