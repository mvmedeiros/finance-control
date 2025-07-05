import React, { useState } from 'react';
import TransactionList from '../components/TransactionList';
import TransactionForm from '../components/TransactionForm';

const TransactionsPage = () => {
  const [refreshKey, setRefreshKey] = useState(0);

  return (
    <div>
        <TransactionForm key={refreshKey} />
        <TransactionList key={refreshKey} />
    </div>
  );
};

export default TransactionsPage;