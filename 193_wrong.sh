# This seems wrong but I am not sure why...
#!/bin/bash
while read line
do
  if [[ "$line" = "^\([0-9]{3}\)\s[0-9]{3}-[0-9]{4}$" ]] || [[ "$line" = "^[0-9]{3}-[0-9]{3}-[0-9]{4}$" ]]; then
      echo $line
  fi
done < file.txt