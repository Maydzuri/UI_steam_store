@echo off
echo ========================================
echo Starting services with Docker Compose...
echo ========================================
docker-compose up -d

echo.
echo ========================================
echo Building test Docker image...
echo ========================================
docker build -t university-tests .

echo.
echo ========================================
echo Waiting for services to be ready...
echo ========================================
docker run --rm ^
    --network ui_steam_store_default ^
    -v %cd%:/app ^
    university-tests ^
    python wait_for_services.py

echo.
echo ========================================
echo Running tests in Docker...
echo ========================================
docker run --rm ^
    --network ui_steam_store_default ^
    -v %cd%/allure-results:/app/allure-results ^
    -e AUTH_SERVICE_API_URL=http://auth:8000 ^
    -e UNIVERSITY_SERVICE_API_URL=http://university:8000 ^
    university-tests ^
    pytest tests/ -v --alluredir=allure-results

echo.
echo ========================================
echo Stopping services...
echo ========================================
docker-compose down

echo.
echo ========================================
echo Generating Allure report...
echo ========================================
allure generate ./allure-results -o ./allure-report --clean

echo.
echo ========================================
echo Done! Report available at:
echo ./allure-report/index.html
echo ========================================
