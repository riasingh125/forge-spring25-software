import { Link } from "react-router-dom";
import "./NavBarStyles.css";
import { useFlow } from "../context/FlowContext";
import logo from '../resources/parcel.png'

const Navbar: React.FC = () => {
  const { hasSubmittedInput } = useFlow();
  const { hasCompletedRankings } = useFlow();

  return (
    <nav>
      <div className="logo">
        <img src={logo} alt="logo" style={{width: "40px", height: "40px"}}/>
        <h1 style={{fontSize: "25px", fontFamily: "Georgia", fontStyle: "italic", fontWeight: "400"}}>parcel</h1>
      </div>
      <div className="pages">
        <Link to="/input" className="enabled">Input</Link> <Link to="/rankings" className={`nav-link ${hasSubmittedInput ? "enabled" : "disabled"}`}>Rankings</Link> <Link to="/results" className={`nav-link ${hasCompletedRankings ? "enabled" : "disabled"}`}>Results</Link>
      </div>
    </nav>
  );
};

export default Navbar;
