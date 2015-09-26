#!/bin/sh
# Copyright (c) 2013 The CM_UppercaseCoinName Core developers
# Distributed under the MIT/X11 software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.
#
# Helper script for pull-tester.
#Param 1: path to CM_LowercaseCoinName srcroot
#Param ...: arguments for build-test.sh

if [ $# -lt 1 ]; then
  echo "usage: $0 [CM_LowercaseCoinName srcroot] build-test arguments..."
fi

killall -q CM_LowercaseCoinName-cli
killall -q CM_LowercaseCoinNamed

cd $1
shift

./autogen.sh
./configure
./qa/pull-tester/build-tests.sh "$@"
