project "SampleLibrary"
   kind "ConsoleApp"
   language "C++"
   cppdialect "C++20"
   staticruntime "off"

    -- location  (prjectdir .. "/%{prj.name}")
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
      kind "WindowedApp"
      defines { }