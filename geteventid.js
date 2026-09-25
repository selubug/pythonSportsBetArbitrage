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

const fetchDataOnce = async () => {
    try {
        console.log("Fetching data...");
        const eventId = 1419211461;  // Example event_id
        const pinnacleApiUrl = `https://pinnacle-odds.p.rapidapi.com/kit/v1/markets?sport_id=3&is_have_odds=true`;

        const response = await fetch(pinnacleApiUrl, {
            method: 'GET',
            headers: {
                'x-rapidapi-host': 'pinnacle-odds.p.rapidapi.com',
                'x-rapidapi-key': 'bdc3d7bd21msh6bab73819d2bf38p13a880jsn2c5acc778970'
            }
        });
        
        const data = await response.json();
       // console.log("Data fetched from Pinnacle API:", data);
       if (data && data.events) {
          const filteredEvents = data.events.filter(event => event.league_name === 'NBA');
          console.log(filteredEvents);  
          }

       
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
};

// Run the fetchDataOnce function once
fetchDataOnce();
