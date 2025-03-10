import React from "react";
import TextBox from "../../components/ResultsText";
import { ResultsProps, Result } from "../../App";
import Chatbot from "../../components/Chatbot";
import resultStyles from "./results.module.css";

const Results: React.FC<ResultsProps> = ({ results }) => {
  function displayResult(results: Result, index: number) {
    return (
      <TextBox
        key={index}
        title={results.name}
        content={`price: ${results.price}`}
        width="500px"
        height="250px"
      />
    );
  }

  return (
    <>
      <div className={resultStyles.resultspage}>
        <div className={resultStyles.resultsdisplay}>
          <br></br>
          <h1>Results</h1>
          <br></br>
          {results.map((result, index) => displayResult(result, index))}
        </div>
        <div className={resultStyles.chatbotdisplay}>
          <Chatbot />
        </div>
      </div>
    </>
  );
};

export default Results;
