import express from 'express';
import bodyParser from 'body-parser';
import axios from 'axios';

const app = express();
const port = 3000;
const API_URL = "http://127.0.0.1:5000";

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Route to render the main page
app.get("/", async (req, res) => {
    try {
      res.render("index.ejs");
    } catch (error) {
      console.log(error);
      res.status(500).json({ message: "Error fetching posts" });
    }
  });
app.post("/api/predict", async (req,res) =>{
  try{
    const response = await axios.post(`${API_URL}/predict`, req.body);
    console.log(response.data.predictions);
      res.render("index.ejs", { prediction:response.data.predictions });
  } catch(error) {
      console.log(error)
      res.status(500).json({ message: "Error fetching predictions" });
  }
})
app.listen(port,()=>{
    console.log(`Listening at port ${port}`);
});