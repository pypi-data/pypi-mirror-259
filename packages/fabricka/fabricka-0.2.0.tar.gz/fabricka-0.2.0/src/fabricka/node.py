from abc import ABC, abstractmethod
import html
from contextvars import ContextVar
from typing import Any, cast
from uuid import uuid4
from copy import deepcopy
from dataclasses import dataclass, field, fields
from enum import Enum
from fabricka.attr_values import *
import urllib.parse
import html

def bool_field() -> Any:
  return field(default=None, metadata={"type": AttrType.BOOL})

def html_field() -> Any:
  return field(default=None, metadata={"type": AttrType.HTML})

def js_field() -> Any:
  return field(default=None, metadata={"type": AttrType.JS})

def pseudo_bool_field() -> Any:
  return field(default=None, metadata={"type": AttrType.PSEUDO_BOOL})

def style_field() -> Any:
  return field(default=None, metadata={"type": AttrType.STYLE})

def text_field() -> Any:
  return field(default=None, metadata={"type": AttrType.TEXT})

def url_field() -> Any:
  return field(default=None, metadata={"type": AttrType.URL})

def data_field() -> Any:
  return field(default=None, metadata={"type": AttrType.TEXT})

def aria_field() -> Any:
  return field(default=None, metadata={"type": AttrType.TEXT})

def user_field() -> Any:
  return field(default=None, metadata={"type": AttrType.TEXT})

class AttrType(Enum):
  BOOL = 0
  PSEUDO_BOOL = 1
  TEXT = 2
  HTML = 3
  URL = 4
  JS = 5
  STYLE = 6

CONFLICTING_ATTRS: tuple[str, ...] = ("as", "async", "class", "for", "is")
PREFIXED_ATTRS: tuple[str, ...] = ("aria", "data", "user")

_with_stack_var: ContextVar[str | None] = ContextVar('_with_stack', default=None)

