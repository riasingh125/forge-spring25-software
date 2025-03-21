import React, { useState } from 'react';
import TextBox from '../../components/ResultsText';
import { ResultsProps, Result } from '../../App';
import Chatbot from '../../components/Chatbot';
import styles from './results.module.css';

function interpolateColor(start: string, end: string, factor: number): string {
    const hexToRgb = (hex: string) => 
        hex.match(/\w\w/g)?.map((x) => parseInt(x, 16)) ?? [0, 0, 0];

    const rgbToHex = (r: number, g: number, b: number) => 
        `#${((1 << 24) | (r << 16) | (g << 8) | b).toString(16).slice(1)}`;

    const startRgb = hexToRgb(start);
    const endRgb = hexToRgb(end);
    
    const resultRgb = startRgb.map((startVal, i) => 
        Math.round(startVal + factor * (endRgb[i] - startVal))
    );

    return rgbToHex(resultRgb[0], resultRgb[1], resultRgb[2]);
}

function displayResult(results: Result, index: number, total: number) {
    const startColor = "#254E5C";
    const endColor = "#597D8A";
    const factor = index / Math.max(1, total - 1); // Avoid division by zero
    const bgColor = interpolateColor(startColor, endColor, factor);

    return (
        <div> 
        <TextBox
            key={index}
            rank={index}
            title={results.name}
            content={`price: ${results.price}`}
            width="500px"
            height="300px"
            bgColor={bgColor} 
        />
        <br></br>
        </div>
    )
}

const Results: React.FC<ResultsProps> = ({results}) => {
    const [isChatOpen, setIsChatOpen] = useState(true);

    if (isChatOpen) {
        return (
            <div>
                <button className={styles.closeChat} onClick={() => setIsChatOpen(false)}>✖</button>
                <div className={styles.resultsdisplay}>
                    <br></br>
                    <h1>Results</h1>
                    <br></br>
                    {
                    results.map((result, index) => (
                        displayResult(result, index, results.length)
                    ))
                    }
                </div>
                <Chatbot />
            </div> 
    
        )
    }

    if (!isChatOpen) {
        return (
            <div>
            <button className={styles.openChat} onClick={() => setIsChatOpen(true)}>
            Chat
            </button>
            <div className={styles.resultsCentered}>
            <br></br>
                <h1>Results</h1>
                <br></br>
                {
                results.map((result, index) => (
                   displayResult(result, index, results.length)
                ))
                }
            </div>
            </div> 
    
        )
    }
    

}

export default Results;
