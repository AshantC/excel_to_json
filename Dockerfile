# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /app

# Expose the port (adjust if your FastAPI app runs on a different port)
EXPOSE 8000

# Command to run the FastAPI application using uvicorn
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Default command to run the application in API mode
CMD ["python", "main.py", "--mode", "api"]
