'use strict';
/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up(queryInterface, Sequelize) {
    await queryInterface.createTable('Questions', {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: Sequelize.INTEGER
      },
      question: {
        type: Sequelize.STRING,
        allowNull: false,
        message: 'Question is required'
      },
      a: {
        type: Sequelize.STRING,
        allowNull: false
      },
      b: {
        type: Sequelize.STRING,
        allowNull: false
      },
      c: {
        type: Sequelize.STRING,
        allowNull: false
      },
      d: {
        type: Sequelize.STRING,
        allowNull: false
      },
      answer: {
        type: Sequelize.STRING,
        allowNull: false,
        message: 'Answer is required'
      },
      categoryId: {
        type: Sequelize.INTEGER,
        allowNull: false,
        message: 'Category is required',
        references: {
          model: 'Categories',
          key: 'id'
        }
      },
      levelId: {
        type: Sequelize.INTEGER,
        allowNull: false,
        message: 'Level is required',
        references: {
          model: 'Levels',
          key: 'id'
        }
      },
      createdAt: {
        allowNull: false,
        type: Sequelize.DATE
      },
      updatedAt: {
        allowNull: false,
        type: Sequelize.DATE
      }
    });
  },
  async down(queryInterface, Sequelize) {
    await queryInterface.dropTable('Questions');
  }
};