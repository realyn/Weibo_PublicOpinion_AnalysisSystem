FROM python:3.11-slim

# Prevent Python from writing .pyc files and buffer stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Install system dependencies required by scientific Python stack, Playwright, and Streamlit
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    libgl1 \
    libglib2.0-0 \
    libgtk-3-0 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libxcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxi6 \
    libxtst6 \
    libnss3 \
    libxrandr2 \
    libxkbcommon0 \
    libasound2 \
    libx11-xcb1 \
    libxshmfence1 \
    libgbm1 \
    ffmpeg \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies first to leverage Docker layer caching
COPY requirements.txt ./ 
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    python -m playwright install chromium

# Copy application source
COPY . .

# Ensure runtime directories exist even if ignored in build context
RUN mkdir -p logs final_reports insight_engine_streamlit_reports media_engine_streamlit_reports query_engine_streamlit_reports

# Expose Flask and Streamlit ports
EXPOSE 5000 8501 8502 8503

# Default command launches the Flask orchestrator which starts Streamlit agents
CMD ["python", "app.py"]
