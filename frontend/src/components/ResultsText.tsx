
import './TextBoxStyles.css';

interface TextBoxProps {
  title: string;
  content: string;
  width: number | string;
  height: number | string;
}

export default function TextBox({ title, content, width, height }: TextBoxProps) {
    return (
      <div className="box-container" style={{ width, height }}>
        <h2 className="title">{title}</h2>
        <div className="inner-box">
          <p>{content}</p>
        </div>
      </div>
    );
  }
  