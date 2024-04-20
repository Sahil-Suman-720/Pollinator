import express from "express";
import bodyParser from "body-parser";

const app = express();
const port = 4000;


app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

//Write your code here//

//CHALLENGE 1: GET All posts
app.get("/posts",(req,res)=>{
res.send("ALL OK");
});

app.listen(port,()=>{
    console.log(`Listening at port ${port}`);
})