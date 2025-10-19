# Use NVIDIA CUDA base image with cuDNN support
FROM python:3.12-slim


# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies (with fallback for externally-managed-environment)
RUN pip install --no-cache-dir -r requirements.txt 

# Copy application code
COPY . .

# Create outputs directory
# RUN mkdir -p outputs



# Set the default command
CMD ["python", "app.py"]
