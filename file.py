content={
    "file1.cpp" : ["file2.h", "file3.h", "file4.h"],
    "file2.cpp" : ["file3.h", "file4.h"],
    "file3.cpp" : ["file3.h", "file4.h"],
    "file2.h"   : ["file3.h"],
    "file3.h"   : ["file5.h"],
    "file4.h"   : [],
    "file5.h"   : ["file4.h", "file3.h","file2.h"]
}
