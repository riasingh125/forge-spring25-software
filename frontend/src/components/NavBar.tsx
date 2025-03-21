import { Link } from "react-router-dom";
import "./NavBarStyles.css";
import { useFlow } from "../context/FlowContext";

const Navbar: React.FC = () => {
  const { hasSubmittedInput } = useFlow();
  const { hasCompletedRankings } = useFlow();

  return (
    <nav>
      <Link to="/input" className="enabled">
        Input
      </Link>{" "}
      |{" "}
      <Link
        to="/rankings"
        className={`nav-link ${hasSubmittedInput ? "enabled" : "disabled"}`}
      >
        Rankings
      </Link>{" "}
      |{" "}
      <Link
        to="/results"
        className={`nav-link ${hasCompletedRankings ? "enabled" : "disabled"}`}
      >
        Results
      </Link>
    </nav>
  );
};

export default Navbar;
