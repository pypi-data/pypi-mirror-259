@echo off
setlocal enabledelayedexpansion

REM Delete last build folders
for %%d in (.\dist\ .\statesxt.egg-info\) do (
    if exist "%%d" (
        rd /s /q "%%d"
        echo Folder %%d deleted
    )
)

@REM Build: to create new build folders
py -m build

@REM Read .env file to get Token
for /f "tokens=1,* delims==" %%a in ('type .env') do set "%%a=%%b"

@REM Split REPO and TOKEN values by comma into arrays
set i=0
for %%a in (!REPO!) do (
    set "REPO_ARRAY[!i!]=%%a"
    set /a "i+=1"
)
set i=0
for %%b in (!TOKEN!) do (
    set "TOKEN_ARRAY[!i!]=%%b"
    set /a "i+=1"
)

REM Pair REPO and TOKEN, then publish
set /a "array_length=!i! - 1"
for /l %%i in (0,1,!array_length!) do (
    echo Repo: !REPO_ARRAY[%%i]!
    echo Token: !TOKEN_ARRAY[%%i]!

    py -m twine upload --repository !REPO_ARRAY[%%i]! dist/* --username __token__ --password !TOKEN_ARRAY[%%i]!
)