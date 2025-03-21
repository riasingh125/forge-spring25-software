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
  name: string;
  price: string;
}

export interface ResultsProps {
  results: Result[];
  setResults: React.Dispatch<React.SetStateAction<Result[]>>;
}

function App() {
  const [results, setResults] = useState<Result[]>([]);

  return (
    <>
      <Router>
        <Navbar></Navbar>
        <Routes>
          <Route
            path="/input"
            element={<Input results={results} setResults={setResults} />}
          />
          <Route
            path="/rankings"
            element={
              <ProtectedRankingsRoute>
                {" "}
                <Rankings results={results} setResults={setResults} />{" "}
              </ProtectedRankingsRoute>
            }
          />
          <Route
            path="/results"
            element={
              <ProtectedResultsRoute>
                <Results results={results} setResults={setResults} />
              </ProtectedResultsRoute>
            }
          />
        </Routes>
      </Router>
    </>
  );
}

export default App;
