// App.js

import React, { useState } from 'react';
import VideoCapture from './VideoCapture';
import UserDetailsForm from './UserDetailsForm';

function App() {
  const [step, setStep] = useState(1);
  const [userData, setUserData] = useState({});

  const handleUserDetailsSubmit = (data) => {
    setUserData(data);
    setStep(2);
  };

  return (
    <div className="App">
      {step === 1 && <UserDetailsForm onSubmit={handleUserDetailsSubmit} />}
      {step === 2 && <VideoCapture userData={userData} />}
    </div>
  );
}

export default App;
