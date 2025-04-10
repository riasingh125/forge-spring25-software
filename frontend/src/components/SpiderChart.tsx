import React, {useMemo} from "react";
import { Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, Tooltip, ResponsiveContainer } from "recharts";
import { Result } from "../App";
import './TextBoxStyles.css';
interface SpiderChartProps {
    scores: Result;
    color: string;
}


export default function SpiderChart({ scores, color }: SpiderChartProps) {



    // affordability: number,
    // convenience_of_coverage: number,
    // coverage_of_all_benefits: number,
    // emergency_coverage: number,
    // flexibility_of_coverage: number,
    // geographic_coverage: number,
    // personalized_coverage: number


    const transformData = (result: Result) => {
        return [
            { factor: "Affordability", value: result.weightedScores.affordability },
            { factor: "Personal Health", value: result.weightedScores.coverage_of_all_benefits},
            { factor: "Essential Services", value: result.weightedScores.emergency_coverage},
            { factor: "Flexibility", value: result.weightedScores.flexibility_of_coverage},
            { factor: "Geographic Coverage", value: result.weightedScores.geographic_coverage},
            { factor: "Family Coverage", value: result.weightedScores.personalized_coverage}
        ];
    }

    // Convert `Result` into Recharts format
    const chartData = useMemo(() => {
        return transformData(scores);
    }, [scores])



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

