import { use, useEffect, useState } from 'react';
import Creatable, { useCreatable } from 'react-select/creatable';
import { getCategories } from '../services/api';

const TransactionForm = ({ onSubmit, initialData = {} }) => {
  const [formData, setFormData] = useState({
    description: initialData.description || '',
    amount: initialData.amount || '',
    date: initialData.date || '',
    category: initialData.category || '',
    user: initialData.user || '',
    account: initialData.account || '',
    type: initialData.type || '',
  });

  const [categoryOptions, setCategoryOptions] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState(
    initialData.category ? { label: initialData.category, value: initialData.category} : null
  );

  // Category selection and creation
  useEffect(() => {
    // Mock data for frontend dev early phase
    const mockCategories = [
        { label: 'Food', value: 'food' },
    ];

    setTimeout(() => {
      setCategoryOptions(mockCategories);
    }, 500); // simulate 500ms API delay

  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleCategoryChange = (selectedOption) => {
    setSelectedCategory(selectedOption);
    setFormData(prev => ({
      ...prev,
      category: selectedOption ? selectedOption.value : '',
    }));
  }

  const handleCreateCategory = (newInput) => {
    const newCategory = { label: newInput, value: newInput };
    setCategoryOptions(prev => [...prev, newCategory]);
    setSelectedCategory(newCategory);
    setFormData(prev => ({
      ...prev,
      category: newInput,
    }));

    console.log('Mock: Created new category:', newInput);
  }

  const handleSubmit = (e) => {
    e.preventDefault(); // Prevent page reload
    onSubmit(formData); // Call the parent function with form data
    setFormData({ description: '', amount: '', date: '' , category: '', user: '', account: '', type: ''}); // Reset form after submission
    setSelectedCategory(null); // Reset selected category
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Description:</label>
        <input
          type="text"
          name="description"
          value={formData.description}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label>Amount:</label>
        <input
          type="number"
          name="amount"
          min="0.01"
          step="0.01"
          value={formData.amount}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label>Date:</label>
        <input
          type="date"
          name="date"
          value={formData.date}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label>Category:</label>
        <Creatable
          isClearable
          options={categoryOptions}
          value={selectedCategory}
          onChange={handleCategoryChange}
          onCreateOption={handleCreateCategory}
          placeholder="Select or create a category"
        />
      </div>
      <button type="submit">Submit</button>
    </form>
  );
}

export default TransactionForm;