// server.js

const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const PORT = 5000;

// Middleware
app.use(bodyParser.json());

// API Routes
app.post('/api/userDetails', (req, res) => {
  const { name, dob, address, panCard, aadhaar, signature, incomeRange, employmentType } = req.body;
  // Process user details and store in database
  // Respond with success message or error
});

app.post('/api/videoCapture', (req, res) => {
  const { userData, videoData } = req.body;
  // Process video data and associate with user data
  // Respond with success message or error
});

// Start server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
