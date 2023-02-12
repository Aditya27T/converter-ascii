require('dotenv').config();
const Sequelize = require('sequelize');
const { development, test, production} = require('../config/config.json');

const conn = 
    process.env.NODE_ENV === 'production' ? production :
    process.env.NODE_ENV === 'test' ? test : development;

const sequelize = new Sequelize(
    conn.database,
    conn.username,
    conn.password,
    {
        host: conn.host,
        dialect: conn.dialect,
        pool: {
            max: 5,
            min: 0,
            acquire: 30000,
            idle: 10000
        },
    }
);

const db = {};

db.Sequelize = Sequelize;
db.sequelize = sequelize;

db.level = require('./level')(sequelize, Sequelize);
db.category = require('./category')(sequelize, Sequelize);
db.question = require('./question')(sequelize, Sequelize);

db.question.belongsTo(db.level);
db.question.belongsTo(db.category);
db.level.hasMany(db.question);
db.category.hasMany(db.question);




module.exports = db;