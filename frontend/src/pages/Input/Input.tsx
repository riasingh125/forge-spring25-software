import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./styles.module.css";
import { ResultsProps } from "../../App";
import { useFlow } from "../../context/FlowContext";
import { useFlow as formUseFlow } from "../../context/FormContext";
import ContactInfo from "../../components/form/ContactInfo";
import Address from "../../components/form/Address";
import BudgetInfo from "../../components/form/BudgetInfo";
import UploadPdfs from "../../components/form/UploadPdfs";
import Rankings from "../../components/form/Rankings";

const Input: React.FC<ResultsProps> = ({
  results,
  setResults,
  modalOpened,
  setModalOpened,
  messages,
  setMessages,
}) => {
  const navigate = useNavigate();
  const { formData, setFormData } = formUseFlow();
  const [files, setFiles] = useState<File[]>([]);
  const [planCost, setPlanCost] = useState<number[]>([]);
  const { setHasSubmittedInput } = useFlow();
  const [step, setStep] = useState(0);

  // Handle form submission
  const handleSubmit = async (e: React.FormEvent) => {
    console.log("Form submitted");
    console.log(formData);
    e.preventDefault();
    //SubmittedInput(true);
    //navigate("/Results", { state: { formData, files, planCost } });
  };

  const nextStep = () =>
    setStep((prev) => Math.min(prev + 1, SubForms.length - 1));
  const prevStep = () => setStep((prev) => Math.max(prev - 1, 0));

  const SubForms = [
    <ContactInfo key="contact"/>,
    <Address key="address" />,
    <BudgetInfo key="budget" />,
    <UploadPdfs key="upload" />,
    <Rankings key="rankings" />,
  ];

  return (
    <div>
      <form className={styles.form} onSubmit={handleSubmit}>
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
            <button type="submit" className={styles.submitButton}>
              Submit
            </button>
          )}
        </div>
      </form>
    </div>
  );
};
export default Input;
