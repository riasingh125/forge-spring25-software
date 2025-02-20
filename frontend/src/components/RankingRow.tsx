import React from "react";
import styles from "../pages/Ranking/rankings.module.css";

interface RankingRowProps {
    number: number;
    label: string;
}

const RankingRow: React.FC<RankingRowProps> = ({ number, label }) => {
    return (
      <div className={styles.item}>
        <span className={styles.number}>{number}</span>
  
        {/* Drag Handle */}
        <div className={styles.dragHandle}>
          <div></div>
          <div></div>
          <div></div>
        </div>
  
        {/* Ranking Box */}
        <div className={styles.box}>{label || "Empty"}</div>
      </div>
    );
  };
  
  export default RankingRow;