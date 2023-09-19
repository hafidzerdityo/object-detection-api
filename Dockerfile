FROM python:3.10.8

ENV PYTHONDONTWRITEBYTECODE 1
# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Set the working directory
WORKDIR /code

# Copy the requirements.txt file
COPY ./requirements.txt /code/requirements.txt

# Install the Python dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the remaining files to the working directory
COPY ./app /code/.

# Set the command to run the main.py file
CMD ["python3", "main.py"]
