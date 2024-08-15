add_library(libpotato STATIC)
set_target_properties(libpotato PROPERTIES PREFIX "")
set_property(TARGET libpotato PROPERTY CXX_STANDARD 20)
set_property(TARGET libpotato PROPERTY C_STANDARD 11)

set(INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../include)

if (CMAKE_SYSTEM_NAME STREQUAL "Windows")
    use_props(${PROJECT_NAME} "${CMAKE_CONFIGURATION_TYPES}" "${DEFAULT_CXX_PROPS}")
endif()

#=================== Top-Level ===================
file(GLOB_RECURSE Header_Files__Root RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} "src/*.h" "src/*.hpp")
file(GLOB_RECURSE Source_Files__Root RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} "src/*.cpp" "src/*.c")

source_group("Header Files" FILES ${Header_Files__Root})
source_group("Source Files" FILES ${Source_Files__Root})

target_sources(libpotato PRIVATE ${Header_Files__Root})
target_sources(libpotato PRIVATE ${Source_Files__Root})

#=================== Packages & Includes ===================

target_include_directories(libpotato
    PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/../extern ${CMAKE_CURRENT_BINARY_DIR}
    PUBLIC ${CMAKE_CURRENT_SOURCE_DIR} ${INCLUDE_DIR} ${ADDITIONAL_LIB_INCLUDES}
)

#=================== Linking ===================



#=================== Compile Options & Defs ===================

if (CMAKE_SYSTEM_NAME STREQUAL "Windows")
    target_compile_definitions(${PROJECT_NAME} PRIVATE
        WIN32
        _CONSOLE
        _CRT_SECURE_NO_WARNINGS
        ENABLE_DX11
        NOMINMAX
    )
endif()

if(CMAKE_SYSTEM_NAME STREQUAL "Darwin" OR CMAKE_SYSTEM_NAME STREQUAL "iOS")
    set_target_properties(${PROJECT_NAME} PROPERTIES
        XCODE_ATTRIBUTE_CLANG_ENABLE_OBJC_ARC YES
    )
endif()

if (CMAKE_SYSTEM_NAME STREQUAL "iOS")
    target_compile_definitions(libpotato PRIVATE
        $<$<CONFIG:Debug>:_DEBUG>
        $<$<NOT:$<CONFIG:Debug>>:NDEBUG>
        $<$<CONFIG:Debug>:SPDLOG_ACTIVE_LEVEL=0>
        $<$<NOT:$<CONFIG:Debug>>:SPDLOG_ACTIVE_LEVEL=1>
        __IOS__
    )

    set_xcode_property(${PROJECT_NAME} PRODUCT_BUNDLE_IDENTIFIER ${BUNDLE_ID} All)

    if(NOT SIGN_LIBRARY)
        set_target_properties(${PROJECT_NAME} PROPERTIES
            XCODE_ATTRIBUTE_CODE_SIGN_IDENTITY ""
            XCODE_ATTRIBUTE_CODE_SIGNING_ALLOWED "NO"
        )

        if(TARGET SDL2)
            set_target_properties(SDL2 PROPERTIES
                XCODE_ATTRIBUTE_CODE_SIGN_IDENTITY ""
                XCODE_ATTRIBUTE_CODE_SIGNING_ALLOWED "NO"
            )
        endif()

        set_target_properties(zip PROPERTIES
            XCODE_ATTRIBUTE_CODE_SIGN_IDENTITY ""
            XCODE_ATTRIBUTE_CODE_SIGNING_ALLOWED "NO"
        )
    endif()
else()
    target_compile_definitions(libpotato PRIVATE
        ENABLE_OPENGL
        $<$<CONFIG:Debug>:_DEBUG>
        $<$<NOT:$<CONFIG:Debug>>:NDEBUG>
        $<$<CONFIG:Debug>:SPDLOG_ACTIVE_LEVEL=0>
        $<$<NOT:$<CONFIG:Debug>>:SPDLOG_ACTIVE_LEVEL=1>
        $<$<BOOL:${USE_OPENGLES}>:USE_OPENGLES>
        $<$<BOOL:${GFX_DEBUG_DISASSEMBLER}>:GFX_DEBUG_DISASSEMBLER>
    )
endif()

if(MSVC)
    target_compile_options(libpotato PRIVATE
        $<$<CONFIG:Debug>:
            /Od;
            /Oi-
        >
        $<$<CONFIG:Release>:
            /Oi;
            /Gy
        >
        /permissive-;
        /MP;
        /sdl;
        /W3;
        ${DEFAULT_CXX_DEBUG_INFORMATION_FORMAT};
        ${DEFAULT_CXX_EXCEPTION_HANDLING};
    )
    target_link_options(libpotato PRIVATE
        $<$<CONFIG:Release>:
            /OPT:REF;
            /OPT:ICF
        >
        /SUBSYSTEM:CONSOLE
    )
endif()

if ("${CMAKE_CXX_COMPILER_ID}" MATCHES "GNU|Clang")
	target_compile_options(libpotato PRIVATE
		-Wall
		-Wextra
		-Wno-error
		-Wno-unused-variable
		-Wno-unused-parameter
		-Wno-unused-function
		-Wno-parentheses
		-Wno-narrowing
		-Wno-missing-field-initializers
        -Wno-implicit-function-declaration
        $<$<COMPILE_LANGUAGE:C,OBJC>:-Wno-int-conversion>
	)
endif()
