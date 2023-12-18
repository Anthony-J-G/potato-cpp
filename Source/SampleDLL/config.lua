project "SampleDLL"
   kind "SharedLib"
   language "C++"
   cppdialect "C++20"
   staticruntime "off"

   location  (prjectdir .. "/%{prj.name}-" .. _ACTION)
   targetdir (binarydir .. "/%{prj.name}")
   objdir    (objectdir .. "/%{prj.name}")

   files { "src/**.h", "src/**.hpp", "src/**.cpp", "src/**.cc", "src/**.c" }

   filter "system:windows"
      defines { }

   filter "configurations:Debug"
      defines { }

   filter "configurations:Release"
      defines { }

   filter "configurations:Dist"
      defines { }