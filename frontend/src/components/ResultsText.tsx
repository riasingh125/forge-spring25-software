
import './TextBoxStyles.css';
import SpiderChart from './SpiderChart';
import { Result } from '../App';

interface TextBoxProps {
  rank: number;
  title: string;
  content: Result;
  bgColor: string;
  expanded: boolean;
}

export const dummyResult: Result = {
    name: "Sample Plan",
    totalScore: 7.2,
    affordability: 8,
    personalHealth: 7,
    essentialServicesCoverage: 9,
    flexibility: 6,
    geographicCoverage: 8,
    familyCoverage: 7,
    convenience: 5,
    longTermBenefits: 9
  };

// will use content once we have the actual data
export default function TextBox({ rank, title, content, bgColor, expanded }: TextBoxProps) {
  if (expanded) {
    return (
      <div>
        <div className="box-container" style={{width: "80vw", height: "550px", backgroundColor: bgColor }}>
          <h6>{rank + 1}. {title}</h6>
          <div className="results-content">
            <div className="inner-box-expanded">
              <SpiderChart scores = {dummyResult} color = {bgColor}></SpiderChart>
            </div>
            <div className="score-card"> 
            <h2 style={{fontFamily: "Georgia", fontSize:"25px", fontWeight: 400, lineHeight: "1.5"}}>
              <br></br>
              ⭐ overall rating: {dummyResult.totalScore}
              <div className="line"></div>
              affordability: {dummyResult.affordability}
              <br></br>
              personal health: {dummyResult.personalHealth}
              <br></br>
              essential services coverage: {dummyResult.essentialServicesCoverage}
              <br></br>
              flexibility: {dummyResult.flexibility}
              <br></br>
              geographic coverage: {dummyResult.geographicCoverage}
              <br></br>
              family coverage: {dummyResult.familyCoverage}
              <br></br>
              convenience: {dummyResult.convenience}
              <br></br>
              long-term benefits: {dummyResult.longTermBenefits}
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
            <SpiderChart scores = {dummyResult} color = {bgColor}></SpiderChart>
          </div>
          <br></br>
          <div className="score-tag"> 
            <h2 style={{fontSize:"20px", fontWeight: 400}}>
              ⭐ overall rating: {dummyResult.totalScore}
            </h2>
          </div>
        </div>
        <br></br>
      </div>
    );
  }
  }
  