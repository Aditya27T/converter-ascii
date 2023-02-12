const models = require('../models');
const { question } = models;

const answerOne = async (req, res) => {
    const { id, answer } = req.body;
    const questions = await question.findOne({
        where: { id: id }
    });

    try {
        if (questions) {
            if (questions.answer === answer) {
                return res.status(200).json({
                    message: 'Jaawabanmu benar selamat!',
                    questions: [
                        `Correct answer: ${questions.answer}`,
                    ]
                });
            }
            return res.status(200).json({
                message: 'Wrong answer',
                correctAnswer: `Correct answer: ${questions.answer}`
            });
        }
        res.status(404).json({ message: 'Question does not exist' });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
};

const answerMany = async (req, res) => {
    const { id, answer } = req.body;

    try {
        let correct = 0;
        let wrong = 0;
        for (let i = 0; i < id.length; i++) {
            const questions = await question.findOne({
                where: { id: id[i] }
            });
            if (questions) {
                if (questions.answer === answer[i]) {
                    correct++;
                } else {
                    wrong++;
                }
            }
        }
        res.status(200).json({
            message: 'Correct: ' + correct + ' Wrong: ' + wrong,     
        });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
}

module.exports = {
    answerOne,
    answerMany
};