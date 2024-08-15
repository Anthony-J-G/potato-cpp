cmake_minimum_required(VERSION 3.24.0)

option(NON_PORTABLE "Build a non-portable version" OFF)

if(CMAKE_SYSTEM_NAME STREQUAL "iOS")
    option(SIGN_LIBRARY "Enable xcode signing" OFF)
    option(BUNDLE_ID "Bundle ID for xcode signing" "com.example.libpotato")
    set(CMAKE_POLICY_DEFAULT_CMP0077 NEW)
endif()

project(libpotato LANGUAGES C CXX)

if (CMAKE_SYSTEM_NAME STREQUAL "Darwin" OR CMAKE_SYSTEM_NAME STREQUAL "iOS")
    enable_language(OBJCXX)
    set(CMAKE_OBJC_FLAGS "${CMAKE_OBJC_FLAGS} -fobjc-arc")
    set(CMAKE_OBJCXX_FLAGS "${CMAKE_OBJCXX_FLAGS} -fobjc-arc")
endif()

if (CMAKE_SYSTEM_NAME STREQUAL "Windows")
	set(CMAKE_MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>")
endif()

include(External/cmake/Utils.cmake)
set(ADDITIONAL_LIB_INCLUDES "")

# ========= Configuration Options =========
set(CMAKE_EXPORT_COMPILE_COMMANDS 1)

# =========== Dependencies =============


# === Platform Specific Configuration ===
if(CMAKE_SYSTEM_NAME STREQUAL "iOS")
    include(External/cmake/ios-toolchain-populate.cmake)
endif()

# =========== Sources =============
add_subdirectory("Source/libpotato")
add_subdirectory("Source/testpotato")
