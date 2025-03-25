import { Link } from "react-router-dom";
import './NavBarStyles.css'
import logo from '../resources/parcel.png'

const Navbar: React.FC = () => {
  return (
    <nav>
      <div className="logo">
        <img src={logo} alt="logo" style={{width: "40px", height: "40px"}}/>
        <h1 style={{fontSize: "25px", fontFamily: "Georgia", fontStyle: "italic", fontWeight: "400"}}>parcel</h1>
      </div>
      <div className="pages">
        <Link to="/input">Input</Link> <Link to="/rankings">Rankings</Link> <Link to="/results">Results</Link>
      </div>
    </nav>
  );
};

export default Navbar;
