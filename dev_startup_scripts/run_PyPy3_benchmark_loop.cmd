@echo off

title "%~0"

set python=C:\pypy3-2.3.1-win32\pypy.exe
if NOT exist %python% (
    echo Error: '%python%' doesn't exists?!?
    pause
    exit 1
)

cd..

:loop
    echo on
    %python% -OO DragonPy_CLI.py benchmark
    @echo off
    pause
goto:loop