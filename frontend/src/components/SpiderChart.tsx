import React from "react";
import { Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, Tooltip, ResponsiveContainer } from "recharts";
import { Result } from "../App";
import './TextBoxStyles.css';

interface SpiderChartProps {
    scores: Result;
    color: string;
}

const transformData = (result: Result) => [
    { factor: "Affordability", value: result.affordability },
    { factor: "Personal Health", value: result.personalHealth },
    { factor: "Essential Services", value: result.essentialServicesCoverage },
    { factor: "Flexibility", value: result.flexibility },
    { factor: "Geographic Coverage", value: result.geographicCoverage },
    { factor: "Family Coverage", value: result.familyCoverage },
    { factor: "Convenience", value: result.convenience },
    { factor: "Long-Term Benefits", value: result.longTermBenefits }
];


export default function SpiderChart({ scores, color }: SpiderChartProps) {
    const chartData = transformData(scores); // Convert `Result` into Recharts format

    return (
        <ResponsiveContainer width="100%" height="100%">
            <RadarChart cx="50%" cy="50%" outerRadius="80%" data={chartData}>
                <PolarGrid />
                <PolarAngleAxis dataKey="factor" tickSize={20}/>
                <PolarRadiusAxis angle={90} domain={[0, 10]} tickCount={10}/>
                <Tooltip />
                <Radar name={scores.name} dataKey="value" stroke={color} fill={color} fillOpacity={0.6} />
            </RadarChart>
        </ResponsiveContainer>
    );
};

