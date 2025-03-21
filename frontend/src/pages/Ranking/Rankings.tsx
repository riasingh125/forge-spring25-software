import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";
import { useLocation } from "react-router-dom";
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Slider from '@mui/material/Slider';
import MuiInput from '@mui/material/Input';
import { ResultsProps } from "../../App";
import {sendInputData} from "../sendInputAPI.ts";
import {getResults} from "../resultsAPI.ts";
import styles from "./rankings.module.css"

const Input = styled(MuiInput)`
  width: 42px;
  `;

const marks = [
    { value: 1, label: "1" },
    { value: 2, label: "2" },
    { value: 3, label: "3" },
    { value: 4, label: "4" },
    { value: 5, label: "5" },
    { value: 6, label: "6" },
    { value: 7, label: "7" },
    { value: 8, label: "8" },
    { value: 9, label: "9" },
    { value: 10, label: "10" },
];

const rankingItems = [
    "Affordability",
    "Personal Health Concerns",
    "Coverage of Essential Services",
    "Plan Flexibility",
    "Geographic Coverage",
    "Coverage for Family and Dependents",
    "Convenience/Ease of Use",
    "Long-Term Benefits",
];



const Rankings: React.FC<ResultsProps> = ({results, setResults}) => {

    const navigate = useNavigate();
    const location = useLocation(); 
    const { formData } = location.state || {};

    const [rankings, setRankings] = React.useState<{ [key: string]: number | string }>(
        Object.fromEntries(rankingItems.map((item) => [item, 1]))
    );

    // Handle slider change
    const handleSliderChange = (category: string) => (event: Event, newValue: number | number[]) => {
        setRankings((prev) => ({
            ...prev,
            [category]: newValue as number,
        }));
    };

    //Handle Submit
    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        const fullUserData = { ...formData, ...rankings };
        const success = await sendInputData(fullUserData);
        // just updates results regardless
        navigate("/results");
        getResults().then(newResults => {
            setResults(newResults);
        });
      };

    return (
        <div>
        <Box sx={{ 
            width: "60vw",
            maxWidth: "100%",
             margin: "auto", 
             padding: 11 }}>

            {/**<h1 style = {{}}> Rank the following factors by importance. </h1> */}
            <h2 style={{fontStyle: "italic", marginBottom: 40}}>
             Rank the following factors on a scale from <br></br>
             Least Important (1) » Most Important (10)
            </h2>
            <hr></hr>

            {rankingItems.map((category) => (
                <Box key={category} sx={{ padding: 2 }}>
                    <h3>{category}</h3>
                    <Grid container spacing={2} sx={{ alignItems: "center", padding: 2 }}>
                        <Grid item xs>
                            <Slider
                                value={typeof rankings[category] === "number" ? rankings[category] : 1}
                                onChange={handleSliderChange(category)}
                                step={1}
                                min={1}
                                max={10}
                                marks={marks}
                                valueLabelDisplay="auto"
                                aria-labelledby={`slider-${category}`}
                                sx = {{ 
                                    color: "var(--navy)",
                                    "& .MuiSlider-thumb": {
                                        backgroundColor: "white",
                                        border: "2px solid var(--navy)",
                                    },
                                    "& .MuiSlider-markLabel": {
                                        fontSize: "20px", 
                                        fontWeight: "bold",
                                    },
                                    height: 15,
                                }}
                            />
                        </Grid>
                    </Grid>
                </Box>
            ))}

            {/* Submit Button */}
            <Box sx={{ textAlign: "center", marginTop: 4 }}>
                <button type="submit" onClick={handleSubmit}>
                    Submit
                </button>
            </Box>
        </Box>
        </div>
    );
}

export default Rankings; 