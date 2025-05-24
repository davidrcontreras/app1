# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency file and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Set environment variables
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port (Flask default)
EXPOSE 5000

# Run the app
CMD ["flask", "run"]
#CMD ["pytest"]