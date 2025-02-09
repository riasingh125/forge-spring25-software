import React from 'react';
import styles from "./rankings.module.css";
import RankingRow from '../../components/RankingRow';
const Rankings: React.FC = () => {
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

    return (
    <div className={styles.container}>
        <h3>Rank the following by importance</h3>

        <div>
            {rankingItems.map((item, index) => (
                <RankingRow key={index} number={index + 1} label={item} />
            ))}

        </div>

        <button className={styles.nextButton}>
            Next
        </button>
    </div>
    );
    
};

export default Rankings;