import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";
import { useLocation } from "react-router-dom";
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Slider from '@mui/material/Slider';
import MuiInput from '@mui/material/Input';
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import { SelectChangeEvent } from '@mui/material/Select';
import { ResultsProps } from "../../App";

import {sendInputData} from "../sendInputAPI.ts";
import {getResults} from "../resultsAPI.ts";

const Input = styled(MuiInput)`
  width: 30px;
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

    const [selectedOption, setSelectedOption] = useState("");
    const [dropdownError, setDropdownError] = useState(false);

    const handleDropdownChange = (event: SelectChangeEvent<string>) => {
        setSelectedOption(event.target.value);
        setDropdownError(false);
    };

    // Handle slider change
    const handleSliderChange = (category: string) => (event: Event, newValue: number | number[]) => {
        setRankings((prev) => ({
            ...prev,
            [category]: newValue as number,
        }));
    };

    // Handle input change
    const handleInputChange = (category: string) => (event: React.ChangeEvent<HTMLInputElement>) => {
        const newValue = event.target.value;

        if (newValue === "") {
            setRankings((prev) => ({ ...prev, [category]: "" }));
            return;
        }

        const parsedValue = Number(newValue);
        if (!isNaN(parsedValue) && parsedValue >= 1 && parsedValue <= 10) {
            setRankings((prev) => ({ ...prev, [category]: parsedValue }));
        }
    };

    // Handle blur event to correct invalid values
    const handleBlur = (category: string) => () => {
        let finalValue = Number(rankings[category]);
        if (isNaN(finalValue) || finalValue < 1) finalValue = 1;
        if (finalValue > 10) finalValue = 10;

        setRankings((prev) => ({ ...prev, [category]: finalValue }));
    };

    //Handle Submit
    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();

        // Check if dropdown is selected
        if (!selectedOption) {
            setDropdownError(true);
            return; // Stop submission
        }

        const fullUserData = { ...formData, ...rankings, selectedOption };
        const success = await sendInputData(fullUserData);
        // just updates results regardless
        navigate("/results");
        getResults().then(newResults => {
            setResults(newResults);
        });
      };

    return (
        <Box sx={{ width: 400, margin: "auto" }}>
            <Typography variant="h5" gutterBottom>
                Rank the following by importance
            </Typography>

            { /* Reference Slider */}
            <Box sx={{ marginBottom: 4, textAlign: "center" }}>
                <Typography variant="subtitle2">1 = Least Important, 10 = Most Important</Typography>
                <Slider
                    value={5}
                    step={null} // Prevent interaction
                    marks={marks}
                    min={1}
                    max={10}
                    disabled
                    sx={{ color: "gray" }}
                />
            </Box>
            

            {rankingItems.map((category) => (
                <Box key={category} sx={{ marginBottom: 3 }}>
                    <Typography variant="subtitle1">{category}</Typography>
                    <Grid container spacing={2} sx={{ alignItems: "center" }}>
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
                            />
                        </Grid>
                        <Grid item>
                            <Input
                                value={rankings[category]}
                                size="small"
                                onChange={handleInputChange(category)}
                                onBlur={handleBlur(category)}
                                inputProps={{
                                    step: 1,
                                    min: 1,
                                    max: 10,
                                    type: "number",
                                    "aria-labelledby": `slider-${category}`,
                                }}
                            />
                        </Grid>
                    </Grid>
                </Box>
            ))}

            {/* Dropdown Selection */}
            <Box sx={{ marginTop: 4, textAlign: "center" }}>
                <Typography variant="subtitle1">Select your level of familiarity with healthcare jargon.</Typography>
                <Select value={selectedOption} onChange={handleDropdownChange} displayEmpty fullWidth error={dropdownError}>
                    <MenuItem value="" disabled>Select an option</MenuItem>
                    <MenuItem value="Option 1">Unfamiliar</MenuItem>
                    <MenuItem value="Option 2">Slightly Familiar</MenuItem>
                    <MenuItem value="Option 3">Moderately Familiar</MenuItem>
                    <MenuItem value="Option 4">Pretty Familiar</MenuItem>
                    <MenuItem value="Option 3">Extremely Familiar</MenuItem>
                </Select>
            </Box>

            {/* Submit Button */}
            <Box sx={{ textAlign: "center", marginTop: 4 }}>
                <button type="submit" onClick={handleSubmit}>
                    Submit
                </button>
            </Box>
        </Box>
    );
}

export default Rankings; 