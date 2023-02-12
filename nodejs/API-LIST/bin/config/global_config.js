require('dotenv').config();

const config = {
    port: process.env.PORT || 3000,
    db: {
        host: process.env.HOST || 'localhost',
        user: process.env.USER || 'root',
        password: process.env.PASSWORD || '',
        database: process.env.DB || 'quiziz',
    },
};

module.exports = config;
        