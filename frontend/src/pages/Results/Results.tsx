import React, { useState } from 'react';
import TextBox from '../../components/ResultsText';
import { ResultsProps, Result } from '../../App';
import Chatbot from '../../components/Chatbot';
import styles from './results.module.css';
import Modal from '../../components/ResultsModal'
import info from '../../resources/info.png'
import Button from '@mui/material/Button';
import Tooltip from '@mui/material/Tooltip';

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

function displayResult(results: Result, index: number, total: number, expanded: boolean) {
    const startColor = "#254E5C";
    const endColor = "#597D8A";
    const factor = index / Math.max(1, total - 1); // Avoid division by zero
    const bgColor = interpolateColor(startColor, endColor, factor);

    return (
        <TextBox
            key={index}
            rank={index}
            title={results.name}
            content={results}
            bgColor={bgColor} 
            expanded={expanded}
        />
    )
}

// constant for Results header and modal button so it doesn't have to repear
const ResultsAndModalButton = (setOpen: () => void) => {
    return (
    <div className={styles.resultsAndInfo}>
        <h1>Results</h1>
        <Tooltip 
        title="What do my results mean?" 
        arrow 
        placement="right-start">
            <button className={styles.openModal}> 
                <img 
                src={info} alt="my image" 
                onClick={setOpen}
                className={styles.infoImage}/>
            </button>
        </Tooltip>
    </div>);
};

const Results: React.FC<ResultsProps> = ({results}) => {
    const [isModalOpen, setIsModalOpen] = useState(true);
    const setOpen = () => setIsModalOpen(true);
    const setClose = () => setIsModalOpen(false);

    const [isChatOpen, setIsChatOpen] = useState(true);

    if (isChatOpen) {
        return (
            <div>
                <Modal 
                isOpen= {isModalOpen} 
                handleClose= {setClose}/>
                <button className={styles.closeChat} onClick={() => setIsChatOpen(false)}>✖</button>
                <div className={styles.resultsdisplay}>
                    {ResultsAndModalButton(setOpen)}
                    {
                    results.map((result, index) => (
                        displayResult(result, index, results.length, false)
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
            <Modal 
            isOpen= {isModalOpen} 
            handleClose= {setClose}/>
            <button className={styles.openChat} onClick={() => setIsChatOpen(true)}>
                Chat
            </button>
            <div className={styles.resultsCentered}>
            {ResultsAndModalButton(setOpen)}
                {
                results.map((result, index) => (
                   displayResult(result, index, results.length, true)
                ))
                }
            </div>
            </div> 
    
        )
    }
    

}

export default Results;
