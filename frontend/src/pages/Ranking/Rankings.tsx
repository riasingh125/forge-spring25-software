import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Slider from '@mui/material/Slider';
import MuiInput from '@mui/material/Input';

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


export default function Rankings() {
    const navigate = useNavigate();
    const [values, setValues] = React.useState<{ [key: string]: number | string }>(
        Object.fromEntries(rankingItems.map((item) => [item, 1]))
    );

    // Handle slider change
    const handleSliderChange = (category: string) => (event: Event, newValue: number | number[]) => {
        setValues((prev) => ({
            ...prev,
            [category]: newValue as number,
        }));
    };

    // Handle input change
    const handleInputChange = (category: string) => (event: React.ChangeEvent<HTMLInputElement>) => {
        const newValue = event.target.value;

        if (newValue === "") {
            setValues((prev) => ({ ...prev, [category]: "" }));
            return;
        }

        const parsedValue = Number(newValue);
        if (!isNaN(parsedValue) && parsedValue >= 1 && parsedValue <= 10) {
            setValues((prev) => ({ ...prev, [category]: parsedValue }));
        }
    };

    // Handle blur event to correct invalid values
    const handleBlur = (category: string) => () => {
        let finalValue = Number(values[category]);
        if (isNaN(finalValue) || finalValue < 1) finalValue = 1;
        if (finalValue > 10) finalValue = 10;

        setValues((prev) => ({ ...prev, [category]: finalValue }));
    };

    //Handle Submit
    const handleSubmit = () => {
        navigate("/results", { state: { rankings: values } });
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
                                value={typeof values[category] === "number" ? values[category] : 1}
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
                                value={values[category]}
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

            {/* Submit Button */}
            <Box sx={{ textAlign: "center", marginTop: 4 }}>
                <button type="submit" onClick={handleSubmit}>
                    Submit
                </button>
            </Box>
        </Box>
    );
}