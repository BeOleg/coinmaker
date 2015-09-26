#!/bin/bash
# create multiresolution windows icon
ICON_SRC=../../src/qt/res/icons/CM_LowercaseCoinName.png
ICON_DST=../../src/qt/res/icons/CM_LowercaseCoinName.ico
convert ${ICON_SRC} -resize 16x16 CM_LowercaseCoinName-16.png
convert ${ICON_SRC} -resize 32x32 CM_LowercaseCoinName-32.png
convert ${ICON_SRC} -resize 48x48 CM_LowercaseCoinName-48.png
convert CM_LowercaseCoinName-16.png CM_LowercaseCoinName-32.png CM_LowercaseCoinName-48.png ${ICON_DST}

