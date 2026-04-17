import React, { useState } from "react";

export default function App() {
  const [input, setInput] = useState("");
  const [result, setResult] = useState(null);

  const analyze = async () => {
    const res = await fetch("http://localhost:8000/analyze", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({input_text: input})
    });
    const data = await res.json();
    setResult(data);
  };

  return (
    <div style={{padding:20}}>
      <h2>PhishGuard Complete 🚀</h2>
      <textarea value={input} onChange={e=>setInput(e.target.value)} rows={6} style={{width:"100%"}} />
      <br/><br/>
      <button onClick={analyze}>Analyze</button>

      {result && (
        <div>
          <h3>AI Result:</h3>
          <pre>{JSON.stringify(result.ai_result, null, 2)}</pre>
          <h3>VirusTotal Status:</h3>
          <p>{result.virustotal_status}</p>
        </div>
      )}
    </div>
  );
}
