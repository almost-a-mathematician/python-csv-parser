import re
from typing import Dict, List

elems: List[List[str]] = []
with open("example.csv","r") as file:
  for line in file:
    elems.append(line.split(','))


def parse_URI(uri: str) -> str | None:
  pattern = r"http(s?):\/\/www.(([a-z]|[A-Z]|[0-9])*([.\-_]?([a-z]|[A-Z]|[0-9])*)*)"
  result = re.match(
      pattern,
      uri,
      )
  if result is not None:
    return result.groups()[1]
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
