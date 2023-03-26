#!/bin/sh

set -xe

yasm -felf64 hello.asm
ld -o helloASM hello.o
./helloASM
