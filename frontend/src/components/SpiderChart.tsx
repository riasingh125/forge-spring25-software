import React, {useMemo} from "react";
import { Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, Tooltip, ResponsiveContainer } from "recharts";
import { Result } from "../App";
import './TextBoxStyles.css';
interface SpiderChartProps {
    scores: Result;
    color: string;
}

export default function SpiderChart({ scores, color }: SpiderChartProps) {

    const chartData = useMemo(() => {
        if (!scores) return []; // handle null/undefined safely

        return [
          { factor: "Affordability", value: scores.weightedScores.affordability },
          { factor: "Personal Health", value: scores.weightedScores.personalized_coverage },
          { factor: "Emergency Coverage", value: scores.weightedScores.emergency_coverage },
          { factor: "Flexibility", value: scores.weightedScores.flexibility_of_coverage },
          { factor: "Geographic Coverage", value: scores.weightedScores.geographic_coverage },
          { factor: "All Benefits Coverage", value: scores.weightedScores.coverage_of_all_benefits },
          { factor: "Convenience", value: scores.weightedScores.convenience_of_coverage },
        ];
    }, [scores]);

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

