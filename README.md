# Dance Central Deluxe

![Header Image](dependencies/header.png)

# Table of Contents  
- [Dance Central Deluxe](#dance-central-deluxe)
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
  - [Features](#features)
    - [Quality of Life](#quality-of-life)
  - [Setup](#setup)
    - [Repo Setup](#repo-setup)
  - [Install](#install)
    - [Xbox](#xbox)
    - [Xenia Emulator](#xenia-emulator)
  - [DLC](#dlc)
  - [Dependencies](#dependencies)

## Introduction

This Repo contains everything you need to build an ARK for Dance Central Deluxe for Xbox 360.

## Features

### Quality of Life
* Faster start time via scripting
* All difficulties, venues, and characters unlocked by default
* New menu, `Deluxe Settings`, in game for additional modifications
* No Kinect check for Xenia

### Additional Modifications
* Hue-shifting menu

## Setup

NOTE: You WILL need a modded/hacked console to play this mod on console. We hope this is clear.

### Repo Setup
Setting up the Dance Central Deluxe repo for the first time is meant to be as easy as possible.
As well, it is designed to allow you to automatically receive updates as the repo is updated.

Simply go to the [Releases](https://github.com/hmxmilohax/dance-central-1-deluxe/releases) of this repo and grab the `_init_repo` script for your platform. Currently there are .bat files for Windows and .sh files for Linux.

Included on the release page for ease of install are a couple dependencies, [Git for Windows](https://gitforwindows.org/), and [Dot Net 6.0 Runtime](https://dotnet.microsoft.com/en-us/download/dotnet/6.0/runtime).
Git is required for you to take advantage of auto updating via GitHub pulls. Dot Net is required to build an ARK/HDR file, the archive format the game needs to run. You cannot run any Deluxe title without building an ARK first.

In addition to this, you will also need to download Python in order to utilize the provided user scripts. These scripts were written and tested using Python 3.9, so it's highly recommended to get that version of Python or newer.

You can setup Git with all default options, same with Dot Net.

Once the dependencies are installed, run `_init_repo.bat` in an **empty folder**. Git will pull the repo and make sure you are completely up to date.

From then on simply run the `build .py` corresponding to the platform you are building for. This script will pull the repo again for updates, and build the ARK for you and spit it out in `\_build\gen`

## Install

### Xbox

**NOTE: You WILL need a modded/hacked console to play this mod on console. We hope this is clear.**

On Xbox, copy the `gen` folder and the xex from `_build/` to the same location your base copy of Dance Central lives.

If installing for the first time, make sure you rename the vanilla `default.xex` to `default_vanilla.xex` for safety.

Make sure you clear your system cache. Do this by navigating to `System Settings` > `Storage` and press Y to clear the system cache.

Also make sure to `disable` any enabled updates for Dance Central in Aurora. Dance Central Deluxe rolls TU2 into its base installation.

Run the build script again to pull any new updates committed to the repo and rebuild a new ARK/HDR.

### Xenia Emulator

To install on Xenia, copy your vanilla Xbox 360 1.0 ARKs to `\_build\gen`

then just navigate to `user_scripts` and run `build_xenia.py` to automatically build and run Dance Central Deluxe.

## DLC

You can find DLC packs for all Dance Central titles in [this drive](https://drive.google.com/drive/folders/1Wc_oYoY8I-HL8XYOlau5qi99CQkPoStl).

On Xenia, launch it and navigate to `File` > `Install Content` and select all the DLC files you want to install. You can select more than one at a time.

## Dependencies

[Git for Windows](https://gitforwindows.org/) - CLI application to allow auto updating DCDX repo files

[Dot Net 6.0 Runtime](https://dotnet.microsoft.com/en-us/download/dotnet/6.0/runtime) - Needed to run ArkHelper

[Mackiloha](https://github.com/PikminGuts92/Mackiloha) - ArkHelper for building Dance Central ARK - SuperFreq for building .bmp_xbox images

[dtab](https://github.com/mtolly/dtab) - For serializing Dance Central DTB files

[python](https://www.python.org/downloads/) - For overall user script functionality (NOTE: 3.9 or newer is highly recommended!)
