import { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Input from "./pages/Input/Input";
import Rankings from "./pages/Ranking/Rankings";
import Results from "./pages/Results/Results";
import Navbar from "./components/NavBar";
import {
  ProtectedRankingsRoute,
  ProtectedResultsRoute,
} from "./routes/ProtectedRoutes";

import "./App.css";

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

function App() {
  const [results, setResults] = useState<Result[]>([]);
  const [modalOpened, setModalOpened] = useState(false);
  const [messages, setMessages] = useState<Message[]>(
    [new Message("Hello! Welcome to Parcel! How can I assist you today?", "bot")]);

  return (
    <>
      <Router>
        <Navbar></Navbar>
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
    </>
  );
}

export default App;
