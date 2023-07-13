# Dance Central 1 Deluxe

![Header Image](dependencies/header.png)

# Introduction

### Dance Central 1 Deluxe is a Quality-of-Life Improvement Mod by [MiloHax](https://github.com/hmxmilohax)

This repo contains everything you need to build Dance Central 1 Deluxe for Xbox 360.

# Table of Contents  
- [Dance Central Deluxe](#dance-central-deluxe)
- [Introduction](#introduction)
- [Table of Contents](#table-of-contents)
- [Features](#features)
  - [Quality of Life](#quality-of-life)
  - [Additional Modifications](#additional-modifications)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [Repo Setup](#repo-setup)
- [Installing](#installing)
  - [Xbox 360 Hardware](#xbox-360-hardware)
  - [Xenia Emulator](#xenia-emulator) (DEV/TESTING ONLY)
- [DLC](#dlc)
  - [Installing DLC on Xenia](#installing-dlc-on-xenia)
- [Troubleshooting](#troubleshooting)
  - [Repo Troubleshooting](#repo-troubleshooting)
  - [Xbox 360 Troubleshooting](#xbox-360-troubleshooting)
  - [Xenia Troubleshooting](#xenia-troubleshooting)
- [Dependencies](#dependencies)

## Features

### Quality of Life
* Faster start time via scripting
* All difficulties, venues, and characters unlocked by default
* New menu, `Deluxe Settings`, in game for additional modifications
* No Kinect check for Xenia dev/testing

### Additional Modifications
* Hue-shifting menu

# Prerequisites

### You will need...

- **A vanilla copy of Dance Central** for Xbox 360 that you can extract onto your PC
- For Console: A **modded/hacked Xbox 360** and a way to transfer files to it, we recommend using FTP
- For Emulator (DEV/TESTING ONLY): A **mid-to-high-end PC** capable of running Xenia

# Setup

## Repo Setup
Setting up the Dance Central Deluxe repo for the first time is meant to be as easy as possible.
As well, it is designed to allow you to automatically receive updates as the repo is updated.

First, **go to the [Releases](https://github.com/hmxmilohax/dance-central-1-deluxe/releases)** of this repo.

Before you do anything else, you'll need to install [Git for Windows](https://gitforwindows.org/), [Dot Net 6.0 Runtime](https://dotnet.microsoft.com/en-us/download/dotnet/6.0/runtime), and [Python](https://www.python.org/downloads/) (version 3.9 or later). **These are ALL required in order to properly build Dance Central Deluxe**.

**Install all three of these with their default options.**.

Next, **download `_init_repo.bat`** if you're on Windows or **`_init_repo.sh`** if you're on Linux.

Now, make a new **empty** folder, **put `_init_repo` in the folder, and run it**. This will pull the repo down for you and make sure you're completely up to date. **This will take some time.**

### ***The folder should look like this once it's done:***

![Repo Folder](dependencies/images/repofolder.png)

***The Dance Central Deluxe repo is now set up!*** You are ready to **build and install install** it for your platform of choice:

  - [Xbox 360 Hardware](#xbox-360-hardware)
  - [Xenia Emulator](#xenia-emulator) (DEV/TESTING ONLY)

**If you were not able to set up the repo properly**, refer to the [Troubleshooting](#repo-troubleshooting) section.

# Installing

*Make sure you follow [Setup](#setup) first!*

## Xbox 360 Hardware

**NOTE: You WILL need a HACKED/MODDED (RGH or JTAG) Xbox 360 in order to play this mod on console. We hope this is clear.**

First, **dump or extract your Dance Central game disc** to a place where Aurora can see it.

Then, navigate to `user_scripts` and **run `build_xbox.py`**.

After that, **copy the contents** of `\_build\` to the location you extracted your disc to. Select `Yes` to overwrite the files.

If you're installing Dance Central Deluxe for the first time, it is recommended that you **rename the vanilla `default.xex` to `default_vanilla.xex`** for safety.

Make sure you **clear your system cache**, navigate to `System Settings > Storage` and press `Y` to clear the system cache.

And finally, **disable updates** for Dance Central in Aurora. Dance Central Deluxe rolls `TU2` into its base installation.

***Dance Central Deluxe should now be installed!*** Head down to [DLC](#dlc) for additional songs.

**If you're having issues**, refer to the [Troubleshooting](#xbox-360-troubleshooting) section and find your issue.

**To update Dance Central Deluxe**, repeat [the above steps](#xbox-360-hardware) (minus installing the vanilla game). You can click the `Watch` button (All Activity) to be notified about any updates that occur.

## Xenia Emulator

### ***WARNING: XENIA DOES NOT HAVE KINECT SUPPORT!!! DANCE CENTRAL IS UNPLAYABLE ON XENIA AND IS ONLY USED FOR DEVELOPMENT AND TESTING PURPOSES!!!***

First, **extract your vanilla Dance Central game disc** and copy **ONLY** the *contents* of the `gen` folder to `\_build\gen\`.

Navigate to `_xenia` and **map your controller with x360ce**. If it asks you to create `xinput1_3.dll`, create it and **rename it to `xinput1_4.dll`**.

Then, navigate to `user_scripts` and **run `build_xenia.py` to automatically update, build, and run Dance Central Deluxe.** You need to run this script every time you want to play. `run_xenia.py`, however, will not automatically build and update the game and will only run it.

***Dance Central Deluxe should now be installed!*** Head down to [DLC](#dlc) for additional songs.

**If you're having issues**, refer to the [Troubleshooting](#xenia-troubleshooting) section and find your issue.

## DLC

You can find every DLC for all Dance Central titles in this [Drive](https://drive.google.com/drive/folders/1Wc_oYoY8I-HL8XYOlau5qi99CQkPoStl).

### Installing DLC on Xenia

Download a DLC pack of your choice and open Xenia. Navigate to `File > Install Content`, and select your DLC pack(s) of choice. You can select more than one at a time.

![Xenia Songs](dependencies/images/xenia_installcontent.png)

# Troubleshooting

*If you're having issues with Dance Central Deluxe, here's where you can look for common issues and try to solve yours.*

***Below every issue are most of the possible reasons they may be happening and how you can fix them.***

## Repo Troubleshooting

### ***The `.bat`/`.py` files open and immediately close!***
* You don't have all the required dependencies installed.
    * Head back to [Repo Setup](#repo-setup) and make sure you followed the directions properly.

## Xbox 360 Troubleshooting

### ***The game doesn't get past the splash screens!***
* Make sure you copy the **ENTIRE** contents of `\_build\` to where your vanilla copy of Dance Central lives.

## Xenia Troubleshooting

### ***My game opens to a black screen!***
* You don't have a vanilla copy of Dance Central installed.
    * Extract your disc and extract **ONLY** the *contents* of the `gen` folder to `\_build\gen\`.

* Dance Central Deluxe did not build properly.
    * Make sure you have [Dot Net 6.0 Runtime](https://dotnet.microsoft.com/en-us/download/dotnet/6.0/runtime) installed.

### ***The game doesn't get past the splash screens!***
* You are not supposed to replace `default.xex` in `\_build\`, only the contents of the `gen` folder.
    * Navigate to `user_scripts` and run `git_reset.py` to rebase your repo.

### ***My controller isn't working even though I have x360ce set up!***
* Navigate to `_xenia` and rename `xinput1_3.dll` to `xinput1_4.dll`.
* Every time you launch Dance Central Deluxe, disconnect your controller from your PC and plug it back in. (This is an issue that only happens with Dance Central)

### ***The framerate is awful (below 60)!***
* Your PC is most likely not capable of running Xenia and we haven't found any settings to help optimize it.

### ***How do I use my Kinect?***
* Play on hardware.

# Dependencies

[Git for Windows](https://gitforwindows.org/) - CLI application to allow auto updating Deluxe repo files

[Dot Net 6.0 Runtime](https://dotnet.microsoft.com/en-us/download/dotnet/6.0/runtime) - Needed to run ArkHelper

[Python](https://www.python.org/downloads/) - For user script functionality (NOTE: 3.9 or newer is highly recommended!)

[Mackiloha](https://github.com/PikminGuts92/Mackiloha) - ArkHelper for building Deluxe

[dtab](https://github.com/mtolly/dtab) - For serializing `.dtb` script files
