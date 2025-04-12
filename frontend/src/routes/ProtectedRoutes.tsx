import { Navigate } from "react-router-dom";
import { useFlow } from "../context/FlowContext";

export const ProtectedResultsRoute = ({
  children,
}: {
  children: React.ReactNode;
}) => {
  const { hasSubmittedInput } = useFlow();
  return hasSubmittedInput ? children : <Navigate to="/results" />;
};
