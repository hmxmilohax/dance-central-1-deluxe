from pathlib import Path
import sys
import subprocess

sys.path.append("../dependencies/dev_scripts")

from build_ark import build_patch_ark

sys.path.append("../dependencies/dev_scripts")
from check_git_updated import check_git_updated

# get the current working directory
cwd = Path().absolute()
root_dir = Path(__file__).parents[1] # root directory of the repo

cmd_xenia = "_xenia\\xenia_canary.exe _build\\default_xenia.xex"

if check_git_updated():
    res = True
    if not root_dir.joinpath("_build/gen/patch_xbox_0.ark").is_file():
        print("DCDX ark not found, building it now...")
        res = build_patch_ark(False)
    if res:
        print("Ready to run DCDX in Xenia.")
        subprocess.run(cmd_xenia, shell=True, cwd="..")
else:
    print("Local repo out of date, pulling and building an updated DCDX ark now...")
    if build_patch_ark(False):
        print("Ready to run DCDX in Xenia.")
        subprocess.run(cmd_xenia, shell=True, cwd="..")