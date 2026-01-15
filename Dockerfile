FROM python:3.10-slim

# Create non-root user
RUN useradd -m user
USER user

WORKDIR /app

# Copy requirements and install
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY --chown=user . .

# Expose Hugging Face port
EXPOSE 7860

# Run Flask app
CMD ["python", "app.py"]
