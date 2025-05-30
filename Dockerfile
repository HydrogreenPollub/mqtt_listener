# Use an official Python runtime as a parent image
FROM python:3.12-bookworm

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./app /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run subscriber.py when the container launches
CMD ["python", "subscriber.py"]
