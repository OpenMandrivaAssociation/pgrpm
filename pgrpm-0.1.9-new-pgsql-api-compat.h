--- pgrpm-0.1.9/pgheader.c~	2010-12-06 22:54:34.692728320 +0100
+++ pgrpm-0.1.9/pgheader.c	2010-12-06 22:54:38.416968508 +0100
@@ -2,6 +2,9 @@
 #include <postgres.h>
 #include <fmgr.h>
 #include <utils/builtins.h>
+#if PG_VERSION_NUM >= 80500
+#include <utils/bytea.h>
+#endif
 #include <funcapi.h>
 
 #include "pgrpm.h"
