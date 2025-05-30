import React, { createContext, useContext, useState, ReactNode } from "react";

type RankingsType = {
  [key: string]: number;
};

export interface FormDataType {
  firstName: string;
  lastName: string;
  email: string;
  familiarity: string;
  city: string;
  state: string;
  zip: string;
  country: string;
  salary: string;
  numHousehold: string;
  budget: string;
  concerns: string;
  age: string;
  phone: string;
  weights: RankingsType;
  files: File[];
  costs: number[];
}

interface FormContextType {
  formData: FormDataType;
  setFormData: React.Dispatch<React.SetStateAction<FormDataType>>;
}

const FormContext = createContext<FormContextType | null>(null);

interface FormProviderProps {
  children: ReactNode;
}

export const FormProvider: React.FC<FormProviderProps> = ({ children }) => {
  const [formData, setFormData] = useState<FormDataType>({
    firstName: "",
    lastName: "",
    email: "",
    familiarity: "",
    city: "",
    state: "",
    zip: "",
    country: "",
    salary: "",
    numHousehold: "",
    budget: "",
    concerns: "",
    age: "",
    phone: "",
    weights: {},
    files: [],
    costs: [],
  });

  return (
    <FormContext.Provider value={{ formData, setFormData }}>
      {children}
    </FormContext.Provider>
  );
};

export const useFlow = (): FormContextType => {
  const context = useContext(FormContext);
  if (!context) {
    throw new Error("useFlow must be used within a FormProvider");
  }
  return context;
};
