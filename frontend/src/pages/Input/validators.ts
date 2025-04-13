import { FormDataType } from "../../context/FormContext";

export const validateContactInfo = (data: FormDataType) => {
  if (!data.firstName?.trim()) return "First name is required.";
  if (!data.lastName?.trim()) return "Last name is required.";
  if (!data.email?.trim() || !data.email.includes("@"))
    return "Valid email is required.";
  if (!data.phone?.trim()) return "Phone number is required.";
  if (!data.familiarity) return "Please select your healthcare familiarity.";
  return true;
};

export const validateAddress = (data: FormDataType) => {
  if (!data.city?.trim()) return "City is required.";
  if (!data.state?.trim()) return "State/Province/Region is required.";
  if (!data.zip?.trim()) return "Zip Code is required.";
  if (!/^\d{5}(-\d{4})?$/.test(data.zip)) return "Zip Code must be valid.";
  if (!data.country?.trim()) return "Country is required.";
  return true;
};

export const validateBudgetInfo = (data: FormDataType) => {
  if (!data.salary || Number(data.salary) <= 0)
    return "Salary must be a positive number.";
  if (!data.numHousehold || Number(data.numHousehold) <= 0)
    return "Household size must be at least 1.";
  if (!data.budget || Number(data.budget) <= 0)
    return "Budget must be a positive number.";
  if (!data.age || Number(data.age) <= 0)
    return "Age must be a positive number.";

  return true;
};

export const validateUploadPdfs = (data: FormDataType) => {
  if (!data.files || data.files.length === 0) {
    return "Please upload at least one PDF file.";
  }
  if (!data.costs || data.costs.length !== data.files.length) {
    return "Each uploaded PDF must have a corresponding cost.";
  }
  return true;
};
