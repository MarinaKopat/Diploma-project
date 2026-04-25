@echo off
chcp 65001 > nul

if exist allure-results rmdir /s /q allure-results
if exist data rmdir /s /q data

set PYTHONPATH=%CD%

echo [1/2] Запуск всех тестов (API и UI)...
python -m pytest

echo [2/2] Формирование отчета Allure...
allure serve allure-results