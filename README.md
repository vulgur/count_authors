# count_authors
Count authors of source files in an iOS project (maybe also works in Mac app project).

This script will scan all the source files (`.m`, `.h`, `.mm`, `.swift`) and count the authors in the header comments.

## Usage
Copy the script in the root of the project and run `python count_authors.py`.

The count result is like:

```
 535  cow
 172  rabbit
 114  whale
  62  tiger
  27  horse
  24  bull
   8  bear
   6  puma
   4  eagle
   3  lion
   2  cat
   2  dog
   2  mouse
   2  dragon
   2  snake
   1  pig
   1  monkey
   1  rabbit
 968: TOTAL
 ```
