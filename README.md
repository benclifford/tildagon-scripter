# Scripter 

![Screenshot of scriper UI](imgs/screenshot.jpg)

## Install

You can install this on your badge in the App Store,
under Apps/Scripter or at:
https://apps.badge.emfcamp.org/apps/00342232/

## Web emulator

You can try this in your browser in the online
emulator:

https://emulator.badge.emfcamp.org/#Apps/Scripter


## The default program

The default program will trigger a scripted sequence of LED flashes. Then it will
wait for:

* any button (except CANCEL) to be pressed and do some more flashing every time
  that happens.

* the badge to be turned upright (from e.g. flat on a table) and turn the
  LEDs green

When you first load the app, it will load the default program and go into edit mode.

## Edit mode

Edit mode is indicated by a blue ring around the edge of the screen.

CANCEL will exit the app.

UP/DOWN will scroll through the default program.

CONFIRM will bring up a menu of things you can do, either to the current
step or to the program as a whole.

You can:

* delete steps
* insert steps
* play the program
* play the program in background - this will play like play mode, but return
  you to the App Launcher so you can do other things. Your program will continue
  running (although 'When button pushed' events won't happen). You can go back
  into normal play mode by navigating back into the scripter app.

## Insert Step dialogs

When you insert a step, you will get an editor specific to the kind of step.
Some steps need no editor, but:

The colour picker: scroll UP and DOWN to choose from a very limited palette:
red, green, blue, off/black. choose CONFIRM to select that colour.

The delay picker: use the menu to pick one of several preconfigured delays.

## Play mode

When you first load the app, it will load a default program and start
playing.

Play mode is indicated by a green ring around the edge of the screen.

Press CANCEL (top left) button to stop the program and go into edit mode.


## Developer Install

```
./install-badge.sh
```

installs on a badge locally, but is hard-coded to
my development environment. Basically it copies all the .py files over.

```
./mypy.sh
```

runs the mypy type checker against the codebase, again hard coded to
my own environment.
