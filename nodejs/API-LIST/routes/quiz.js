const quiz = require('../bin/controllers/quiz');
const router = require('express').Router();

router.get('/', quiz.getQuestions);
router.get('/:id', quiz.getQuestionById);
router.post('/', quiz.createQuestion);
router.put('/:id', quiz.updateQuestion);
router.delete('/:id', quiz.deleteQuestion);

router.post('/level', quiz.createLevel);
router.post('/category', quiz.createCategory);
router.get('/category/:id', quiz.getbyCategory);

module.exports = router;