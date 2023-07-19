const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());

// Route for CPU usage
app.get('/api/cpu', (req, res) => {
    // Logic to generate dummy CPU usage data
    const cpuUsage = Math.floor(Math.random() * 101); // Generates a random integer between 0 and 100
    res.json({ cpuUsage });
});

// Route for memory usage
app.get('/api/memory', (req, res) => {
    // Logic to generate dummy memory usage data
    const memoryUsage = Math.floor(Math.random() * 101); // Generates a random integer between 0 and 100
    res.json({ memoryUsage });
});

// Route for storage usage
app.get('/api/storage', (req, res) => {
    // Logic to generate dummy storage usage data
    const storageUsage = Math.floor(Math.random() * 101); // Generates a random integer between 0 and 100
    res.json({ storageUsage });
});

// Route for number of VMs
app.get('/api/vms', (req, res) => {
    // Logic to generate dummy number of VMs data
    const numVMs = Math.floor(Math.random() * 21); // Generates a random integer between 0 and 10
    res.json({ numVMs });
});

// Route for number of hosted items
app.get('/api/hosted-items', (req, res) => {
    // Logic to generate dummy number of hosted items data
    const numHostedItems = Math.floor(Math.random() * 21); // Generates a random integer between 0 and 100
    res.json({ numHostedItems });
});

// Start the server
app.listen(3000, () => {
    console.log('Dummy server is running on http://localhost:3000');
});
