import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [form, setForm] = useState({
    fullName: '',
    email: '',
    phone: '',
    course: '',
  });

  const [message, setMessage] = useState('');

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('http://localhost:5000/admission', form);
      setMessage(res.data.message);
      setForm({ fullName: '', email: '', phone: '', course: '' });
    } catch (err) {
      setMessage('Error submitting the form');
    }
  };

  return (
    <div className="container">
      <h1>College Admission Form</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" name="fullName" placeholder="Full Name" value={form.fullName} onChange={handleChange} required />
        <input type="email" name="email" placeholder="Email Address" value={form.email} onChange={handleChange} required />
        <input type="tel" name="phone" placeholder="Phone Number" value={form.phone} onChange={handleChange} required />
        <select name="course" value={form.course} onChange={handleChange} required>
          <option value="">Select Course</option>
          <option value="Computer Science">Computer Science</option>
          <option value="Mechanical Engineering">Mechanical Engineering</option>
          <option value="Business Administration">Business Administration</option>
        </select>
        <button type="submit">Apply</button>
      </form>
      {message && <p className="confirmation">{message}</p>}
    </div>
  );
}

export default App;
