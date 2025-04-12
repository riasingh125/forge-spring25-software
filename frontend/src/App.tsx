import { Amplify } from "aws-amplify";
import { Authenticator, ThemeProvider, Theme } from "@aws-amplify/ui-react";
import "@aws-amplify/ui-react/styles.css";
import { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Input from "./pages/Input/Input";
import Results from "./pages/Results/Results";
import Home from "./pages/Home/Home";

import config from "./aws-exports";
import Navbar from "./components/NavBar";
import { ProtectedResultsRoute } from "./routes/ProtectedRoutes";
import logo from "./resources/parcel.png";
import { FormProvider } from "./context/FormContext";

Amplify.configure(config);

// export interface Result {
//   name : string;
//   affordability : number;
//   personalHealth : number;
//   essentialServicesCoverage : number;
//   flexibility : number;
//   geographicCoverage : number;
//   familyCoverage : number;
//   convenience : number;
//   longTermBenefits : number;
//   totalScore : number;
// }

export interface Result {
  name: string;
  totalScore: number;
  weightedScores: {
    affordability: number;
    convenience_of_coverage: number;
    coverage_of_all_benefits: number;
    emergency_coverage: number;
    flexibility_of_coverage: number;
    geographic_coverage: number;
    personalized_coverage: number;
  };
}

export interface ResultsProps {
  results: Result[];
  setResults: React.Dispatch<React.SetStateAction<Result[]>>;
  modalOpened: boolean;
  setModalOpened: React.Dispatch<React.SetStateAction<boolean>>;
  messages: Message[];
  setMessages: React.Dispatch<React.SetStateAction<Message[]>>;
}

export class Message {
  message: string;
  sender: "user" | "bot";

  constructor(message: string, sender: "user" | "bot") {
    this.message = message;
    this.sender = sender;
  }
}

export interface ResultsProps {
  results: Result[];
  setResults: React.Dispatch<React.SetStateAction<Result[]>>;
}

function App() {
  const [results, setResults] = useState<Result[]>([]);
  const [modalOpened, setModalOpened] = useState(false);
  const [messages, setMessages] = useState<Message[]>([
    new Message("Hello! Welcome to Parcel! How can I assist you today?", "bot"),
  ]);

  return (
    <div
      style={{
        height: "100vh",
        width: "100vw",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Authenticator
        components={{
          Header() {
            return (
              <div className="auth-header">
                <img src={logo} alt="Parcel Logo" className="auth-logo" />
                <h1 className="auth-title">parcel</h1>
              </div>
            );
          },
        }}
      >
        {({ signOut, user }) => (
          <FormProvider>
            <Router>
              <Navbar signOut={signOut} />
              <Routes>
                <Route path="/" element={<Home />} />
                <Route
                  path="/input"
                  element={
                    <Input
                      results={results}
                      setResults={setResults}
                      modalOpened={modalOpened}
                      setModalOpened={setModalOpened}
                      messages={messages}
                      setMessages={setMessages}
                    />
                  }
                />
                <Route
                  path="/results"
                  element={
                    <ProtectedResultsRoute>
                      <Results
                        results={results}
                        setResults={setResults}
                        modalOpened={modalOpened}
                        setModalOpened={setModalOpened}
                        messages={messages}
                        setMessages={setMessages}
                      />
                    </ProtectedResultsRoute>
                  }
                />
              </Routes>
            </Router>
          </FormProvider>
        )}
      </Authenticator>
    </div>
  );
}

export default App;
