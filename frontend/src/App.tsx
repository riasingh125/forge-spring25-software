import { Amplify } from 'aws-amplify';
import { Authenticator } from '@aws-amplify/ui-react';
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
//import Authenticator from amplify



/*
const config = {
  aws_project_region: 'us-east-1',
  aws_cognito_region: 'us-east-1', 
  aws_user_pools_id: 'us-east-1_0BnGQZ2AO', 
  aws_user_pools_web_client_id: '7357poqc90amf4c1c7t3i6dqjs',
  aws_mandatory_sign_in: false,
};
*/

Amplify.configure(config);


export interface Result {
  name : string;
  affordability : number;
  personalHealth : number;
  essentialServicesCoverage : number;
  flexibility : number;
  geographicCoverage : number;
  familyCoverage : number;
  convenience : number;
  longTermBenefits : number;
  totalScore : number;
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
  const [messages, setMessages] = useState<Message[]>(
    [new Message("Hello! Welcome to Parcel! How can I assist you today?", "bot")]);

  return (
    <>
      <Authenticator>
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
    </>
  );
}

export default App;

