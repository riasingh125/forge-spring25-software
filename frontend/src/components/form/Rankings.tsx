import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useLocation } from "react-router-dom";
import { styled } from "@mui/material/styles";
import Box from "@mui/material/Box";
import Grid from "@mui/material/Grid";
import Typography from "@mui/material/Typography";
import Slider from "@mui/material/Slider";
import MuiInput from "@mui/material/Input";
import Select from "@mui/material/Select";
import MenuItem from "@mui/material/MenuItem";
import { SelectChangeEvent } from "@mui/material/Select";
import { ResultsProps } from "../../App";

import { sendInputData } from "../../pages/sendInputAPI.ts";
import { getResults } from "../../pages/resultsAPI.ts";
import styles from "./rankings.module.css";
import { useFlow } from "../../context/FlowContext.tsx";

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
  "Coverage of Personal Health Concerns",
  "Plan Flexibility",
  "Coverage of All Benefits",
  "Geographic Coverage",
  "Coverage in Emergencies",
  "Convenience of Accessing Benefits",
];

const rankingDescriptions = [
  "Overall cost of the plan, including premiums, deductibles, and out-of-pocket expenses.",
  "How well the plan covers your specific health needs, including pre-existing conditions and ongoing treatments.",
  "Flexibility in choosing healthcare providers, specialists, and treatment options.",
  "Comprehensive coverage of all necessary medical services, including preventive care and specialist visits.",
  "Availability of the plan in your geographic area and its network of providers.",
  "Coverage for emergency situations, including out-of-network care.",
  "Ease of accessing benefits, including online services, customer support, and appointment scheduling.",
];

const Rankings: React.FC<ResultsProps> = ({ results, setResults }) => {
  const navigate = useNavigate();
  const location = useLocation();
  const { formData } = location.state || {};
  const { files } = location.state || {};
  const { planCost } = location.state || {};

  const [loading, setLoading] = useState(false);

  const [rankings, setRankings] = React.useState<{
    [key: string]: number | string;
  }>(Object.fromEntries(rankingItems.map((item) => [item, 1])));

  const [selectedOption, setSelectedOption] = useState("");
  const [dropdownError, setDropdownError] = useState(false);

  const handleDropdownChange = (event: SelectChangeEvent<string>) => {
    setSelectedOption(event.target.value);
    setDropdownError(false);
  };

  // Handle slider change
  const handleSliderChange =
    (category: string) => (event: Event, newValue: number | number[]) => {
      setRankings((prev) => ({
        ...prev,
        [category]: newValue as number,
      }));
    };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (loading) {
      return;
    }

    // Check if dropdown is selected
    if (!selectedOption) {
      setDropdownError(true);
      return; // Stop submission
    }
    const fullUserData = { ...formData, ...rankings, selectedOption };
    console.log(planCost);

    setLoading(true);
    // success = true, if form upload worked someone handle that..
    const results = await sendInputData(fullUserData, files, planCost);
    setLoading(false);

    if (results.length === 0) {
      console.log("FAILED");
      return;
    }
    setResults(results);
    //navigate("/results");
  };

  return (
    <div>
      <Box
        sx={{
          width: "60vw",
          margin: "auto",
          padding: 11,
        }}
      >
        <h2 style={{ fontStyle: "italic", marginBottom: 40 }}>
          Rank the following factors on a scale from <br></br>
          Least Important (1) » Most Important (10)
        </h2>
        <hr></hr>

        {rankingItems.map((category, index) => (
          <Box key={category + index} sx={{ padding: 2 }}>
            <h3>{category}</h3>
            <h4
              style={{
                fontStyle: "italic",
                fontWeight: "normal",
                opacity: 0.5,
              }}
            >
              {rankingDescriptions[index]}
            </h4>
            <Grid
              container
              spacing={2}
              sx={{ alignItems: "center", padding: 2 }}
            >
              <Grid item xs>
                <Slider
                  value={
                    typeof rankings[category] === "number"
                      ? rankings[category]
                      : 1
                  }
                  onChange={handleSliderChange(category)}
                  step={1}
                  min={1}
                  max={10}
                  marks={marks}
                  valueLabelDisplay="auto"
                  aria-labelledby={`slider-${category}`}
                  sx={{
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
      </Box>
    </div>
  );
};

export default Rankings;
