
@echo off
cd T10-Profitable-strategies-scanner

REM Unzip the strategy scanner files
powershell -Command "Expand-Archive -Path $env:USERPROFILE\Downloads\trading_strategies_scanner_bundle_full.zip -DestinationPath . -Force"

REM Copy README
copy %USERPROFILE%\Downloads\README_Strategies_Scanner.md README.md

REM Git commands
git add .
git commit -m "Initial commit with trading strategies scanner"
git push origin main

pause
