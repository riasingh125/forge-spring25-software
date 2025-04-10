import { Amplify } from 'aws-amplify';
import { Authenticator, ThemeProvider, Theme } from '@aws-amplify/ui-react';
import '@aws-amplify/ui-react/styles.css'; 
import { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Input from "./pages/Input/Input";
import Rankings from "./pages/Ranking/Rankings";
import Results from "./pages/Results/Results";

import config from './aws-exports';
import Navbar from "./components/NavBar";
import {
  ProtectedRankingsRoute,
  ProtectedResultsRoute,
} from "./routes/ProtectedRoutes";
import logo from './resources/parcel.png';

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
  name: string
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
  shortSummary : string;
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

const theme = {
  name: 'parcel-custom-theme',
  tokens: {
    colors: {
      brand: {
        primary: '#416774',
        secondary: '#000000',
      },
    },

    components: {
      button: {
        primary: {
          backgroundColor: '{colors.brand.primary}',
          borderColor: '{colors.brand.primary}',
          borderRadius: '4px',
        },
      },

      tabs: {
        item: {
          borderColor: "#a7bccf",
          color: "#a7bccf",
        },
    },
  }
  },
};

function App() {
  const [results, setResults] = useState<Result[]>([]);
  const [modalOpened, setModalOpened] = useState(false);
  const [messages, setMessages] = useState<Message[]>(
    [new Message("Hello! Welcome to Parcel! How can I assist you today?", "bot")]);

  return (
    <ThemeProvider theme={theme}>
      <div style={{ 
      display: 'flex',
      justifyContent: 'center',
      paddingTop: '150px',
      paddingLeft: '550px',
    }}>
      <Authenticator components={{
          Header() {
            return (
              <div style={{
                display: 'flex', 
                justifyContent: 'center', 
                alignItems: 'center',
                gap: '10px',
                paddingBottom: '10px',
              }}>

                <img src={logo} alt="Parcel Logo" style={{ width: '50px', height: '50px' }} />
                <h1 style={{ 
                  fontSize: '36px', 
                  fontFamily: 'Georgia', 
                  fontStyle: 'italic', 
                  fontWeight: 400,
                  margin: 0
                }}>
                  parcel
                </h1>
              </div>
            );
          }
        }}>
        {({ signOut, user }) => ( 
      <Router>
        <Navbar signOut={signOut}></Navbar>
        <Routes>
          <Route
            path="/input"
            element={<Input results={results} setResults={setResults}
          modalOpened={modalOpened} setModalOpened={setModalOpened}
          messages={messages} setMessages={setMessages} />}
          />
          <Route
            path="/rankings"
            element={
              <ProtectedRankingsRoute>
                {" "}
                <Rankings results={results} setResults={setResults}
          modalOpened={modalOpened} setModalOpened={setModalOpened}
          messages={messages} setMessages={setMessages} />{" "}
              </ProtectedRankingsRoute>
            }
          />
          <Route
            path="/results"
            element={
              <ProtectedResultsRoute>
                <Results results={results} setResults={setResults} 
          modalOpened={modalOpened} setModalOpened={setModalOpened}
          messages={messages} setMessages={setMessages} />
              </ProtectedResultsRoute>
            }
          />
        </Routes>
      </Router>
        )}
      </Authenticator>
      </div>
    </ThemeProvider>
  );
}

export default App;

