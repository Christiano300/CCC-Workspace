@echo off
@REM if "%1"=="" (
@REM     echo Usage: ccc [action]
@REM     echo Actions:
@REM     echo   init      Initialize the project. Will give you a prompt for levels and language
@REM     echo   import    After downloading level*.zip files into the levels/ directory, use this to extract them
@REM     echo   test      Tests the current level against the provided examples. Shows a diff editor if it fails.
@REM     echo   run       Runs the current level on all input files and puts them in the out/ directory. Keep the console open! If there are errors you can abort and nothing will happen. If everything works, the workspace will advance to the next level.
@REM     echo   skip      Skips the current level and advances to the next one.
@REM     echo   help      Shows this help message.
@REM )
@echo off
setlocal enabledelayedexpansion

REM -----------------------------------------------------------------
REM Require at least one argument
REM -----------------------------------------------------------------
if "%~1"=="" (
    echo Print help message here
    exit /b 1
)

set "forward=%*"

REM -----------------------------------------------------------------
REM Symlink resolver
REM Writes the resolved path into the variable name passed as argument 2
REM Example: call :resolve "%candidate%" resolved
REM -----------------------------------------------------------------
:resolve
setlocal
set "input=%~1"

for /f "usebackq delims=" %%R in (`powershell -NoProfile -Command ^
    "(Get-Item -LiteralPath '%input%' -Force | Resolve-Path -LiteralPath).ProviderPath" 2^>nul`) do (
    endlocal & set "%2=%%R" & goto :eof
)

endlocal & set "%2=" & goto :eof



REM -----------------------------------------------------------------
REM Try python3.exe and python.exe from PATH
REM -----------------------------------------------------------------
for %%B in (python3.exe python.exe) do (
    for /f "usebackq delims=" %%P in (`where %%B 2^>nul`) do (
        set "candidate=%%~fP"

        call :resolve "!candidate!" resolved

        echo "!resolved!" | find /i "AppInstallerPythonRedirector.exe" >nul
        if !errorlevel! == 0 (
            REM skip redirector
            continue
        )

        if exist "!candidate!" (
            "!candidate!" scripts\ccc.py %forward%
            exit /b 0
        )
    )
)



REM -----------------------------------------------------------------
REM Fallback: %localappdata%\Python\bin\python.exe
REM -----------------------------------------------------------------
if exist "%localappdata%\Python\bin\python.exe" (
    "%localappdata%\Python\bin\python.exe" scripts\ccc.py %forward%
    exit /b 0
)



REM -----------------------------------------------------------------
REM Fallback: %localappdata%\Programs\Python\*
REM -----------------------------------------------------------------
if exist "%localappdata%\Programs\Python" (
    for /f "delims=" %%D in ('dir /b "%localappdata%\Programs\Python" 2^>nul') do (
        if exist "%localappdata%\Programs\Python\%%D\python.exe" (
            "%localappdata%\Programs\Python\%%D\python.exe" scripts\ccc.py %forward%
            exit /b 0
        )
    )
)

echo No usable Python installation found.
exit /b 1
