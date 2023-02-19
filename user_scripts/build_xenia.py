import sys
import subprocess

sys.path.append("../dependencies/dev_scripts")

from build_ark import build_patch_ark

print("Building DCDX for Xenia...")

if build_patch_ark(False):
    print("Ready to run DCDX in Xenia.")
    cmd_xenia = "_xenia\\xenia_canary.exe _build\\default_xenia.xex"
    subprocess.run(cmd_xenia, shell=True, cwd="..")