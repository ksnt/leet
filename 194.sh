# Read from the file file.txt and print its transposed content to stdout.
# Reference: https://stackoverflow.com/questions/1729824/an-efficient-way-to-transpose-a-file-in-bash
awk '
{ 
    for (i=1; i<=NF; i++)  {
        a[NR,i] = $i
    }
}
NF>p { p = NF }
END {    
    for(j=1; j<=p; j++) {
        str=a[1,j]
        for(i=2; i<=NR; i++){
            str=str" "a[i,j];
        }
        print str
    }
}' file.txt