class Node(ABC):
  tag_name: str = "node"
  _with_stack: dict[str | None, list[list["Node"]]] = {}

  def __init__(self, *nodes, **kwargs) -> None:
    self.parent: "Node | None" = None
    self.inline: bool = False
    # self.attrs_: dict = {}
    self._nodes: list[Node] = []

    for node in nodes:
      self.insert(node)

    if _with_stack_var.get() is None:
      _with_stack_var.set(uuid4().hex)  
      self._with_stack[_with_stack_var.get()] = []

    if Node._with_stack.get(_with_stack_var.get(), None):
      self.collect()  

  def __str__(self) -> str:
    return self.render()
  
  def render(self, level: int = 0, spaces: int | None = 2, escape: bool = False) -> str:
    markup = ""
    
    inline = self.inline or spaces is None or not self._nodes
    new_line = "" if inline else "\n"

    markup += self.start_tag(level, spaces)
    markup += new_line
    markup += self.inner_html(level+1, spaces, escape)
    markup += self.end_tag(level, spaces)

    return markup
  
  def render_inline(self, level: int = 0) -> str: 
    return self.render(level=level, spaces=None)
  
  def start_tag(self, level: int = 0, spaces: int | None = 2) -> str:
    indent = "" if spaces is None else " " * level * spaces
    
    attrs = self.render_attrs()
    html = f"{indent}<{self.tag_name}{' ' + attrs if attrs != '' else ''}>"

    return html 
  
  def end_tag(self, level: int = 0, spaces: int | None = 2) -> str:
    inline = self.inline or spaces is None or not self._nodes

    indent = "" if inline else " " * level * (0 if spaces is None else spaces)
    new_line = "" if inline else "\n"
    end_indent = "" if inline is None else indent

    return f"{new_line}{end_indent}</{self.tag_name}>"
  
  def inner_html(self, level: int = 0, spaces: int | None = 2, escape: bool = False) -> str:
    markup = ""
    inline = self.inline or spaces is None or not self._nodes
    new_line = "" if inline else "\n"

    markup += new_line.join(node.render(level, None if inline else spaces) for node in self._nodes)  

    return html.escape(markup) if escape else markup
  
  def insert(self, child: "str | int | float | Node | None", index: int | None = None) -> "Node": 
    if type(child) == Root:
      i = -1
      while child._nodes:
        node: Node | None = child.take_first()
        i += 1  
        if index is None:
          self.insert(node)
        else:  
          self.insert(node, index+i)

      return child  
    
    if child is None:
      child_ = Text("") 
    elif type(child) in (str, int, float, bool):
      child_ = Text(str(child)) 
    else:
      child_: Node = child # type: ignore

    if child_.parent is not None:
      raise Exception(f"Node {type(self)} already having a parent. Detach the node before inserting it again.")  

    child_.parent = self 
    if index is None:
      self._nodes.append(child_)
    else:  
      self._nodes.insert(index, child_)
    return child_ 
  
  def insert_in(self, parent: "Node", index: int | None = None) -> "Node":
    parent.insert(self, index)

    return parent
  
  def prepend_to(self, container: "Node") -> "Node":
    return self.insert_in(container, 0)  
  
  def prepend(self, node: "Node | str | int | float") -> "Node":
    return self.insert(node, 0)   

  def append_to(self, container: "Node") -> "Node":
    self.insert_in(container)
    return container 
  
  def append(self, node: "Node | str | int | float") -> "Node":
    return self.insert(node)
  
  def at(self, index: int) -> "Node | None":
    if self._nodes:
      return self._nodes[index]
    
    return None
  
  def first(self) -> "Node | None":
    return self.at(0) 
  
  def last(self) -> "Node | None":
    return self.at(-1) 
  
  def take_at(self, index: int) -> "Node | None":
    if self._nodes:
      node = self._nodes.pop(index)
      node.parent = None
      return node
    
    return None
  
  def take_first(self) -> "Node | None":
    return self.take_at(0)
  
  def take_last(self) -> "Node | None":
    return self.take_at(-1)
  
  def collect(self) -> "Node":
    if self.parent is not None:
      raise Exception(f"Node already having a parent. Detach the node before collecting it.")

    Node._with_stack[_with_stack_var.get()][-1].append(self)
    return self
  
  def free(self) -> "Node | None":
    old_parent = self.parent
    if self.parent is not None:
      self.parent._nodes.remove(self)
      self.parent = None  

    return old_parent 
  
  def __enter__(self) -> "Node":   
    Node._with_stack[_with_stack_var.get()].append([])
    return self

  def __exit__(self, type_, value, traceback):
    if type_:
      self._with_stack[_with_stack_var.get()].pop()
    else:  
      for node in self._with_stack[_with_stack_var.get()].pop():
        if node.parent is None:
          self.insert(node)

  def __iter__(self):
    return iter(self._nodes)  

  def __rshift__(self, parent: "Node") -> "Node":
    parent.insert(self)
    return parent

  def __rrshift__(self, text: str | int | float | None) -> "Node":
    self.insert(text)
    return self  

  def __lshift__(self, child: "str | int | float | Node | None") -> "Node":
    child_ = self.insert(child)
    return self if type(child) == Root else child_ 

  def __radd__(self, text: str | int | float) -> "Root":
    root = Root()
    root.insert(text)
    root.insert(self)
    return root

  def __add__(self, node: "Node | str | int | float") -> "Root":
    root = Root()
    root.insert(self)
    root.insert(node)

    return root   

  def __mul__(self, count: int) -> "Root":
    root = Root()
    for _ in range(count):
      root.insert(deepcopy(self))

    return root
  
  def __rmul__(self, count: int) -> "Container":    
    return self.__mul__(count) 

  def __call__(self, *nodes: "Node | str | int | float") -> "Node":
    for node in nodes:
      self.insert(node)

    return self  

  def attrs(self) -> dict[str, str]:
    attrs = {}
    for field in fields(self): # type: ignore
      if not field.init:
        continue

      value = getattr(self, field.name)
      if value is not None:
        if type(value) == bool and not value:
          continue

        attrs[self.attr_name(field.name)] = getattr(self, field.name)

    return attrs
  
  def render_attr(self, name: str, value: str | bool | None) -> str:
    if type(value) == bool:
      if value:
        return name

    if value is None:
      return ""

    if self.attr_type(name) == AttrType.URL:
      return f'{name}="{urllib.parse.quote(value)}"' #type: ignore
    else:  
      return f'{name}="{html.escape(str(value), quote=True)}"'

  def render_attrs(self) -> str:
    attrs: list[str] = []
    output = ""
    for key, value in self.attrs().items():
      if type(value) == dict:
        if key in PREFIXED_ATTRS:
          l = []
          for k, v in value.items(): #type: ignore
            l.append(self.render_attr(f'{key}-{k}', v))
            output = " ".join(l)
        else:
          raise TypeError(f"Dict. values not allowed for attribute '{key}'.")
      else:
        output = self.render_attr(key, value)

      attrs.append(output)

    return " ".join(attrs)
  
  @classmethod
  def attr_name(cls, field_name: str) -> str:
    return field_name.removesuffix("_").replace("_", "-")
  
  @classmethod
  def field_name(cls, attr_name: str) -> str:
    if attr_name in CONFLICTING_ATTRS:
      return attr_name + "_"
    
    return attr_name.replace("-", "_")
  
  def attr_type(self, attr_name: str) -> AttrType:
    prefix = attr_name.split("-", 1)[0]
    attr_name = prefix if prefix in PREFIXED_ATTRS else attr_name

    return self.__dataclass_fields__[self.field_name(attr_name)].metadata["type"] #type: ignore

