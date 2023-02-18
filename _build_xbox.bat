set FAILED_ARK_BUILD=0
git pull https://github.com/hmxmilohax/dance-central-1-deluxe main
@echo off
echo:
echo:Building Xbox ARK
"%~dp0dependencies/arkhelper" dir2ark "%~dp0_ark" "%~dp0_build\gen" -n "patch_xbox" -e -v 6 >nul
if %errorlevel% neq 0 (set FAILED_ARK_BUILD=1)
echo:
if %FAILED_ARK_BUILD% neq 1 (echo:Successfully built Dance Central Deluxe ARK. You may find the files needed to place on your Xbox 360 in /_build/Xbox/)
if %FAILED_ARK_BUILD% neq 0 (echo:Error building ARK. Check your modifications or run _git_reset.bat to rebase your repo.)
echo:
pause