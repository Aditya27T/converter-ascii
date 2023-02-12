const jobsheet = require('../bin/controllers/jobsheet');
const router = require('express').Router();

router.post('/one', jobsheet.answerOne);
router.post('/many', jobsheet.answerMany);

module.exports = router;