const quiz = require('./quiz');
const jobsheet = require('./jobsheet');
const router = require('express').Router();

router.use('/quiz', quiz);
router.use('/jobsheet', jobsheet);



module.exports = router;


