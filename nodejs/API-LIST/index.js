const express = require('express');
const app = express();
const cors = require('cors');
const config = require('./bin/config/global_config');
const port = config.port;
const quiz = require('./routes/index');


app.use(cors());
app.options('*', cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));


app.get('/', (req, res) => {
    res.send('Hello World!');
});
app.use(quiz);

app.listen(config.port, () => {
    console.log(`Example app listening at http://localhost:${port}`);
});
