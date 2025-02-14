setlocal enabledelayedexpansion

if "%~1"=="" (
    echo dev/build?.
    goto :end
)

if "%~1"=="dev" (
    echo ========== Dev ===========
    for /d %%i in (view\*) do (
        set folder_name=%%~nxi
        del /f /q "%%i\_view.py"
        pyside6-uic "%%i\view.ui" -o "%%i\_view.py"
    )
    python app.py
)

if "%~1"=="build" (
    echo ========== Build ===========
    rmdir /S /Q build
    rmdir /S /Q dist
    
    pyinstaller build.spec
    mkdir dist\res
    xcopy res dist\res /E /I
    copy setting.py dist
)

:end
exit /b
echo off