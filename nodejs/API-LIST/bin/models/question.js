'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class Question extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  }
  Question.init({
    question: {
      type: DataTypes.STRING,
      allowNull: false,
      message: 'Question is required'
    },
    a: {
      type: DataTypes.STRING,
      allowNull: false
    },
    b: {
      type: DataTypes.STRING,
      allowNull: false
    },
    c: {
      type: DataTypes.STRING,
      allowNull: false
    },
    d: {
      type: DataTypes.STRING,
      allowNull: false
    },
    answer: {
      type: DataTypes.STRING,
      allowNull: false,
      message: 'Answer is required'
    },
    categoryId: {
      type: DataTypes.INTEGER,
      allowNull: false,
      message: 'Category is required'
    },
    levelId: {
      type: DataTypes.INTEGER,
      allowNull: false,
      message: 'Level is required'
    }

  }, {
    sequelize,
    modelName: 'Question',
    tableName: 'questions'
  });
  return Question;
};