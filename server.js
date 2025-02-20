const express = require("express");
const mysql = require("mysql");
const cors = require("cors");
const bodyParser = require("body-parser");
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// MySQL Database Configuration
const db = mysql.createConnection({
    host: "localhost",
    user: "ism",
    password: "password",
    database: "tcap"
});

// Connect to MySQL Database
db.connect((err) => {
    if (err) {
        console.error("Database connection failed: " + err.stack);
        return;
    }
    console.log("Connected to the database.");
});



// Login API
app.post('/login', (req, res) => {
    const { username, password } = req.body;

    // Query to check user credentials
    const query = 'SELECT id FROM login WHERE username = ? AND password = ?';

    db.query(query, [username, password], (err, result) => {
        if (err) {
            return res.status(500).send({ message: 'Server error' });
        }

        if (result.length > 0) {
            return res.send({ message: 'Login successful', id: result[0].id });
        } else {
            return res.status(401).send({ message: 'Invalid credentials' });
        }
    });
});





let id1, algo1;
// Fetch `algo` value by ID (fix: using query parameters)
app.get("/fetch-algo", (req, res) => {
    const id = req.query.id; // Use query parameters
    console.log("Received ID:", id); // Debug log

    if (!id) {
        return res.status(400).send({ message: "ID parameter is required" });
    }

    const query = "SELECT algo FROM algo_map WHERE id = ?";
    db.query(query, [id], (err, result) => {
        id1 = id;
        if (err) {
            console.error("Error executing query:", err);
            return res.status(500).send({ message: "Server error" });
        }

        if (result.length > 0) {
            algo1 = result[0].algo;
            return res.send({ algo: result[0].algo });
        } else {
            return res.status(404).send({ message: "No record found" });
        }
    });

    const { spawn } = require("child_process");
    fname = "./image.py";
    const pythonProcess = spawn("python", ["./image.py", id]);
    

    pythonProcess.stdout.on("data", (data) => {
        console.log(`Output: ${data}`);
    });

    pythonProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });

    pythonProcess.on("close", (code) => {
        console.log(`Python script finished with code ${code}`);
    });

});

// Start the server
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});







