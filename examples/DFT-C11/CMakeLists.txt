cmake_minimum_required(VERSION 3.14)
project(DFT_C11 C)

set(CMAKE_C_STANDARD 11)

add_executable(DFT_C11 main.c)
add_executable(DFT_C11_Golfed golfed_main.c)