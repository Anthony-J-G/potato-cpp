-- Main Project Script (premake5.lua)

workspace "SampleCodebase"
   architecture "x64"
   configurations { "Debug", "Release", "Dist" }
   startproject "SampleApp"

   outputdir = "%{cfg.buildcfg}-%{cfg.system}-%{cfg.architecture}"

   binarydir = "../../Binaries/" .. outputdir
   prjectdir = "../../Intermediate/ProjectFiles/" .. outputdir
   objectdir = "../../Intermediate/Objects/" .. outputdir

   group "Core"
      include "Source/SampleApp/config.lua"
      include "Source/SampleLibrary/config.lua"
   group ""

   filter "system:windows"
      systemversion "latest"
      defines { }

   filter "configurations:Debug"
      defines { }
      runtime "Debug"
      symbols "On"

   filter "configurations:Release"
      defines { }
      runtime "Release"
      optimize "On"
      symbols "On"

   filter "configurations:Dist"
      defines { }
      runtime "Release"
      optimize "On"
      symbols "Off"

