import './App.css';
import React from 'react'; // added this for an error meesage
import PathwayView from './components/PathwayView';

function App() {
  return (
    <div className="App">
      {/* Top navigation bar needed for all activities */}
      
      {/* The main View which should hold everything else */}
      <PathwayView/>
    </div>
  );
}

export default App;