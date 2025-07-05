import { useState, React } from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import TransactionsPage from './pages/TransactionsPage';
import './App.css';

function App() {
  return (
    <div>
      <nav>
        <Link className='navBarLink' to="/">Home</Link>
        <Link className='navBarLink' to="/transactions">Transactions</Link>
      </nav>

      <Routes>
        <Route path="/" element={<h1>Welcome to the Expense Tracker</h1>} />
        <Route path="/transactions" element={<TransactionsPage />} />
      </Routes>

    </div>

  );
}

export default App;
