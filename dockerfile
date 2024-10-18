# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the default Streamlit port
EXPOSE 8501

# Run the Streamlit app on container startup
CMD ["streamlit", "run", "afm_analysis/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
