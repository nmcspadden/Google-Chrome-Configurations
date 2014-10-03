#!/usr/bin/python
from LaunchServices import LSSetDefaultHandlerForURLScheme
from LaunchServices import LSSetDefaultRoleHandlerForContentType
 
# 0x00000002 = kLSRolesViewer
# see https://developer.apple.com/library/mac/#documentation/Carbon/Reference/LaunchServicesReference/Reference/reference.html#//apple_ref/c/tdef/LSRolesMask
LSSetDefaultRoleHandlerForContentType("public.html", 0x00000002, "com.google.chrome")
LSSetDefaultRoleHandlerForContentType("public.xhtml", 0x00000002, "com.google.chrome")
LSSetDefaultHandlerForURLScheme("http", "com.google.chrome")
LSSetDefaultHandlerForURLScheme("https", "com.google.chrome")