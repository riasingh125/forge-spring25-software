import { Link } from "react-router-dom";
import './NavBarStyles.css'

const Navbar: React.FC = () => {
  return (
    <nav>
      <Link to="/input">Input</Link> | <Link to="/rankings">Rankings</Link> | <Link to="/results">Results</Link>
    </nav>
  );
};

export default Navbar;
