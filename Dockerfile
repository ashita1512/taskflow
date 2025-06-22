# Use the Debian Buster-based image for better compatibility
FROM python:3.9-buster

# Add the location where pip installs command-line scripts to the PATH.
ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /app

COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /app