# Use a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and dependencies
COPY backup_script.py /app/
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script when the container starts
CMD ["python", "./backup_script.py"]
