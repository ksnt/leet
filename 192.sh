# Read from the file words.txt and output the word frequency list to stdout.
filename="words.txt"
egrep -o "\b[[:alpha:]]+\b" $filename | awk '{ count[$0]++ }
END{
  for(ind in count)
  {  printf("%s %d\n",ind,count[ind]);  }
}' | sort -k 2 -n -r