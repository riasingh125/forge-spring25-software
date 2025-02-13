import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./styles.module.css";

const Input: React.FC = () => {
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

  // Handle input changes
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  // Handle form submission
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await fetch("back end endpoint here", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        navigate("/rankings");
      } else {
        alert("Error submitting the form. Please try again.");
      }
    } catch (error) {
      console.error("Submission error:", error);
      alert("Failed to connect to the server.");
    }
  };

  return (
    <div>
      <h1>Welcome</h1>
      <h3>
        Let's get you set up to compare the best insurance plans. We'll need a
        few details to get started.
      </h3>
      <hr></hr>
      <div className={styles.formContainer}>
        <form className={styles.form}>
          {/* Contact Information */}
          <div className={styles.formGroup}>
            <div className={styles.formLabelGroup}>Contact Information</div>
            <div className={styles.formInputGroup}>
              <div>
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
              <div>
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

          <hr></hr>

          {/* Address Information */}
          <div className={styles.formGroup}>
            <div className={styles.formLabelGroup}>Address</div>
            <div className={styles.formInputGroup}>
              <div>
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
              <div>
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

          <hr></hr>

          {/* Budget Information */}

          <div className={styles.formGroup}>
            <div className={styles.formLabelGroup}>Budget Information</div>
            <div className={styles.formInputGroup}>
              <div>
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
                  placeholder="Number of People in Household"
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
              <div>
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

          <hr></hr>

          {/* Submit Button */}
          <button type="submit" className={styles.submitButton}>
            Submit
          </button>
        </form>
      </div>
    </div>
  );
};

export default Input;
