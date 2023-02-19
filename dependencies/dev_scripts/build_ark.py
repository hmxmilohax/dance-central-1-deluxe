# build_ark.py
from pathlib import Path
from subprocess import CalledProcessError
from sys import platform
import subprocess
from check_git_updated import check_git_updated

def rm_tree(pth):
    pth = Path(pth)
    for child in pth.glob('*'):
        if child.is_file():
            child.unlink()
        else:
            rm_tree(child)
    pth.rmdir()

def make_executable_binaries():
    cmd_chmod_arkhelper = "chmod +x dependencies/arkhelper".split()
    subprocess.check_output(cmd_chmod_arkhelper, shell=(platform == "win32"), cwd="..")
    cmd_chmod_dtab = "chmod +x dependencies/dtab".split()
    subprocess.check_output(cmd_chmod_dtab, shell=(platform == "win32"), cwd="..")

# if xbox is true, build for hardware
# else, build for xenia
def build_patch_ark(xbox: bool):
    # directories used in this script
    cwd = Path().absolute() # current working directory (dev_scripts)
    root_dir = cwd.parents[0] # root directory of the repo

    if platform == "win32":
        build_location = "_build\gen" if not xbox else "_build\\xbox\gen"
    else:
        build_location = "_build/gen" if not xbox else "_build/xbox/gen"
        make_executable_binaries()

    # pull the latest changes from the RB3DX repo if necessary
    if not check_git_updated():
        cmd_pull = "git pull https://github.com/hmxmilohax/dance-central-1-deluxe main".split()
        subprocess.run(cmd_pull, shell=(platform == "win32"), cwd="..")

    # configure the xenia macro depending on what you're building for
    with open(root_dir.joinpath("_ark/config/macros.dta"), "r", encoding="ISO-8859=1") as f:
        the_macros = [line for line in f.readlines()]

    for i in range(len(the_macros)):
        if "#define XENIA_SUCKS" in the_macros[i]:
            if xbox:
                the_macros[i] = ";#define XENIA_SUCKS (1)\n"
            else:
                the_macros[i] = "#define XENIA_SUCKS (1)\n"
            break
    
    with open(root_dir.joinpath("_ark/config/macros.dta"), "w", encoding="ISO-8859=1") as ff:
        ff.writelines(the_macros)

    # build the ark
    failed = False
    try:
        if platform == "win32":
            cmd_build = f"dependencies\\arkhelper.exe dir2ark _ark {build_location} -n patch_xbox -e -v 6".split()
        else:
            cmd_build = f"dependencies/arkhelper dir2ark _ark {build_location} -n patch_xbox -e -v 6".split()
        subprocess.check_output(cmd_build, shell=(platform == "win32"), cwd="..")
    except CalledProcessError as e:
        print(e.output)
        failed = True

    if not failed:
        print("Successfully built Dance Central Deluxe ARK.")
        return True
    else:
        print("Error building ARK. Check your modifications or run git_reset.py to rebase your repo.")
        return False