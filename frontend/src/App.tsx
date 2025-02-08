import { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Input from "./pages/Input/Input";
import Rankings from "./pages/Rankings";
import Results from "./pages/Results";

import Navbar from "./components/NavBar";

import "./App.css";

function App() {
  return (
    <>
      <Router>
        <Navbar></Navbar>
        <Routes>
          <Route path="/input" element={<Input />} />
          <Route path="/rankings" element={<Rankings />} />
          <Route path="/results" element={<Results />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
