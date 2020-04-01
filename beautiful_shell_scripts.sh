find . -type f  -exec basename {} \;
/*
https://qr.ae/pNvZwW
{} is the placeholder to pass a single file name to -exec called command, and \; is to finish -exec.
The whole command is generally equivalent to
for f in `find .`; do basename ${f}; done
*/