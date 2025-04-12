import { Navigate } from "react-router-dom";
import { useFlow } from "../context/FlowContext";

export const ProtectedResultsRoute = ({
  children,
}: {
  children: React.ReactNode;
}) => {
  const { hasSubmittedInput } = useFlow();

  if (!hasSubmittedInput) {
    return <div>Please complete the input to view the results.</div>; 
  }

  return <>{children}</>;
};
