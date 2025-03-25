import { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";


import Input from "./pages/Input/Input";
import Rankings from "./pages/Ranking/Rankings";
import Results from "./pages/Results/Results";

import Navbar from "./components/NavBar";

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
}

export interface Message {
  message: string;
  sender: string;
}

function App() {
  const [results, setResults] = useState<Result[]>([]);
  const [modalOpened, setModalOpened] = useState(false);

  return (
    <>
      <Router>
        <Navbar></Navbar>
        <Routes>
          <Route path="/input" element={<Input results={results} setResults={setResults}
          modalOpened={modalOpened} setModalOpened={setModalOpened}/>} />
          <Route path="/rankings" element={<Rankings results={results} setResults={setResults}
          modalOpened={modalOpened} setModalOpened={setModalOpened}/>} />
          <Route path="/results" element={<Results results={results} setResults={setResults} 
          modalOpened={modalOpened} setModalOpened={setModalOpened}/>} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
