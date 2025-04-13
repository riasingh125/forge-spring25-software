import Modal from '@mui/material/Modal';
import styles from './ModalStyles.module.css';
import info from '../resources/info.png';
import SpiderChart from './SpiderChart';
import {dummyResult} from './ResultsText.tsx';
import {Result} from "../App.tsx";

interface ModalProps {
  isOpen: boolean;
  handleClose: () => void;
  setNoOpenOnClick: React.Dispatch<React.SetStateAction<boolean>>;
  result: Result
}

export default function ResultsModal({ isOpen, handleClose, setNoOpenOnClick, result}: ModalProps) {


  return (
    <div>
      <Modal
        open={isOpen}>
        <div className={styles.modalBoxOuter}>
          <div className={styles.modalBoxInner}>
            <div>
              <strong style={{fontSize: "28px"}}>Before you dive into your results, here are a few details: </strong>
              <br></br>
              <br></br>
              We ranked each of your possible plans from best fit to worst fit, given your priorities. 
              You will see a spider chart showing the ratings for each plan, and the overall rating based on the weight you assigned to each category. 
              <br></br>
              <br></br>
              <div style={{fontStyle: "italic", marginBottom: "10px"}}>For example, if you weighed affordability as a 10 and the rest of the categories as 1s, you'd likely see the
              cheapest plan ranked first with the highest overall rating.</div>
              <hr></hr>
              <br></br>
              You can hover over the vertexes of each chart to see exact numbers for each plan, or close the 
              chatbot to view a list of all the individual scores. (Feel free to play around with the sample chart below)
              <br></br>
              <div style={{width: "100%", height: "30%", marginTop: "20px"}}>
                <SpiderChart scores={result} color={"gray"}/>
              </div>
              <br></br> 
              <hr style={{marginTop:"20px", marginBottom: "20px"}}></hr>
              The page automatically opens with a chatbot on the right that you can open and close whenever you wish, and don't worry, your messages will save.
              <br></br>
              <br></br>
              <strong style={{textDecoration: "underline"}}>We highly encourage you to ask the chatbot any questions you might have!</strong>
              <br></br>
              <hr style={{marginTop:"20px", marginBottom: "20px"}}></hr>
              We hope this tool helps you make a decision that's right for you!
              <br></br>
              <br></br>
              If you need to reopen this message for any reason, just click the <img src={info} style={{width:"15px", height: "15px"}}></img> symbol next to "Results"!
              <br></br>
            </div>
          </div>
          <br></br>
          <button className={styles.modalButton} onClick={() => { handleClose(); setNoOpenOnClick(true); }}>Close</button>
        </div>
      </Modal>
    </div>
  );
}
