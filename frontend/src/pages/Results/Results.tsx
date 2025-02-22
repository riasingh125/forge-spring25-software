import React from 'react';
import TextBox from '../../components/ResultsText';
import { ResultsProps, Result } from '../../App';


    

const Results: React.FC<ResultsProps> = ({results, setResults}) => {

    function displayResult(results: Result) {
        return (
            <>
            <TextBox 
            title={results.name}
            content={`price: ${results.price}`}
            width= "500px"
            height="250px" 
            />
            <br></br>
            </>
        )
    }

    return (
        <>
            {
            results.map((result) => (
                displayResult(result)
            ))
            }
        </>

    )
    
    
}

export default Results;