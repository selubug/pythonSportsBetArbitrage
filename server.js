import express from 'express';
import bodyParser from 'body-parser';
import fetch from 'node-fetch';  // Using import instead of require
import dotenv from 'dotenv';  // Importing dotenv using ES Module syntax

dotenv.config();  // Load environment variables from the .env file

const app = express();
const port = 3000;

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Polymarket API endpoint
const clobApiUrl = "https://clob.polymarket.com/order";

// SSE endpoint to notify frontend
app.get('/events', (req, res) => {
    res.setHeader('Content-Type', 'text/event-stream');
    res.setHeader('Cache-Control', 'no-cache');
    res.setHeader('Connection', 'keep-alive');
    res.flushHeaders();  // Flush headers to keep the connection open

    // Function to check Pinnacle API every second
    const interval = setInterval(async () => {
        try {
            console.log("teeeee")
            const eventId = 1603650230;  // Example event_id
            const pinnacleApiUrl = `https://pinnacle-odds.p.rapidapi.com/kit/v1/details?event_id=${eventId}`;

            const response = await fetch(pinnacleApiUrl, {
                method: 'GET',
                headers: {
                    'x-rapidapi-host': 'pinnacle-odds.p.rapidapi.com',
                    'x-rapidapi-key': 'bdc3d7bd21msh6bab73819d2bf38p13a880jsn2c5acc778970'
                }
            });
            
            const data = await response.json();
            console.log("Data fetched from Pinnacle API:", data);
           
            if (data && data.odds) {
                const conditionMet = data.odds.home > 1.5;
                if (conditionMet) {
                    res.write('data: {"message": "Condition met, ready to place order!"}\n\n');
                    await placeOrder(0.5, 100, "BUY", "your_token_id");  // Place the order
                
                }
            }
        } catch (error) {
            console.error("Error fetching Pinnacle API:", error);
        }
    }, 1000);
  
    req.on('close', () => {
        clearInterval(interval);
        res.end();
    });
});


app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
