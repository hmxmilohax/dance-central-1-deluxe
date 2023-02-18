git pull https://github.com/hmxmilohax/dance-central-1-deluxe main
@echo OFF
echo:Building Dance Central Deluxe patch arks.
"%~dp0dependencies/arkhelper" dir2ark "%~dp0\_ark" "%~dp0\_build\gen" -n "patch_xbox" -e -v6 >nul
echo:Wrote Dance Central Deluxe patch arks.
echo:Complete. Launching Xenia. Enjoy Dance Central Deluxe
"%~dp0\_xenia\xenia_canary" "%~dp0\_build\default_xenia.xex"
pause