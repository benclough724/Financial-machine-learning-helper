// App.jsx
import React from "react";
import { Header } from "./components/Header";
import { Overview } from "./components/Overview";
import { PredictionCard } from "./components/PredictionCard";
import { TransactionTable } from "./components/TransactionTable";

export default function App() {
  return (
    <div className="min-h-screen bg-gray-50 text-gray-900">
      <Header />
      <main className="max-w-6xl mx-auto p-4 space-y-6">
        <Overview />
        <PredictionCard />
        <TransactionTable />
      </main>
    </div>
  );
}
