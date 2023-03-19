#!/bin/sh

set -xe

echo $1

cc -Wall -Wextra -Werror -o bin/main src/main.c

./bin/main

feh output.ppm
