
import './TextBoxStyles.css';
import SpiderChart from './SpiderChart';
import { Result } from '../App';

interface TextBoxProps {
  rank: number;
  title: string;
  result: Result;
  bgColor: string;
  expanded: boolean;
}

export const dummyResult: Result = {
    name: "Sample Plan",
    totalScore: 7.2,
    weightedScores: {
        affordability: 7.2,
        convenience_of_coverage: 8,
        coverage_of_all_benefits: 7,
        emergency_coverage: 9,
        flexibility_of_coverage: 6,
        geographic_coverage: 8,
        personalized_coverage: 9
    }
  };

// will use content once we have the actual data
export default function TextBox({ rank, title, result, bgColor, expanded }: TextBoxProps) {
  if (expanded) {
    return (
      <div>
        <div className="box-container" style={{width: "80vw", height: "550px", backgroundColor: bgColor }}>
          <h6>{rank + 1}. {title}</h6>
          <div className="results-content">
            <div className="inner-box-expanded">
              <SpiderChart scores = {result} color = {bgColor}></SpiderChart>
            </div>
            <div className="score-card"> 
            <h2 style={{fontFamily: "Georgia", fontSize:"25px", fontWeight: 400, lineHeight: "1.5"}}>
              <br></br>
              ⭐ overall rating: {result.totalScore}
              <div className="line"></div>
              affordability: {result.weightedScores.affordability}
              <br></br>
              convenience of coverage: {result.weightedScores.convenience_of_coverage}
              <br></br>
              coverage of all benefits: {result.weightedScores.coverage_of_all_benefits}
              <br></br>
              emergency coverage: {result.weightedScores.emergency_coverage}
              <br></br>
              flexibility of coverage: {result.weightedScores.flexibility_of_coverage}
              <br></br>
              geographic coverage: {result.weightedScores.geographic_coverage}
              <br></br>
              personalized coverage: {result.weightedScores.personalized_coverage}
            </h2>
          </div>
          </div>
        </div>
        <br></br>
      </div>
    );
  }

  else {
    return (
      <div>
        <div className="box-container" style={{width: "50vw", height: "600px", backgroundColor: bgColor }}>
          <h6>{rank + 1}. {title}</h6>
          <div className="inner-box">
            <SpiderChart scores = {result} color = {bgColor}></SpiderChart>
          </div>
          <br></br>
          <div className="score-tag"> 
            <h2 style={{fontSize:"20px", fontWeight: 400}}>
              ⭐ overall rating: {result.totalScore}
            </h2>
          </div>
        </div>
        <br></br>
      </div>
    );
  }
  }
  