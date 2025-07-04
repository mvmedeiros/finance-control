export const getTransactions = async () => {
  const response = await fetch('http://localhost:8000/api/transactions/');
  if (!response.ok) throw new Error('Failed to fetch transactions');
  return response.json();
};