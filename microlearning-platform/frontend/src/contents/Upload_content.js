import React, { useState } from 'react';
import axios from 'axios';

function UploadContent() {
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:5000/upload', formData);
      setSummary(response.data.summary);
    } catch (error) {
      console.error('Error uploading file:', error);
    }
  };

  return (
    <div>
      <h1>Upload Content</h1>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
      {summary && (
        <div>
          <h2>Summary</h2>
          <p>{summary}</p>
        </div>
      )}
    </div>
  );
}

export default UploadContent;
