import { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";


import Input from "./pages/Input/Input";
import Rankings from "./pages/Ranking/Rankings";
import Results from "./pages/Results/Results";

import Navbar from "./components/NavBar";
//import Authenticator from amplify
import { Authenticator } from '@aws-amplify/ui-react';
import { Amplify } from 'aws-amplify';
import awsconfig from './aws-exports';
Amplify.configure(awsconfig);
import "./App.css";

export interface Result {
  name : string;
  price : string;
}

export interface ResultsProps {
  results: Result[];
  setResults: React.Dispatch<React.SetStateAction<Result[]>>;
}

function App() {
  const [results, setResults] = useState<Result[]>([]);

  return (
    <>
      <Authenticator>
        <h1>Welcome to the App</h1>
      <Router>
        <Navbar></Navbar>
        <Routes>
          <Route path="/input" element={<Input results={results} setResults={setResults}/>} />
          <Route path="/rankings" element={<Rankings results={results} setResults={setResults}/>} />
          <Route path="/results" element={<Results results={results} setResults={setResults}/>} />
        </Routes>
      </Router>
      </Authenticator>
    </>
  );
}

export default App;
