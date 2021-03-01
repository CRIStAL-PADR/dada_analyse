content={
    "file1.cpp" : ["file1.h", "file3.h", "file1.cpp", "file5.h"],
    "file2.cpp" : ["file3.h", "file2.cpp"],
    "file3.cpp" : ["file3.h", "file3.cpp", "file2.cpp", "file5.h", "monFichierAvecUnGrandNom.h"],
    "file1.h"   :    ["file1.cpp", "file3.h", "file4.h", "file1.h"],
    "file2.h"   :    ["file2.h", "file4.h", "file5.h"],
    "file3.h"   :    ["file3.h","monFichierAvecUnGrandNom.h"],
    "file4.h"   :    ["file4.h","file1.cpp", "file2.cpp"],
    "monFichierAvecUnGrandNom.h"   :    ["file4.h", "file5.h","file1.h"],
    "/home/damien/development/grand/fichier/monFichierAvecUnGrandNom.h"   :    ["file4.h", "file5.h","file1.h","file1.cpp"],
    "file5.h"   :    ["file4.h", "file5.h","file1.h"],
    "file6.h"   :    ["file4.h", "file5.h","file1.h",  "file1.cpp","file8.cpp" ],
    "file7.h"   :    [],
    "file8.cpp"   :    ["file4.h", "file5.h","file1.h"]
   }