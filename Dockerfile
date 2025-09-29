FROM docker.io/python:3.13-slim-trixie
MAINTAINER Computer Science House

# Install Debian packages required for dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    libffi-dev \
    libldap2-dev \
    libsasl2-dev \
    && rm -rf /var/lib/apt/lists/*

# Add application user
RUN adduser --system --group map && \
    mkdir -p /opt/map

# Add files and set permissions
ADD . /opt/map
RUN chown -R map /opt/map
WORKDIR /opt/map

# Install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Drop privileges
USER map

# Expose default port
EXPOSE 8080

# Run application with Gunicorn
CMD ["gunicorn", "--workers=2", "--bind", "0.0.0.0:8080", "app"]