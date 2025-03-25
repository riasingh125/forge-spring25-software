import Modal from '@mui/material/Modal';
import styles from './ModalStyles.module.css';

interface ModalProps {
  isOpen: boolean;
  handleClose: () => void;
  setNoOpenOnClick: React.Dispatch<React.SetStateAction<boolean>>;
}

export default function ResultsModal({ isOpen, handleClose, setNoOpenOnClick}: ModalProps) {

  return (
    <div>
      <Modal
        open={isOpen}>
        <div className={styles.modalBoxOuter}>
          <h1>Here are your results! Hover over the radar chart vertexes to see exact values. 
            Feel free to use the chatbot for any questions you might have!</h1>
            <br></br>
          <button onClick={() => { handleClose(); setNoOpenOnClick(true); }}>X</button>
        </div>
      </Modal>
    </div>
  );
}
