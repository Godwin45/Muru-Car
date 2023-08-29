# Logistic Software for Engine Quality Prediction

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This logistic software is designed to predict engine quality and determine whether an engine requires maintenance or is in great quality. The software leverages a machine learning model and goes through a complete ML Ops cycle, including integration with MLflow. The deployment options include using Docker containers on AWS or deploying to HerokuApp.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [ML Ops Cycle](#ml-ops-cycle)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Deployment](#deployment)
- [License](#license)

## Overview

Modern industries rely heavily on predictive maintenance to minimize downtime and optimize operational efficiency. This logistic software provides an intelligent solution for predicting engine quality. It integrates machine learning into operations and streamlines the development, deployment, and monitoring process.

## Features

- Engine quality prediction using a machine learning model.
- Complete ML Ops cycle for efficient development and deployment.
- Integration with MLflow for tracking and managing machine learning experiments.
- Scalable deployment options on AWS using Docker containers or on HerokuApp.
- User-friendly interface for entering engine parameters and obtaining predictions.

## ML Ops Cycle

The software follows a comprehensive ML Ops cycle, which includes the following stages:

1. Data Collection: Gather engine data for training and testing the model.
2. Data Preprocessing: Clean, preprocess, and transform data for model training.
3. Model Development: Train a machine learning model using the preprocessed data.
4. Model Evaluation: Assess model performance using relevant metrics and validation.
5. Model Deployment: Deploy the trained model using Docker containers or HerokuApp.
6. Monitoring and Logging: Continuously monitor the deployed model's performance.
7. Model Update: Periodically update the model with new data and retrain as needed.

## Getting Started

To get started, follow these steps:

1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Prepare your engine data and ensure it's properly formatted.
4. Train the machine learning model using the provided notebooks.
5. Integrate the trained model with the software's backend.
6. Set up your environment variables for integration with MLflow.

## Usage

1. Run the software using `python app.py` or `flask run`.
2. Access the software via the provided URL (e.g., http://localhost:5000).
3. Input engine parameters to obtain predictions for engine quality.

## Deployment

### AWS with Docker Container

1. Build the Docker image using `docker build -t engine-prediction .`.
2. Deploy the image to an AWS container service (ECS, EKS, etc.).
3. Configure environment variables for MLflow integration and model deployment.

### HerokuApp

1. Create a Heroku account and install the Heroku CLI.
2. Use the Heroku CLI to deploy the software: `heroku create`.
3. Push the Docker image to the Heroku container registry.
4. Configure environment variables for MLflow integration and model deployment.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
