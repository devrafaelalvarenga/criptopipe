import os

folders = [
    "src/criptopipe/etl/extractor",
    "src/criptopipe/etl/transformer",
    "src/criptopipe/etl/loader",
    "src/criptopipe/dashboard",
    "src/criptopipe/config",
    "src/criptopipe/data/raw",
    "tests"
]

files = {
    "src/criptopipe/etl/__init__.py": "",
    "src/criptopipe/etl/extractor/__init__.py": "",
    "src/criptopipe/etl/extractor/api_base.py": "# Base HTTP client using aiohttp\n",
    "src/criptopipe/etl/transformer/__init__.py": "",
    "src/criptopipe/etl/transformer/clean_data.py": "# Data cleaning and transformation\n",
    "src/criptopipe/etl/loader/__init__.py": "",
    "src/criptopipe/etl/loader/postgresql.py": "# Load data into PostgreSQL\n",
    "src/criptopipe/etl/loader/mongodb.py": "# Load data into MongoDB\n",
    "src/criptopipe/etl/pipeline.py": "# ETL orchestration logic\n",
    "src/criptopipe/dashboard/__init__.py": "",
    "src/criptopipe/dashboard/app.py": "# Streamlit or Dash dashboard\n",
    "src/criptopipe/config/__init__.py": "",
    "src/criptopipe/config/settings.py": "# Settings and .env loading\n",
    "tests/test_etl.py": "# Unit tests for ETL pipeline\n",
    ".env": "# Add your environment variables here\n",
    ".env.example": "POSTGRES_URI=postgresql://user:pass@localhost:5432/dbname\nMONGO_URI=mongodb://localhost:27017\n",
    "docker-compose.yml": "# Docker Compose file for PostgreSQL and MongoDB\n",
    "README.md": "# Criptopipe\n\nProjeto ETL assíncrono para múltiplas APIs com dashboard final.\n"
}


def create_structure():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

    for path, content in files.items():
        with open(path, "w") as f:
            f.write(content)
        print(f"Created file: {path}")


if __name__ == "__main__":
    create_structure()
