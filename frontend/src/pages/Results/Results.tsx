import React, { useState } from "react";
import TextBox, { dummyResult } from "../../components/ResultsText";
import { ResultsPageProps, Result } from "../../App";
import Chatbot from "../../components/Chatbot";
import styles from "./results.module.css";
import Modal from "../../components/ResultsModal";
import info from "../../resources/info.png";
import Tooltip from "@mui/material/Tooltip";

function interpolateColor(start: string, end: string, factor: number): string {
  const hexToRgb = (hex: string) =>
    hex.match(/\w\w/g)?.map((x) => parseInt(x, 16)) ?? [0, 0, 0];

  const rgbToHex = (r: number, g: number, b: number) =>
    `#${((1 << 24) | (r << 16) | (g << 8) | b).toString(16).slice(1)}`;

  const startRgb = hexToRgb(start);
  const endRgb = hexToRgb(end);

  const resultRgb = startRgb.map((startVal, i) =>
    Math.round(startVal + factor * (endRgb[i] - startVal))
  );

  return rgbToHex(resultRgb[0], resultRgb[1], resultRgb[2]);
}

function displayResult(
  result: Result,
  index: number,
  total: number,
  expanded: boolean
) {
  const startColor = "#254E5C";
  const endColor = "#597D8A";
  const factor = index / Math.max(1, total - 1); // Avoid division by zero
  const bgColor = interpolateColor(startColor, endColor, factor);

  return (
    <TextBox
      key={index}
      rank={index}
      title={result.name}
      content={result}
      bgColor={bgColor}
      expanded={expanded}
      result={result}
    />
  );
}

// constant for Results header and modal button so it doesn't have to repear
const ResultsAndModalButton = (setOpen: () => void) => {
  return (
    <div className={styles.resultsAndInfo}>
      <h1>Results</h1>
      <Tooltip
        title="How do I navigate this page?"
        arrow
        placement="right-start"
      >
        <button className={styles.openModal}>
          <img
            src={info}
            alt="info"
            onClick={setOpen}
            className={styles.infoImage}
          />
        </button>
      </Tooltip>
    </div>
  );
};

const Results: React.FC<ResultsPageProps> = ({
  results,
  modalOpened,
  setModalOpened,
  messages,
  setMessages,
}) => {
  const [isModalOpen, setIsModalOpen] = useState(!modalOpened);
  const setOpen = () => setIsModalOpen(true);
  const setClose = () => setIsModalOpen(false);

  const [isChatOpen, setIsChatOpen] = useState(true);

  if (isChatOpen) {
    return (
      <div>
        <Modal
          isOpen={isModalOpen}
          handleClose={setClose}
          setNoOpenOnClick={setModalOpened}
          result={dummyResult}
        />
        <button
          className={styles.closeChat}
          onClick={() => setIsChatOpen(false)}
        >
          ✖
        </button>
        <div className={styles.resultsdisplay}>
          {ResultsAndModalButton(setOpen)}
          {results.map((result, index) =>
            displayResult(result, index, results.length, false)
          )}
        </div>
        <Chatbot messages={messages} setMessages={setMessages} />
      </div>
    );
  }

  if (!isChatOpen) {
    return (
      <div>
        <Modal
          isOpen={isModalOpen}
          handleClose={setClose}
          setNoOpenOnClick={setModalOpened}
          result={dummyResult}
        />
        <button className={styles.openChat} onClick={() => setIsChatOpen(true)}>
          Chat
        </button>
        <div className={styles.resultsCentered}>
          {ResultsAndModalButton(setOpen)}
          {results.map((result, index) =>
            displayResult(result, index, results.length, true)
          )}
        </div>
      </div>
    );
  }
};

export default Results;
