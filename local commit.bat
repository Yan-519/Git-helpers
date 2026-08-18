@echo off

echo =========================
echo          Commit
echo =========================
echo.

set /p "commit_message=Commit message: "

:empty_message
if "%commit_message%"=="" (
    echo.
    echo Commit message cannot be empty.
    set /p "commit_message=Commit message: "

    goto :empty_message
)

echo.
choice /C YN /M "Are you sure you want to push?"
if errorlevel 2 exit /b 0

echo.
echo Adding files...
git add .
if errorlevel 1 (
    echo Git add failed.
    pause
    exit /b 1
)

echo.
echo Committing...
git commit -m "%commit_message%"
if errorlevel 1 (
    echo Git commit failed.
    pause
    exit /b 1
)