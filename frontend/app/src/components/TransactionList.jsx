import { useEffect, useState } from 'react';
import { getTransactions } from '../services/api';

const TransactionList = () => {
  const [transactions, setTransactions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await getTransactions();
        setTransactions(data);
      } catch (err) {
        setError(err.message || 'Something went wrong');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) return <p>Loading transactions...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div>
      <h2>Transaction List</h2>
      <ul>
        {transactions.map((tx) => (
          <li key={tx.id}>
            {tx.description} - ${tx.amount}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TransactionList;