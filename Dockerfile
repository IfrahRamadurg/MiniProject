FROM ubuntu:latest
COPY ScientificCalculator.py /app/ScientificCalculator.py
COPY ScientificCalculatorMethods.py /app/ScientificCalculatorMethods.py
COPY TestScientificCalculator.py /app/TestScientificCalculator.py
RUN apt-get update && apt-get install -y python3
