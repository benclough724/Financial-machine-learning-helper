import React, { useState } from "react";
import "./App.css";

function App() {
  const [input1, setInput1] = useState("");
  const [input2, setInput2] = useState("");
  const [submittedData, setSubmittedData] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmittedData({ input1, input2 });
  };

  return (
    <div className="App">
      <h1>Two Input Boxes App</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Input 1:</label>
          <input
            type="text"
            value={input1}
            onChange={(e) => setInput1(e.target.value)}
            placeholder="Enter first value"
          />
        </div>
        <div>
          <label>Input 2:</label>
          <input
            type="text"
            value={input2}
            onChange={(e) => setInput2(e.target.value)}
            placeholder="Enter second value"
          />
        </div>
        <button type="submit">Submit</button>
      </form>

      {submittedData && (
        <div className="output">
          <h2>Submitted Data:</h2>
          <p>
            <strong>Input 1:</strong> {submittedData.input1}
          </p>
          <p>
            <strong>Input 2:</strong> {submittedData.input2}
          </p>
        </div>
      )}
    </div>
  );
}

export default App;
