
import './TextBoxStyles.css';

interface TextBoxProps {
  rank: number;
  title: string;
  content: string;
  width: number | string;
  height: number | string;
  bgColor?: string;
}

export default function TextBox({ rank, title, content, width, height, bgColor }: TextBoxProps) {
    return (
      <div className="box-container" style={{width, height, backgroundColor: bgColor }}>
        <h6>{rank + 1}. {title}</h6>
        <div className="inner-box">
          <p>{content}</p>
        </div>
      </div>
    );
  }
  