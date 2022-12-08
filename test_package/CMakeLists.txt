cmake_minimum_required(VERSION 3.1)
project(PackageTest C)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(argp-test argp-test.c)
set_target_properties(argp-test PROPERTIES LINKER_LANGUAGE C)
target_link_libraries(argp-test ${CONAN_LIBS})

# CTest is a testing tool that can be used to test your project.
# enable_testing()
# add_test(NAME argp-test
#          WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#          COMMAND argp-test)
