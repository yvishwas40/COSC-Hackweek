import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [city, setCity] = useState('');
  const [weatherData, setWeatherData] = useState(null);
  const [error, setError] = useState('');

  const apiKey = '8f185ac2f82da7b1038f2cf2238a90bd'; // 🔑 Replace with your OpenWeatherMap API key

  const fetchWeather = async () => {
    if (!city) return;

    try {
      const response = await axios.get(
        `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`
      );
      setWeatherData(response.data);
      setError('');
    } catch (err) {
      setWeatherData(null);
      setError('City not found. Please try again.');
    }
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.heading}>🌦️ Weather Dashboard</h1>
      <input
        type="text"
        placeholder="Enter city name"
        value={city}
        onChange={(e) => setCity(e.target.value)}
        style={styles.input}
      />
      <button onClick={fetchWeather} style={styles.button}>Get Weather</button>

      {error && <p style={styles.error}>{error}</p>}

      {weatherData && (
        <div style={styles.card}>
          <h2>{weatherData.name}</h2>
          <p><strong>Temperature:</strong> {weatherData.main.temp}°C</p>
          <p><strong>Humidity:</strong> {weatherData.main.humidity}%</p>
          <p><strong>Forecast:</strong> {weatherData.weather[0].description}</p>
        </div>
      )}
    </div>
  );
}

const styles = {
  container: {
    textAlign: 'center',
    padding: '2rem',
    fontFamily: 'Arial, sans-serif',
  },
  heading: {
    fontSize: '2rem',
    marginBottom: '1rem',
  },
  input: {
    padding: '0.5rem',
    fontSize: '1rem',
    width: '200px',
    marginRight: '0.5rem',
  },
  button: {
    padding: '0.5rem 1rem',
    fontSize: '1rem',
    cursor: 'pointer',
  },
  card: {
    marginTop: '1.5rem',
    padding: '1rem',
    border: '1px solid #ccc',
    borderRadius: '8px',
    display: 'inline-block',
    textAlign: 'left',
  },
  error: {
    color: 'red',
    marginTop: '1rem',
  },
};

export default App;
