import { Link } from "react-router-dom";
import "./NavBarStyles.css";
import { useFlow } from "../context/FlowContext";
import logo from "../resources/parcel.png";
import { useAuthenticator } from "@aws-amplify/ui-react";

interface NavbarProps {
  signOut?: () => void;
}

const Navbar: React.FC<NavbarProps> = () => {
  const { hasSubmittedInput } = useFlow();
  const { signOut, user } = useAuthenticator((context) => [context.user]);

  return (
    <nav
      style={{
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        padding: "0 20px",
      }}
    >
      <div className="logo">
        <img src={logo} alt="logo" style={{ width: "40px", height: "40px" }} />
        <h1
          style={{
            fontSize: "25px",
            fontFamily: "Georgia",
            fontStyle: "italic",
            fontWeight: "400",
          }}
        >
          parcel
        </h1>
      </div>
      <div
        className="pages"
        style={{
          display: "flex",
          alignItems: "center",
          gap: "30px",
          paddingRight: "5px",
          marginLeft: "auto",
        }}
      >
        <Link
          to="/input"
          className="enabled"
          style={{ display: "flex", alignItems: "center" }}
        >
          Input
        </Link>

        <Link
          to="/results"
          className={`nav-link ${hasSubmittedInput ? "enabled" : "disabled"}`}
          style={{ display: "flex", alignItems: "center" }}
        >
          Results
        </Link>
        {user && (
          <button
            className="sign-out"
            onClick={signOut}
            style={{
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              padding: "5px 15px",
              borderRadius: "4px",
              background: "#FFFAEE",
              color: "#416774",
            }}
          >
            Sign Out
          </button>
        )}
      </div>
    </nav>
  );
};

export default Navbar;
