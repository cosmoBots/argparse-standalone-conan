from conans import ConanFile, CMake, tools


class ArgparseStandaloneConan(ConanFile):
    name = "argp-standalone"
    version = "1.0.1"
    license = "GNU LGPL v2.1"
    author = "Txinto Vaz txinto@elporis.com"
    url = "https://github.com/cosmoBots/argp-standalone-conan"
    description = "argp-standalone is another standalone version of the argp argument parsing functions from glibc by Thomas Mathys."
    topics = ("argparse", "standalone", "windows")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        self.run("git clone https://github.com/cosmoBots/argp-standalone.git")
        # This small hack might be useful to guarantee proper /MT /MD linkage
        # in MSVC if the packaged project doesn't have variables to set it
        # properly
        tools.replace_in_file("argp-standalone/CMakeLists.txt", "project(argp-standalone VERSION 1.0.0 LANGUAGES C)",
                              '''project(argp-standalone VERSION 1.0.0 LANGUAGES C)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="argp-standalone")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/argp-standalone %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="argp-standalone")
        self.copy("*.h", dst="include", src="argp-standalone/include/argp-standalone")
        self.copy("*argp-standalone.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["argp-standalone"]

