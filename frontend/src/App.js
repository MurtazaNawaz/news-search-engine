import React, { useState } from "react";

function App() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    if (!query) return;
    try {
      const res = await fetch(`http://127.0.0.1:8000/search?q=${query}`);
      const data = await res.json();
      setResults(data.items || []);
    } catch (err) {
      console.error("Error fetching search results:", err);
      setResults([]);
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>News Search</h1>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search news..."
      />
      <button onClick={handleSearch}>Search</button>

      <ul>
        {results.length > 0 ? (
          results.map((item) => (
            <li key={item.id}>
              <strong>{item.title}</strong> - {item.category}
            </li>
          ))
        ) : (
          <li>No results</li>
        )}
      </ul>
    </div>
  );
}

export default App;
