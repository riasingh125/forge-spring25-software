import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./styles.module.css";
import { InputPageProps } from "../../App";
import { useFlow } from "../../context/FlowContext";
import { useFlow as formUseFlow } from "../../context/FormContext";
import ContactInfo from "../../components/form/ContactInfo";
import Address from "../../components/form/Address";
import BudgetInfo from "../../components/form/BudgetInfo";
import UploadPdfs from "../../components/form/UploadPdfs";
import Rankings from "../../components/form/Rankings";
import {getSessionID, sendInputData} from "../sendInputAPI";

const Input: React.FC<InputPageProps> = ({ results, setResults }) => {
  const navigate = useNavigate();
  const { formData } = formUseFlow();
  const { setHasSubmittedInput } = useFlow();
  const [step, setStep] = useState(0);
  const [loading, setLoading] = useState(false);

  // Handle form submission
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    console.log("Form submitted");
    console.log(formData);

    if (loading) {
      return;
    }
    setLoading(true);
    const { files, costs, ...formDataWithoutFilesAndCosts } = formData;

    setLoading(false);
    setHasSubmittedInput(true);
    // get session id and store it
    const sessionId = await getSessionID();
    localStorage.setItem("sessionId", sessionId);

    // success = true, if form upload worked someone handle that..
    const results = await sendInputData(
      formDataWithoutFilesAndCosts,
      files,
      costs,sessionId
    );
    if (results.length === 0) {
      console.log("GOT 0 RESULTS");
      return;
    }
    setResults(results);
    navigate("/results");
  };

  const nextStep = () =>
    setStep((prev) => Math.min(prev + 1, SubForms.length - 1));
  const prevStep = () => setStep((prev) => Math.max(prev - 1, 0));

  const SubForms = [
    <ContactInfo key="contact" />,
    <Address key="address" />,
    <BudgetInfo key="budget" />,
    <UploadPdfs key="upload" />,
    <Rankings key="rankings" />,
  ];

  return (
    <div>
      <form className={styles.form}>
        {/* Render current step */}
        <div>{SubForms[step]}</div>
        {/* Navigation Buttons */}
        <div
          className={
            step === 0 ? styles.buttonGroupCentered : styles.buttonGroup
          }
        >
          {step > 0 && (
            <button
              type="button"
              onClick={prevStep}
              className={styles.navButton}
            >
              Previous
            </button>
          )}
          {step < SubForms.length - 1 ? (
            <button
              type="button"
              onClick={nextStep}
              className={styles.navButton}
            >
              Next
            </button>
          ) : (
            <button
              type="button"
              onClick={handleSubmit}
              className={styles.submitButton}
            >
              Submit
            </button>
          )}
        </div>
      </form>
    </div>
  );
};
export default Input;
