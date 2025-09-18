import React, { useEffect, useState } from "react";
import ReactDOM from "react-dom/client";

function App() {
  const [message, setMessage] = useState("Loading...");

  useEffect(() => {
    fetch("/api/hello")
      .then(res => res.json())
      .then(data => setMessage(data.message))
      .catch(() => setMessage("Error connecting to backend"));
  }, []);

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>Frontend App</h1>
      <p>{message}</p>
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
