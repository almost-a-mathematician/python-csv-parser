from typing import Dict, List
from urllib.parse import urlparse 

elems: List[List[str]] = []
with open("example.csv","r") as file:
  for line in file:
    elems.append(line.split(','))

def parse_URI(uri: str) -> str | None:
  parsed_uri = urlparse(uri)
  result = parsed_uri.netloc
  

  if result is not None:
    return result
  else:
    return None


def push_entry(entry:str, to:Dict[str,int]) -> None:
  if entry in to:
        to[entry] += 1
  else:
        to[entry] = 1

  
def results() -> Dict[str,int]:
  url_entr: Dict[str,int] = dict() 

  for line in elems:
    for elem in line:
      result = parse_URI(elem)
      if not result:
        continue
      else:
        push_entry(result, url_entr)

  return url_entr
    

print(results())
