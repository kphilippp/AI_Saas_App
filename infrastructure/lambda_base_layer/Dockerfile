FROM amazonlinux:2

# Enable Amazon Linux extras and install Python 3.8
RUN yum install -y amazon-linux-extras && \
    amazon-linux-extras enable python3.8 && \
    yum install -y python3.8 python3-pip zip && \
    yum clean all

# Create symbolic links so the commands point to the right version
RUN ln -sf /usr/bin/python3.8 /usr/bin/python && \
    ln -sf /usr/bin/python3.8 /usr/bin/python3

# Verify Python version
RUN python3 --version

# Set up PIP and create a virtual environment
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install virtualenv && \
    python3 -m venv base && \
    source base/bin/activate

# Install dependencies from requirements.txt to the deployment package
COPY ./requirements.txt .
RUN pip install -r requirements.txt -t ./python

# Install pydantic-core for a specific platform
RUN pip install pydantic-core --platform manylinux2014_x86_64 -t ./python --only-binary=:all:

# Zip it up for deployment
RUN zip -r layer.zip ./python/

# Set ENTRYPOINT
ENTRYPOINT ["/bin/bash", "-l"]
