from typing import List


ORDERED_LIST = "ol"
UNORDERED_LIST = "ul"

def wrap_in_tags(tag_name: str, text: str) -> str:
  return f"{opening_tag(tag_name)}{text}{closing_tag(tag_name)}"

def opening_tag(tag_name: str) -> str:
  return f"<{tag_name}>"

def closing_tag(tag_name: str) -> str:
  return f"</{tag_name}>"

def unordered_list(title: str, input_list: List[str]) -> str:
  return html_list(title, input_list, UNORDERED_LIST)

def ordered_list(title: str, input_list: List[str]) -> str:
  return html_list(title, input_list, ORDERED_LIST)

def html_list(title: str, input_list: List[str], list_type: str) -> str: 
  list_opening = opening_tag(list_type)
  list_closing = closing_tag(list_type)
  li_opening = "<li>"
  li_closing = "</li>"
  result = "<h2>" + title + "</h2>" + list_opening + "\n"
  result += "\n".join([li_opening + str(s) + li_closing for s in input_list])
  result += list_closing
  return result



