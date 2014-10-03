#!/bin/sh

PREFS_SRC="/Library/Application Support/Google/Chrome/Default/Preferences"
PREFS_TGT_DIR="$HOME/Library/Application Support/Google/Chrome/Default"
PREFS_TGT_FILE="$PREFS_TGT_DIR/Preferences"

# make our user's chrome profile dir if one doesn't already exist
[ -d "$PREFS_TGT_DIR" ] || mkdir -p "$PREFS_TGT_DIR"

# if prefs file doesn't already exist, copy it
[ -e "$PREFS_TGT_FILE" ] || cp "$PREFS_SRC" "$PREFS_TGT_FILE"

# yeah thanks
touch "$PREFS_TGT_DIR/../First Run"
