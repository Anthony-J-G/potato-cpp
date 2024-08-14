project "SampleApp"
   kind "ConsoleApp"
   language "C++"
   cppdialect "C++20"
   staticruntime "off"

   location  (prjectdir .. "/%{prj.name}-" .. _ACTION)
   objdir    (objectdir .. "/%{prj.name}")
   targetdir (binarydir .. "/%{prj.name}")

   includedirs {
      "../SampleLibrary/include",
      "../SampleDLL/include"
   }

   dependson {
      "SampleDLL"
   }

   links {
      "SampleLibrary"

   }

   files { "src/**.h", "src/**.hpp", "src/**.cpp", "src/**.cc", "src/**.c" }

   filter "system:windows"
      defines { }

   filter "configurations:Debug"
      defines { }

   filter "configurations:Release"
      defines { }

   filter "configurations:Dist"
      kind "WindowedApp"
      defines { }