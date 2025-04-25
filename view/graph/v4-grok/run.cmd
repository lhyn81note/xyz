@REM setlocal enabledelayedexpansion

@REM if "%~1"=="" (
@REM     echo dev/build?.
@REM     goto :end
@REM )

@REM if "%~1"=="dev" (
@REM     echo ========== Dev ===========
@REM     for /d %%i in (view\*) do (
@REM         set folder_name=%%~nxi
@REM         del /f /q "%%i\_view.py"
@REM         pyside6-uic "%%i\view.ui" -o "%%i\_view.py"
@REM     )
@REM     python app.py
@REM )

@REM if "%~1"=="build" (
@REM     echo ========== Build ===========
@REM     rmdir /S /Q build
@REM     rmdir /S /Q dist
    
@REM     pyinstaller build.spec
@REM     mkdir dist\res
@REM     xcopy res dist\res /E /I
@REM     copy setting.py dist
@REM )

@REM :end
@REM exit /b
@REM echo off

pyside6-uic view.ui -o _view.py
python main-qss.py