const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");

const app = express();
const PORT = 5000;

app.use(cors());
app.use(bodyParser.json());

const submissions = []; // in-memory store

app.post("/admission", (req, res) => {
  const { fullName, email, phone, course } = req.body;
  submissions.push({ fullName, email, phone, course });
  res.json({ message: `Thank you, ${fullName}! You’ve successfully applied for the ${course} program.` });
});

app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
