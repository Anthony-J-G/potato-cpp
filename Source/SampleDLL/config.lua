project "SampleDLL"
   kind "SharedLib"
   language "C++"
   cppdialect "C++20"
   staticruntime "off"

   location  (prjectdir .. "/%{prj.name}-" .. _ACTION)
   objdir    (objectdir .. "/%{prj.name}")
   targetdir (binarydir)

   srcdir = path.getabsolute("src")
   headerfiledir = path.getabsolute("include")
   
   postbuildcommands {
      "{RMDIR} " .. headerfiledir,
      "{COPYDIR} " .. srcdir .. "\\*.h " .. headerfiledir
   }

   files { "src/**.h", "src/**.hpp", "src/**.cpp", "src/**.cc", "src/**.c" }

   filter "system:windows"
      defines { }

   filter "configurations:Debug"
      defines { }

   filter "configurations:Release"
      defines { }

   filter "configurations:Dist"
      defines { }