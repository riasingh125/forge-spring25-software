import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./styles.module.css";
import { ResultsProps } from "../../App";
import FileUpload from "../../components/FileUpload";
import { useFlow } from "../../context/FlowContext";
import { useFlow as formUseFlow } from "../../context/FormContext";
import ContactInfo from "../../components/form/ContactInfo";
import Address from "../../components/form/Address";
import BudgetInfo from "../../components/form/BudgetInfo";
import UploadPdfs from "../../components/form/UploadPdfs";
import Welcome from "../../components/form/Welcome";

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

  // Handle input changes
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  // Handle form submission
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setHasSubmittedInput(true);
    navigate("/Rankings", { state: { formData, files, planCost } });
  };

  const nextStep = () =>
    setStep((prev) => Math.min(prev + 1, SubForms.length - 1));
  const prevStep = () => setStep((prev) => Math.max(prev - 1, 0));

  const SubForms = [
    <Welcome
      key="welcome"
      results={results}
      setResults={setResults}
      modalOpened={modalOpened}
      setModalOpened={setModalOpened}
      messages={messages}
      setMessages={setMessages}
    />,
    <ContactInfo
      key="contact"
      results={results}
      setResults={setResults}
      modalOpened={modalOpened}
      setModalOpened={setModalOpened}
      messages={messages}
      setMessages={setMessages}
    />,
    <Address
      key="welcome"
      results={results}
      setResults={setResults}
      modalOpened={modalOpened}
      setModalOpened={setModalOpened}
      messages={messages}
      setMessages={setMessages}
    />,
    <BudgetInfo
      key="budget"
      results={results}
      setResults={setResults}
      modalOpened={modalOpened}
      setModalOpened={setModalOpened}
      messages={messages}
      setMessages={setMessages}
    />,
    <UploadPdfs
      key="upload"
      results={results}
      setResults={setResults}
      modalOpened={modalOpened}
      setModalOpened={setModalOpened}
      messages={messages}
      setMessages={setMessages}
    />,
  ];

  return (
    <div className={styles.inputPage}>
      <div className={styles.formContainer}>
        <form className={styles.form} onSubmit={handleSubmit}>
          {/* Render current step */}
          <div>{SubForms[step]}</div>
          {/* Navigation Buttons */}
          <div className={styles.buttonGroup}>
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
    </div>
  );
};
export default Input;
