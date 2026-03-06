import { useState } from 'react';
import { invoke } from '@tauri-apps/api/core';

function App() {
  const [greeting, setGreeting] = useState<string>('');
  const [error, setError] = useState<string>('');

  async function handleGreet() {
    try {
      setError('');
      const result = await invoke<string>('greet', { name: 'World' });
      setGreeting(result);
    } catch (err) {
      setError(String(err));
    }
  }

  return (
    <div className="App">
      <h1>Palate Detector</h1>
      <p>License Plate Recognition Desktop App</p>

      <div>
        <button onClick={handleGreet}>Greet</button>
      </div>

      {greeting && <p>{greeting}</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
}

export default App;