import { Navigate } from "react-router-dom";
import { useFlow } from "../context/FlowContext";

export const ProtectedRankingsRoute = ({
  children,
}: {
  children: React.ReactNode;
}) => {
  const { hasSubmittedInput } = useFlow();
  return hasSubmittedInput ? children : <Navigate to="/input" />;
};

export const ProtectedResultsRoute = ({
  children,
}: {
  children: React.ReactNode;
}) => {
  const { hasCompletedRankings } = useFlow();
  return hasCompletedRankings ? children : <Navigate to="/rankings" />;
};
