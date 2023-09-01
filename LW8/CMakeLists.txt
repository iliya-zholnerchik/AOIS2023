cmake_minimum_required(VERSION 3.21)
project(Lab_8 C)

set(CMAKE_C_STANDARD 11)

include_directories(.)

add_executable(Lab_8
        associative_processor.c
        associative_processor.h
        usage_example.c)
