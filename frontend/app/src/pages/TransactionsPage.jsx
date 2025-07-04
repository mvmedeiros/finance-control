// src/pages/TransactionsPage.jsx
import React, { useState } from 'react';
import TransactionList from '../components/TransactionList';

const TransactionsPage = () => {
  const [refreshKey, setRefreshKey] = useState(0);

  return (
    <div>
      <TransactionList key={refreshKey} />
    </div>
  );
};

export default TransactionsPage;