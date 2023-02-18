git pull https://github.com/hmxmilohax/dance-central-1-deluxe main
@echo OFF
echo:Make sure your 1.0 vanilla ark files are in _build/gen/
del "%~dp0\_build\gen\main_xbox.hdr"
del "%~dp0\_build\gen\main_xbox_7.ark"
xcopy "%~dp0\dependencies\_rebuild_files\main_xbox.hdr" "%~dp0\_build\gen" >nul
echo:Building Dance Central Deluxe patch arks.
echo:The "Unhandled exception" below is expected, and does not indicate failure.
"%~dp0dependencies/arkhelper" patchcreator -a "%~dp0\_ark" -o "%~dp0\_build" "%~dp0\_build\gen\main_xbox.hdr" >nul
echo:Wrote Dance Central Deluxe patch arks.
echo:Complete. Launching Xenia. Enjoy Dance Central Deluxe
"%~dp0\_xenia\xenia_canary" "%~dp0\_build\default_xenia.xex"
pause