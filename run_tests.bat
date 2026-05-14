                                        @echo off
REM ============================================
REM  SauceDemo Test Runner - Kolay Kullanim
REM ============================================
REM
REM  Kullanim:
REM    run_tests.bat              -> Tum testleri calistir + Allure raporu ac
REM    run_tests.bat cart         -> Sadece Cart testleri
REM    run_tests.bat checkout     -> Sadece Checkout testleri
REM    run_tests.bat sorting      -> Sadece Sorting testleri
REM    run_tests.bat login        -> Sadece Login testleri
REM    run_tests.bat performance  -> Sadece Performance testleri
REM    run_tests.bat report       -> Sadece raporu ac (test calistirmadan)
REM ============================================

set ALLURE_CMD=%TEMP%\allure\allure-2.32.0\bin\allure.bat

if "%1"=="report" (
    echo [*] Allure raporu aciliyor...
    call "%ALLURE_CMD%" serve reports\allure-results
    goto :end
)

if "%1"=="" (
    echo [*] Eski test sonuclari temizleniyor...
    if exist "reports\allure-results" rmdir /s /q "reports\allure-results"
    
    echo [*] TUM testler calistiriliyor...
    py -m behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results -f pretty --no-logcapture --no-capture
) else (
    echo [*] Eski test sonuclari temizleniyor...
    if exist "reports\allure-results" rmdir /s /q "reports\allure-results"

    echo [*] %1 testleri calistiriliyor...
    py -m behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results -f pretty --no-logcapture --no-capture features/%1.feature
)

echo.
echo [*] Testler tamamlandi! Allure raporu aciliyor...
call "%ALLURE_CMD%" serve reports\allure-results

:end
echo [*] Bitti!
