import './TextBoxStyles.css';
import SpiderChart from './SpiderChart';
import {Result} from '../App';
import results from "../pages/Results/Results.tsx";
import React from 'react';
import _Collapsible from 'react-collapsible';
import type { FC } from 'react';
import Tooltip from "@mui/material/Tooltip";

const Collapsible = _Collapsible as unknown as FC<any>;


interface TextBoxProps {
    rank: number;
    title: string;
    content: Result;
    bgColor: string;
    expanded: boolean;
    result: Result
}

export const dummyResult: Result = {
    name: "Sample Plan",
    totalScore: 7,
    weightedScores: {
        affordability: 9,
        convenience_of_coverage: 9,
        coverage_of_all_benefits: 8,
        emergency_coverage: 4,
        flexibility_of_coverage: 3,
        geographic_coverage: 2,
        personalized_coverage: 7
    },
    shortSummary: ""
}

// will use content once we have the actual data
export default function TextBox({
                                    rank,
                                    title,
                                    content,
                                    bgColor,
                                    expanded,
                                    result
                                }: TextBoxProps) {
    if (result == undefined) {
        return <></>
    }
    // console.log("RESULT TEXT BOX:")
    // console.log(result)

    if (expanded) {
        return (
            <div>
                <div className="box-container" style={{
                    width: "80vw",
                    backgroundColor: bgColor
                }}>
                    <h6>{rank + 1}. {title}</h6>
                    <div className="results-content">
                        <div className="inner-box-expanded">
                            <SpiderChart scores={content}
                                         color={bgColor}></SpiderChart>
                        </div>
                        <div className="score-card">
                            <b style={{paddingBottom: "3%"}}>⭐ Overall Rating: {result.totalScore}</b>
                            <div className="line"></div>
                         <div style={{padding: "2%", fontSize: "80%", paddingTop: "2%"}}>{result.shortSummary}</div>
                        </div>
                    </div>
                    <br></br>
                </div>
                <br></br>
            </div>
        );
    } else {
        return (
            <div>
                <div className="box-container" style={{
                    width: "50vw",
                    backgroundColor: bgColor
                }}>
                    <h6>{rank + 1}. {title}</h6>
                    <div className="inner-box">
                        <SpiderChart scores={result}
                                     color={bgColor}></SpiderChart>
                    </div>
                    <br></br>
                    <div className="score-and-summary">
                    <Collapsible trigger={
                        <span className="score-tag">
                            ⭐ Overall Rating: {result.totalScore}&nbsp;
                            <div style={{opacity: "70%", fontWeight: "normal", fontStyle: "italic", fontSize: "80%", alignSelf: "center"}}>
                                (click to learn more)
                            </div>
                        </span>}>
                            <div className="line"></div>
                            <div style={{paddingBottom: "2%"}}>{result.shortSummary}</div>
                        </Collapsible>
                    </div>
                </div>
                <br></br>
            </div>
        );
    }
}
  