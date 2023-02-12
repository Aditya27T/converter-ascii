quizModels = require('../models');
const { question, category, level } = quizModels;

const getQuestions = async (req, res) => {
    try {
        const questions = await question.findAll({
            include: [
                {
                    model: category,
                    as: 'category'
                },
                {
                    model: level,
                    as: 'level'
                }
            ]
        });
        res.status(200).json({
            message: 'Questions retrieved successfully',
            questions: questions.map(question => {
                return {
                    id: question.id,
                    question: question.question,
                    answer: question.answer,
                    category: question.category,
                    level: question.level
                }
            })
        });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
};

const getQuestionById = async (req, res) => {
    try {
        const { id } = req.params;
        const questions = await question.findOne({
            where: { id: id },
            include: [
                {
                    model: category,
                    as: 'category'
                },
                {
                    model: level,
                    as: 'level'
                }
            ]
        });
        if (questions) {
            return res.status(200).json({
                message: 'Question retrieved successfully',
                questions: questions
            });
        }
        res.status(404).json({ message: 'Question does not exist' });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
};

const createQuestion = async (req, res) => {
    try {
        const questions = await question.create(req.body);
        res.status(201).json({
            message: 'Question created successfully',
            questions: questions
        });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
}

const updateQuestion = async (req, res) => {
    try {
        const { id } = req.params;
        const [updated] = await question.update(req.body, {
            where: { id: id }
        });
        if (updated) {
            const updatedQuestion = await question.findOne({ where: { id: id } });
            return res.status(200).json({
                message: 'Question updated successfully',
                questions: updatedQuestion
            });
        }
        throw new Error('Question not found');
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
};

const deleteQuestion = async (req, res) => {
    try {
        const { id } = req.params;
        const deleted = await question.destroy({
            where: { id: id }
        });
        if (deleted) {
            return res.status(204).send("Question deleted");
        }
        throw new Error("Question not found");
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
};

const createLevel = async (req, res) => {
    try {
        const levels = await level.create(req.body);
        res.status(201).json({
            message: 'Level created successfully',
            levels: levels
        });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
}

const createCategory = async (req, res) => {
    try {
        const categories = await category.create(req.body);
        res.status(201).json({
            message: 'Category created successfully',
            categories: categories
        });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
}

const getbyCategory = async (req, res) => {
    try {
        const { id } = req.params;
        const questions = await question.findAll({
            where: { id: id },
            include: [
                {
                    model: category,
                    as: 'category'
                },
                {
                    model: level,
                    as: 'level'
                }
            ]
        });
        if (questions) {
            return res.status(200).json({
                message: 'Question retrieved successfully',
                questions: questions
            });
        }
        res.status(404).json({ message: 'Question does not exist' });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
};

module.exports = {
    getQuestions,
    getQuestionById,
    createQuestion,
    updateQuestion,
    deleteQuestion,
    createLevel,
    createCategory,
    getbyCategory
};


