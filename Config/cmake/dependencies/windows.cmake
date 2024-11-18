include(FetchContent)

# If we are using windows, a lot of the grunt work of the dependency fetching can be done using
# VCPKG. Currently this set up is very fragile and doesn't support GCC/MinGW, needs work

if (USE_AUTO_VCPKG)
	include(cmake/automate-vcpkg.cmake)

	if ("${CMAKE_VS_PLATFORM_NAME}" STREQUAL "Win32")
		set(VCPKG_TRIPLET x86-windows-static)
		set(VCPKG_TARGET_TRIPLET x86-windows-static)
	elseif ("${CMAKE_VS_PLATFORM_NAME}" STREQUAL "x64")
		set(VCPKG_TRIPLET x64-windows-static)
		set(VCPKG_TARGET_TRIPLET x64-windows-static)
	endif()

	# vcpkg_bootstrap()
	# vcpkg_install_packages(<dependency port 1> <dependency port 2> ... <dependency port n>)
endif()