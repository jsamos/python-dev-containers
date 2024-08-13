# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory to /code
WORKDIR /code

# Copy the requirements file
COPY requirements.txt .

# Install any needed packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app directory and necessary scripts to the container's /code directory
COPY . .

# Keep the container running so you can exec into it
CMD ["tail", "-f", "/dev/null"]