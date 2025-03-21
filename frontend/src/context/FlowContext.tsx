import React, { createContext, useContext, useState, ReactNode } from "react";

interface FlowContextType {
  hasSubmittedInput: boolean;
  setHasSubmittedInput: React.Dispatch<React.SetStateAction<boolean>>;
  hasCompletedRankings: boolean;
  setHasCompletedRankings: React.Dispatch<React.SetStateAction<boolean>>;
}

const FlowContext = createContext<FlowContextType | null>(null);

interface FlowProviderProps {
  children: ReactNode;
}

export const FlowProvider: React.FC<FlowProviderProps> = ({ children }) => {
  const [hasSubmittedInput, setHasSubmittedInput] = useState(false);
  const [hasCompletedRankings, setHasCompletedRankings] = useState(false);

  return (
    <FlowContext.Provider
      value={{
        hasSubmittedInput,
        setHasSubmittedInput,
        hasCompletedRankings,
        setHasCompletedRankings,
      }}
    >
      {children}
    </FlowContext.Provider>
  );
};

export const useFlow = (): FlowContextType => {
  const context = useContext(FlowContext);
  if (!context) {
    throw new Error("useFlow must be used within a FlowProvider");
  }
  return context;
};
