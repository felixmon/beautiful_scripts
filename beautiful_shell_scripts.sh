# find and show filenames only
find . -type f  -exec basename {} \;
<<COMMENT
https://qr.ae/pNvZwW
{} is the placeholder to pass a single file name to -exec called command, and \; is to finish -exec.
The whole command is generally equivalent to
for f in `find .`; do basename ${f}; done
COMMENT

# split with awk https://stackoverflow.com/a/8009724/13130970
echo "12|23|11" | awk '{split($0,a,"|"); print a[3],a[2],a[1]}'
# or https://stackoverflow.com/a/8009855/13130970
echo "12|23|11|bb|dd|aaa|badfasjlkdjalsg|g" | awk -F\| '{for (i = 0; ++i <= NF;)print i, $i}'
echo "/Users/felix/Documents/LEARN/Science/Computer_Science/Programming/Shell_Programming/Shell_Scripts" | awk -F\/ '{for (i = 0; ++i <= NF;)print i, $i}'