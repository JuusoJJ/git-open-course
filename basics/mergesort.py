commit dd8c56cede9b109c1df7bda13abc1b1b7b79ed0b
Author: Aku Niskanen <aku.niskanen@tuni.fi>
Date:   Mon Oct 21 02:12:41 2019 -0700

    Merge-sort

diff --git a/basics/mergesort.py b/basics/mergesort.py
index 468ba8b..119844c 100644
--- a/basics/mergesort.py
+++ b/basics/mergesort.py
@@ -8,6 +8,40 @@ def debug_print(debug_msg=None, **kwargs):
         print("{}: {}".format(key, value))
 
 
+def mergesort(array):
+    debug_print(array=array)
+    if len(array) <= 1:
+        return array
+
+    m = len(array) // 2
+    debug_print(m=m)
+
+    left = mergesort(array[:m])
+    right = mergesort(array[m:])
+
+    return merge(left, right)
+
+
+def merge(left, right):
+    debug_print(debug_msg="Merging...", left=left, right=right)
+
+    merged = []
+
+    while len(left) > 0 and len(right) > 0:
+        if left[0] <= right[0]:
+            merged.append(left.pop(0))
+        else:
+            merged.append(right.pop(0))
+
+    if len(left) > 0:
+        merged += left
+    else:
+        merged += right
+
+    debug_print(merged=merged)
+    return merged
+
+
 if __name__ == "__main__":
     input_str = input("Enter numbers, separated by ',': ")
 
@@ -23,3 +57,6 @@ if __name__ == "__main__":
             quit(1)
 
     debug_print(value_list=value_list)
+
+    sorted_list = mergesort(value_list)
+    print(sorted_list)
