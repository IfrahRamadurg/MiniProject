FROM ubuntu:latest
COPY ScientificCalculator.py /app/ScientificCalculator.py
COPY ScientificCalculatorMethods.py /app/ScientificCalculatorMethods.py
COPY TestScientificCalculator.py /app/TestScientificCalculator.py
apt-get update && apt-get install python3
