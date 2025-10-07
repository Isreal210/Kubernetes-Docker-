import React, { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("Loading...");

  useEffect(() => {
    // When running in Kubernetes, replace with your Flask service name:
    fetch('http://155.98.38.240:31251/api/hello')
      .then((res) => res.json())
      .then((data) => setMessage(data.message))
      .catch((err) => {
        console.error("Error fetching message:", err);
        setMessage("Failed to fetch message from backend.");
      });
  }, []);

  return (
    <div className="App">
      <h1>Thomas Burke is the GOAT 🥏</h1>
      <p>{message}</p>
    </div>
  );
}

export default App;
