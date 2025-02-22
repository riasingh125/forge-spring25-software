import React from 'react';
import TextBox from '../../components/ResultsText';

const Results: React.FC = () => (
    <div>
        <h1>Results page</h1>
        <TextBox 
        title="#1: Plan A" 
        content="Details" 
        width= {500}
        height="250px" 
        />
        <h1></h1>
        <TextBox 
        title="#2: Plan B" 
        content="More details" 
        width="500px" 
        height="200px" 
/>
    </div>
    
);

export default Results;