class Text(Node):
  def __init__(self, text: str = "", escape=True) -> None:
    super().__init__()
    self.text = text
    self.escape = escape

  @property
  def text(self) -> str:
    return self._text

  @text.setter
  def text(self, text: str) -> None:
    self._text = "" if text is None else str(text)

  def render(self, level: int = 0, spaces: int | None = 2) -> str:
    indent = "" if spaces is None else " " * level * spaces
    text = f"{indent}{html.escape(self.text) if self.escape else self.text}"

    return text  
  
  def insert(self, child: "str | int | float | Node", index: int | None = None) -> "Node": 
    raise TypeError(f"Node insertion not allowed in a Text node.")
  
  def __rshift__(self, parent: "Node") -> "Node":
    if type(parent) == Text:
      parent.text += self.text
      self.text = ""
    else:  
      parent.insert(self)

    return parent
  
  def __rrshift__(self, text: str | int | float) -> "Text":
    self.text += str(text)
    return self  
  
  def __lshift__(self, child: str | int | float | Node) -> "Node":
    if type(child) == Text: 
      self.text += child.text
      child.text = ""
    elif type(child) in (str, int, float, bool):
      self.text += str(child)
    else:  
      self.insert(child)

    return self

@dataclass(kw_only=True, repr=False, eq=False)
class Element(Node): 
  tag_name: str = field(default="element", init=False)

  accesskey: str | None = text_field()
  autocapitalize: str | None = text_field()
  autofocus: bool | None = bool_field()
  class_: str | None = text_field()
  contenteditable: str | None = text_field()
  contextmenu: str | None = text_field()
  dir: DirL | None = text_field()
  draggable: DraggableL | None = text_field()
  enterkeyhint: str | None = text_field()
  exportparts: str | None = text_field()
  hidden: str | bool | None = pseudo_bool_field()
  id: str | None = text_field()
  inert: bool | None = bool_field()
  inputmode: InputmodeL | None = text_field()
  is_: str | None = text_field()
  itemid: str | None = text_field()
  itemprop: str | None = text_field()
  itemref: str | None = text_field()
  itemscope: bool | None = bool_field()
  itemtype: str = url_field()
  lang: str | None = text_field()
  nonce: str | None = text_field()
  part: str | None = text_field()
  popover: str | None = text_field()
  role: RoleL | None = text_field()
  slot: str | None = text_field()
  spellcheck: SpellcheckL | None = text_field()
  style: str | None = style_field()
  tabindex: str | None = text_field()
  title: str | None = text_field()
  translate: TranslateL | None = text_field()
  virtualkeyboardpolicy: str | None = text_field()

  aria: str | dict[str, str] | None = aria_field()
  data: str | dict[str, str] | None = data_field()
  user: str | dict[str, str] | None = user_field()
  
  def __post_init__(self) -> None:
    super().__init__()

@dataclass(kw_only=True, repr=False, eq=False)
class Void(Element):
  tag_name: str = field(default="void", init=False)

  def end_tag(self, level: int = 0, spaces: int | None = 2) -> str:
    return ""  
  
  def insert(self, child: "Node", index: int | None = None) -> "Node": 
    raise TypeError(f"Node insertion not allowed in a void element.")

@dataclass(kw_only=True, repr=False, eq=False)  
class Container(Element):
  tag_name: str = field(default="container", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Root(Container):
  tag_name: str = field(default="root", init=False)

  def start_tag(self, level: int = 0, spaces: int | None = 2) -> str:
    return "" 
  
  def end_tag(self, level: int = 0, spaces: int | None = 2) -> str:
    return ""
  
  def render(self, level: int = 0, spaces: int | None = 2, escape: bool = False) -> str:
    return self.inner_html(level, spaces, escape)
  