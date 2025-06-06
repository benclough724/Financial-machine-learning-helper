import { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip } from "recharts";


export default function DataView() {
  const [data, setData] = useState("");

  useEffect(() => {
    fetch("/http://127.0.0.1:8000/data/preprocessed")
      .then((res) => res.json())
      .then(setData);
  }, []);

  return (
    <LineChart width={500} height={300} data={data}>
      <XAxis dataKey="date" />
      <YAxis />
      <Tooltip />
      <Line type="monotone" dataKey="amount" stroke="#8884d8" />
    </LineChart>
  );
}