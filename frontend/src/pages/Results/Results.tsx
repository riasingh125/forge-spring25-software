import React from 'react';
import TextBox from '../../components/ResultsText';
import { ResultsProps, Result } from '../../App';
import Chatbot from '../../components/Chatbot';
import styles from './results.module.css';

const Results: React.FC<ResultsProps> = ({results}) => {





    function displayResult(results: Result, index: number) {
        return (
            <TextBox
            key={index}
            title={results.name}
            content={`price: ${results.price}`}
            width= "500px"
            height="250px" 
            />


        )
    }

    return (
        <>
        <div className={styles.resultspage}>
            <div className={styles.resultsdisplay}>
                <br></br>
                <h1>Results</h1>
                <br></br>
                {
                results.map((result, index) => (
                    displayResult(result, index)
                ))
                }
            </div>
            <div className={styles.chatbotdisplay}>
                <Chatbot />
            </div>
        </div>
        </>

    )
    
    
}

export default Results;