// src/App.tsx
import { Amplify } from 'aws-amplify';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { useState } from "react";

import config from './aws-exports';
import Input from "./pages/Input/Input";
import Rankings from "./pages/Ranking/Rankings";
import Results from "./pages/Results/Results";
import Navbar from "./components/NavBar";
import {
  ProtectedRankingsRoute,
  ProtectedResultsRoute,
} from "./routes/ProtectedRoutes";
import AuthPage from "./pages/Auth/Auth";

Amplify.configure(config);

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

function App() {
  const [results, setResults] = useState<Result[]>([]);
  const [modalOpened, setModalOpened] = useState(false);
  const [messages, setMessages] = useState<Message[]>(
    [new Message("Hello! Welcome to Parcel! How can I assist you today?", "bot")]
  );

  return (
    <Router>
      <Routes>
        <Route path="/" element={<AuthPage />} />
        <Route
          path="/input"
          element={
            <>
              <Navbar />
              <Input results={results} setResults={setResults}
                modalOpened={modalOpened} setModalOpened={setModalOpened}
                messages={messages} setMessages={setMessages} />
            </>
          }
        />
        <Route
          path="/rankings"
          element={
            <ProtectedRankingsRoute>
              <Navbar />
              <Rankings results={results} setResults={setResults}
                modalOpened={modalOpened} setModalOpened={setModalOpened}
                messages={messages} setMessages={setMessages} />
            </ProtectedRankingsRoute>
          }
        />
        <Route
          path="/results"
          element={
            <ProtectedResultsRoute>
              <Navbar />
              <Results results={results} setResults={setResults}
                modalOpened={modalOpened} setModalOpened={setModalOpened}
                messages={messages} setMessages={setMessages} />
            </ProtectedResultsRoute>
          }
        />
      </Routes>
    </Router>
  );
}

export default App;
