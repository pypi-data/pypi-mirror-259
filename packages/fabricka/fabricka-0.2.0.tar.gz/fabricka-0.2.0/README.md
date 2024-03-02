# Fabricka
Build reusable styled HTML components with python.

A library under development.

## Installation

`$ pip install fabricka`

## Features
Below are the main features of Fabricka:

  - Create complex element hierarchies using context managers
  - Append elements with the right and left shift operators
  - Create element siblings with the plus operator
  - Context-aware escaping
  - Support for all current HTML elements
  - Support for all current HTML attributes
  - Code autocompletion for HTML attributes
  - Comprehensive unit tests

## Usage

### Simple example

```python
from fabricka import Ol, Li

with Ol() as ol:
  Li("HTML")
  Li("CSS")
  Li("JS")

print(ol.render())
```

```html
<ol>
  <li>HTML</li>
  <li>CSS</li>
  <li>JS</li>
</ol>
```
