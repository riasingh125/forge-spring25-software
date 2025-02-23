import React, { useState } from "react";
import styles from "./ChatbotStyles.module.css";

const Chatbot: React.FC = () => {
  const [messages, setMessages] = useState<{ text: string; sender: string }[]>([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { text: input, sender: "user" };
    setMessages((prev) => [...prev, userMessage]);

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
      const botMessage = { text: data.response, sender: "bot" };
      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      setMessages((prev) => [...prev, { text: "Error: Unable to fetch response", sender: "bot" }]);
    }

    setInput("");
  };

  return (
    <div className={styles.chatcontainer}>
      <div className={styles.chatbox}>
        {messages.map((msg, index) => (
          <div key={index} className={`message ${msg.sender}`}>
            <strong>{msg.sender === "user" ? "You" : "Bot"}:</strong> {msg.text}
          </div>
        ))}
      </div>
      <div className={styles.chatinput}>
        <input
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
