import React from 'react';
import Dashboard from './contents/Dashboard';
import Login from './contents/login';
import UploadContent from './contents/Upload_content';

function App() {
  return (
    <div>
      <h1>Microlearning Platform</h1>
      <Login />
      <UploadContent />
      <Dashboard />
    </div>
  );
}

export default App;
