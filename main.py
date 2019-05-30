import codecs
import os
import pickle
import json
s= u"\u0627\u0644\u0639\u062a\u0629"
is_russian = False
with codecs.open('data//ar.csv', "r", "utf8") as f:
  translation_dict = {}
  for line in f.readlines():
    parts = line.split(",")
    en = parts[0]
    if en == "" or en[0].isupper():
      continue
    else:
      if is_russian and parts[3] != "\n" and parts[3] != "\r\n" and parts[3] != "\r":
          other_m = parts[2]
          other_f = parts[3].strip()
          translation_dict[en] = (other_m, other_f)
      else:
        other_m = parts[1].strip()
        other_f = None
        if len(parts) > 2 and parts[2] != "\n" and parts[2] != "\r\n" and parts[2] != "\r" and parts[2] != '':
          other_f = parts[2].strip()
        translation_dict[en] = (other_m, other_f)
  print(translation_dict)
with  open('file.txt', 'w') as file:
  file.write(json.dumps(translation_dict))