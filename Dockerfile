# The Final Corrected Dockerfile

FROM python:3.9-slim

# Add the location where pip installs command-line scripts to the PATH.
# This MUST come before any RUN command that needs to use those scripts.
ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /app

COPY requirements.txt .

# Now, when this command runs, the system will know where to find django-admin
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /app