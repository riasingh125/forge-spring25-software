import React, { useState } from "react";
import styles from "./ChatbotStyles.module.css";
import { Message } from "../App.tsx";

interface ChatbotProps {
  messages: Message[];
  setMessages: React.Dispatch<React.SetStateAction<Message[]>>;
}

const Chatbot: React.FC<ChatbotProps> = ({messages, setMessages}) => {
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) return;
    
    setMessages((prev) => [...prev, { message: input, sender: "user" }]);

    try {
      // Replace with your AI API (e.g., OpenAI, Rasa, Dialogflow, etc.)
      const response = await fetch("http://127.0.0.1:8000/chat/message", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input }),
      });

      if (!response.ok) {
        throw new Error("Failed to fetch response");
      }
  
      const data = await response.json();
      const botMessage = new Message(data.response, "bot");
      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      setMessages((prev) => [...prev, new Message("Error: Unable to fetch response", "bot")]);
    }

    setInput("");
  };

  return (
    <div className={styles.chatcontainer}>    
    <div className={styles.chatTitle}>CHAT</div>
      <div className={styles.chatbox}>
        {messages.map((msg, index) => (
          <div key={index} className={`${styles.message} ${msg.sender === "user" ? styles.user : styles.bot}`}>
            <div className={styles.bubble}>
              <div className={styles.messageText}>{msg.message}</div> 
            </div>
            {msg.sender === "user" ? "You" : "Bot"}
          </div>
        ))}
      </div>
      <div className={styles.chatinput}>
        <input className={styles.messageinput}
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type a message..."
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
};

export default Chatbot;
