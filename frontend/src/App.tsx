import { Amplify } from 'aws-amplify';
import { Authenticator } from '@aws-amplify/ui-react';
import { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";


import Input from "./pages/Input/Input";
import Rankings from "./pages/Ranking/Rankings";
import Results from "./pages/Results/Results";
import config from './aws-exports';
import Navbar from "./components/NavBar";
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
  name: string;
  price: number;
}

export interface ResultsProps {
  results: Result[];
  setResults: React.Dispatch<React.SetStateAction<Result[]>>;
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

