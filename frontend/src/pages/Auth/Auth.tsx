import { Authenticator, ThemeProvider } from "@aws-amplify/ui-react";
import "@aws-amplify/ui-react/styles.css";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import logo from "../../resources/parcel.png";

const theme = {
  name: "parcel-custom-theme",
  tokens: {
    colors: {
      brand: {
        primary: "#416774",
        secondary: "#000000",
      },
    },
    components: {
      button: {
        primary: {
          backgroundColor: "{colors.brand.primary}",
          borderColor: "{colors.brand.primary}",
          borderRadius: "4px",
        },
      },
      tabs: {
        item: {
          borderColor: "#a7bccf",
          color: "#a7bccf",
        },
      },
    },
  },
};

export default function AuthPage() {
  const navigate = useNavigate();

  return (
    <ThemeProvider theme={theme}>
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          paddingTop: "150px",
          paddingLeft: "550px",
        }}
      >
        <Authenticator
          components={{
            Header() {
              return (
                <div
                  style={{
                    display: "flex",
                    justifyContent: "center",
                    alignItems: "center",
                    gap: "10px",
                    paddingBottom: "10px",
                  }}
                >
                  <img
                    src={logo}
                    alt="Parcel Logo"
                    style={{ width: "50px", height: "50px" }}
                  />
                  <h1
                    style={{
                      fontSize: "36px",
                      fontFamily: "Georgia",
                      fontStyle: "italic",
                      fontWeight: 400,
                      margin: 0,
                    }}
                  >
                    parcel
                  </h1>
                </div>
              );
            },
          }}
        >
          {({ user, signOut }) => {
            useEffect(() => {
              if (user) {
                navigate("/input");
              }
            }, [user]);

            return <></>;
          }}
        </Authenticator>
      </div>
    </ThemeProvider>
  );
}
