from fabricka import Container, Void, AttrType
from fabricka import bool_field, html_field, js_field, style_field, text_field, url_field
from fabricka.attr_values import *
from dataclasses import dataclass, field
from typing import Literal, Any

#region A
@dataclass(kw_only=True, repr=False, eq=False)
class A(Container):
  """
  Together with its `href` attribute, creates a hyperlink to web pages, files, email addresses, locations within the current page, or anything else a URL can address.
  """
  tag_name: str = field(default="a", init=False)
  inline: bool = field(default=True, init=False)

  download: str | None = text_field()
  href: str | None = url_field()
  hreflang: str | None = text_field()
  ping: str | None = url_field()
  referrerpolicy: AReferrerpolicyL | None = text_field()
  rel: ARelL | None = text_field()
  target: ATargetL | None = text_field()
  type: str | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Abbr(Container):
  """
  Represents an abbreviation or acronym.
  """
  tag_name: str = field(default="abbr", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Address(Container):
  """
  Indicates that the enclosed HTML provides contact information for a person or people, or for an organization.
  """
  tag_name: str = field(default="address", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Area(Void):
  """
  Defines an area inside an image map that has predefined clickable areas. An image map allows geometric areas on an image to be associated with hyperlink.
  """
  tag_name: str = field(default="area", init=False)

  alt: str | None = text_field()
  coords: str | None = text_field()
  download: str | None = text_field()
  href: str | None = url_field()
  ping: str | None = url_field()
  referrerpolicy: AreaReferrerpolicyL | None = text_field()
  rel: AreaRelL | None = text_field()
  shape: AreaShapeL | None = text_field()
  target: AreaTargetL | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Article(Container):
  """
  Represents a self-contained composition in a document, page, application, or site, which is intended to be independently distributable or reusable (e.g., in syndication). Examples include a forum post, a magazine or newspaper article, a blog entry, a product card, a user-submitted comment, an interactive widget or gadget, or any other independent item of content.
  """
  tag_name: str = field(default="article", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Aside(Container):
  """
  Represents a portion of a document whose content is only indirectly related to the document's main content. Asides are frequently presented as sidebars or call-out boxes.
  """
  tag_name: str = field(default="aside", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Audio(Container):
  """
  Used to embed sound content in documents. It may contain one or more audio sources, represented using the `src` attribute or the source element: the browser will choose the most suitable one. It can also be the destination for streamed media, using a MediaStream.
  """
  tag_name: str = field(default="audio", init=False)

  autoplay: bool | None = bool_field()
  controls: bool | None = bool_field()
  controlslist: str | None = text_field()
  crossorigin: AudioCrossoriginL | None = text_field()
  disableremoteplayback: bool | None = bool_field()
  loop: bool | None = bool_field()
  muted: bool | None = bool_field()
  preload: AudioPreloadL | None = text_field()
  src: str | None = url_field()

#endregion
#region B
@dataclass(kw_only=True, repr=False, eq=False)
class B(Container):
  """
  Used to draw the reader's attention to the element's contents, which are not otherwise granted special importance. This was formerly known as the Boldface element, and most browsers still draw the text in boldface. However, you should not use `b` for styling text or granting importance. If you wish to create boldface text, you should use the CSS 'font-weight' property. If you wish to indicate an element is of special importance, you should use the strong element.
  """
  tag_name: str = field(default="b", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Base(Void):
  """
  Specifies the base URL to use for all relative URLs in a document. There can be only one such element in a document.
  """
  tag_name: str = field(default="base", init=False)
  inline: bool = field(default=True, init=False)

  href: str | None = url_field()
  target: BaseTargetL | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Bdi(Container):
  """
  Tells the browser's bidirectional algorithm to treat the text it contains in isolation from its surrounding text. It's particularly useful when a website dynamically inserts some text and doesn't know the directionality of the text being inserted.
  """
  tag_name: str = field(default="bdi", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Bdo(Container):
  """
  Overrides the current directionality of text, so that the text within is rendered in a different direction.
  """
  tag_name: str = field(default="bdo", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Blockquote(Container):
  """
  Indicates that the enclosed text is an extended quotation. Usually, this is rendered visually by indentation. A URL for the source of the quotation may be given using the `cite` attribute, while a text representation of the source can be given using the `cite` element.
  """
  tag_name: str = field(default="blockquote", init=False)

  cite: str | None = url_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Body(Container):
  """
  represents the content of an HTML document. There can be only one such element in a document.
  """
  tag_name: str = field(default="body", init=False)

  onafterprint: str | None = js_field()
  onbeforeprint: str | None = js_field()
  onbeforeunload: str | None = js_field()
  onblur: str | None = js_field()
  onerror: str | None = js_field()
  onfocus: str | None = js_field()
  onhashchange: str | None = js_field()
  onlanguagechange: str | None = js_field()
  onload: str | None = js_field()
  onmessage: str | None = js_field()
  onoffline: str | None = js_field()
  ononline: str | None = js_field()
  onpopstate: str | None = js_field()
  onredo: str | None = js_field()
  onresize: str | None = js_field()
  onstorage: str | None = js_field()
  onundo: str | None = js_field()
  onunload: str | None = js_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Br(Void):
  """
  Produces a line break in text (carriage-return). It is useful for writing a poem or an address, where the division of lines is significant.
  """
  tag_name: str = field(default="br", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Button(Container):
  """
  An interactive element activated by a user with a mouse, keyboard, finger, voice command, or other assistive technology. Once activated, it performs an action, such as submitting a form or opening a dialog.
  """
  tag_name: str = field(default="button", init=False)
  inline: bool = field(default=True, init=False)

  autofocus: bool | None = bool_field()
  disabled: bool | None = bool_field()
  form: str | None = text_field()
  formaction: str | None = url_field()
  formenctype: ButtonFormenctypeL | None = text_field()
  formmethod: ButtonFormmethodL | None = text_field()
  formnovalidate: bool | None = bool_field()
  formtarget: ButtonFormtargetL | None = text_field()
  name: str | None = text_field()
  popovertarget: str | None = text_field()
  popovertargetaction: str | None = text_field()
  type: ButtonTypeL | None = text_field()
  value: str | None = text_field()

#endregion
#region C
@dataclass(kw_only=True, repr=False, eq=False)
class Canvas(Container):
  """
  Container element to use with either the canvas scripting API or the WebGL API to draw graphics and animations.
  """
  tag_name: str = field(default="canvas", init=False)

  height: str | None = text_field()
  width: str | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Caption(Container):
  """
  Specifies the caption (or title) of a table.
  """
  tag_name: str = field(default="caption", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Cite(Container):
  """
  Used to mark up the title of a cited creative work. The reference may be in an abbreviated form according to context-appropriate conventions related to citation metadata.
  """
  tag_name: str = field(default="cite", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Code(Container):
  """
  Displays its contents styled in a fashion intended to indicate that the text is a short fragment of computer code. By default, the content text is displayed using the user agent's default monospace font.
  """
  tag_name: str = field(default="code", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Col(Void):
  """
  Defines one or more columns in a column group represented by its implicit or explicit parent `colgroup` element. The `col` element is only valid as a child of a `colgroup` element that has no `span` attribute defined.
  """
  tag_name: str = field(default="col", init=False)
  inline: bool = field(default=True, init=False)

  span: str | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Colgroup(Container):
  """
  Defines a group of columns within a table.
  """
  tag_name: str = field(default="colgroup", init=False)

  span: str | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Comment(Void):
  tag_name: str = field(default="", init=False)
  text: str = field(default="", init=False)
  # def __init__(self, text: str) -> None:
  #   super().__init__()
  #   self.name = ""
  #   self.text = text

  # def __post_init__(self, text: str) -> None:
  #   super().__init__() 
  #   self.text = text 

  def __call__(self, text: str) -> "Comment":
    self.text = text  

    return self

  def render(self, level: int = 0, spaces: int | None = 2) -> str:
    # indent = " " * spaces * level
    indent = "" if spaces is None else " " * spaces * level
    markup = f'{indent}<!--{self.text}-->'

    return markup    

#endregion
#region D
@dataclass(kw_only=True, repr=False, eq=False)
class Data(Container):
  """
  Links a given piece of content with a machine-readable translation. If the content is time- or date-related, the`time` element must be used.
  """
  tag_name: str = field(default="data", init=False)

  value: str | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Datalist(Container):
  """
  Contains a set of `option` elements that represent the permissible or recommended options available to choose from within other controls.
  """
  tag_name: str = field(default="datalist", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Dd(Container):
  """
  Provides the description, definition, or value for the preceding term (`dt`) in a description list (`dl`).
  """
  tag_name: str = field(default="dd", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Del(Container):
  """
  Represents a range of text that has been deleted from a document. This can be used when rendering 'track changes' or source code diff information, for example. The `ins` element can be used for the opposite purpose: to indicate text that has been added to the document.
  """
  tag_name: str = field(default="del", init=False)
  inline: bool = field(default=True, init=False)

  cite: str | None = url_field()
  datetime: str | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Details(Container):
  """
  Creates a disclosure widget in which information is visible only when the widget is toggled into an 'open' state. A summary or label must be provided using the `summary` element.
  """
  tag_name: str = field(default="details", init=False)

  open: bool | None = bool_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Dfn(Container):
  """
  Used to indicate the term being defined within the context of a definition phrase or sentence. The ancestor `p` element, the `dt`/`dd` pairing, or the nearest section ancestor of the `dfn` element, is considered to be the definition of the term.
  """
  tag_name: str = field(default="dfn", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Dialog(Container):
  """
  Represents a dialog box or other interactive component, such as a dismissible alert, inspector, or subwindow.
  """
  tag_name: str = field(default="dialog", init=False)

  open: bool | None = bool_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Div(Container):
  """
  The generic container for flow content. It has no effect on the content or layout until styled in some way using CSS (e.g., styling is directly applied to it, or some kind of layout model like flexbox is applied to its parent element).
  """
  tag_name: str = field(default="div", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Dl(Container):
  """
  Represents a description list. The element encloses a list of groups of terms (specified using the `dt` element) and descriptions (provided by `dd` elements). Common uses for this element are to implement a glossary or to display metadata (a list of key-value pairs).
  """
  tag_name: str = field(default="dl", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Dt(Container):
  """
  Specifies a term in a description or definition list, and as such must be used inside a `dl` element. It is usually followed by a `dd` element; however, multiple `dt` elements in a row indicate several terms that are all defined by the immediate next `dd` element.
  """
  tag_name: str = field(default="dt", init=False)

#endregion
#region E
@dataclass(kw_only=True, repr=False, eq=False)
class Em(Container):
  """
  Marks text that has stress emphasis. The `em` element can be nested, with each nesting level indicating a greater degree of emphasis.
  """
  tag_name: str = field(default="em", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Embed(Void):
  """
  Embeds external content at the specified point in the document. This content is provided by an external application or other source of interactive content such as a browser plug-in.
  """
  tag_name: str = field(default="embed", init=False)

  height: str | None = text_field()
  src: str | None = url_field()
  type: str | None = text_field()
  width: str | None = text_field()

#endregion
#region F
@dataclass(kw_only=True, repr=False, eq=False)
class Fieldset(Container):
  """
  Used to group several controls as well as labels (`label`) within a web form.
  """
  tag_name: str = field(default="fieldset", init=False)

  disabled: bool | None = bool_field()
  form: str | None = text_field()
  name: str | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Figcaption(Container):
  """
  Represents a caption or legend describing the rest of the contents of its parent `figure` element.
  """
  tag_name: str = field(default="figcaption", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Figure(Container):
  """
  Represents self-contained content, potentially with an optional caption, which is specified using the `figcaption` element. The figure, its caption, and its contents are referenced as a single unit.
  """
  tag_name: str = field(default="figure", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Footer(Container):
  """
  Represents a footer for its nearest ancestor sectioning content or sectioning root element. A `footer` typically contains information about the author of the section, copyright data, or links to related documents.
  """
  tag_name: str = field(default="footer", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Form(Container):
  """
  Represents a document section containing interactive controls for submitting information.
  """
  tag_name: str = field(default="form", init=False)

  accept_charset: str | None = text_field()
  action: str | None = url_field()
  autocomplete: FormAutocompleteL | None = text_field()
  enctype: FormEnctypeL | None = text_field()
  method: FormMethodL | None = text_field()
  name: str | None = text_field()
  novalidate: bool | None = bool_field()
  rel: FormRelL | None = text_field()
  target: FormTargetL | None = text_field()

#endregion
#region H
@dataclass(kw_only=True, repr=False, eq=False)
class H1(Container):
  """
  Level 1 of section headings
  """
  tag_name: str = field(default="h1", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class H2(Container):
  """
  Level 2 of section headings
  """
  tag_name: str = field(default="h2", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class H3(Container):
  """
  Level 3 of section headings
  """
  tag_name: str = field(default="h3", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class H4(Container):
  """
  Level 4 of section headings
  """
  tag_name: str = field(default="h4", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class H5(Container):
  """
  Level 5 of section headings
  """
  tag_name: str = field(default="h5", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class H6(Container):
  """
  Level 6 of section headings
  """
  tag_name: str = field(default="h6", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Head(Container):
  """
  Contains machine-readable information (metadata) about the document, like its title, scripts, and style sheets.
  """
  tag_name: str = field(default="head", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Header(Container):
  """
  Represents introductory content, typically a group of introductory or navigational aids. It may contain some heading elements but also a logo, a search form, an author name, and other elements.
  """
  tag_name: str = field(default="header", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Hgroup(Container):
  """
  Represents a heading grouped with any secondary content, such as subheadings, an alternative title, or a tagline.
  """
  tag_name: str = field(default="hgroup", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Hr(Void):
  """
  Represents a thematic break between paragraph-level elements: for example, a change of scene in a story, or a shift of topic within a section.
  """
  tag_name: str = field(default="hr", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Html(Container):
  """
  Represents the root (top-level element) of an HTML document, so it is also referred to as the root element. All other elements must be descendants of this element.
  """
  tag_name: str = field(default="html", init=False)

  xmlns: str | HtmlXmlnsL | None = url_field()

  def render(self, level: int = 0, spaces: int | None = 2, escape: bool = False) -> str:
    return "<!DOCTYPE html>\n" + super().render(level, spaces, escape)  

#endregion
#region I
@dataclass(kw_only=True, repr=False, eq=False)
class I(Container):
  """
  Represents a range of text that is set off from the normal text for some reason, such as idiomatic text, technical terms, and taxonomical designations, among others. Historically, these have been presented using italicized type, which is the original source of the `i` naming of this element.
  """
  tag_name: str = field(default="i", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Iframe(Container):
  """
  Represents a nested browsing context, embedding another HTML page into the current one.
  """
  tag_name: str = field(default="iframe", init=False)

  allow: str | None = text_field()
  allowfullscreen: IframeAllowfullscreenL | None = text_field()
  allowpaymentrequest: str | None = text_field()
  credentialless: str | None = text_field()
  csp: str | None = text_field()
  height: str | None = text_field()
  loading: IframeLoadingL | None = text_field()
  name: str | None = text_field()
  referrerpolicy: IframeReferrerpolicyL | None = text_field()
  sandbox: IframeSandboxL | None = text_field()
  src: str | None = url_field()
  srcdoc: str | None = html_field()
  width: str | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Img(Void):
  """
  Embeds an image into the document.
  """
  tag_name: str = field(default="img", init=False)

  alt: str | None = text_field()
  crossorigin: ImgCrossoriginL | None = text_field()
  decoding: ImgDecodingL | None = text_field()
  elementtiming: str | None = text_field()
  fetchpriority: ImgFetchpriorityL | None = text_field()
  height: str | None = text_field()
  ismap: bool | None = bool_field()
  loading: ImgLoadingL | None = text_field()
  referrerpolicy: ImgReferrerpolicyL | None = text_field()
  sizes: str | None = text_field()
  src: str | None = url_field()
  srcset: str | None = url_field()
  usemap: str | None = url_field()
  width: str | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Input(Void):
  """
  Used to create interactive controls for web-based forms to accept data from the user; a wide variety of types of input data and control widgets are available, depending on the device and user agent. The `input` element is one of the most powerful and complex in all of HTML due to the sheer number of combinations of input types and attributes.
  """
  tag_name: str = field(default="input", init=False)

  accept: InputAcceptL | None = text_field()
  alt: str | None = text_field()
  autocomplete: InputAutocompleteL | None = text_field()
  autofocus: bool | None = bool_field()
  capture: str | None = text_field()
  checked: bool | None = bool_field()
  dirname: str | None = text_field()
  disabled: bool | None = bool_field()
  form: str | None = text_field()
  formaction: str | None = url_field()
  formenctype: InputFormenctypeL | None = text_field()
  formmethod: InputFormmethodL | None = text_field()
  formnovalidate: bool | None = bool_field()
  formtarget: InputFormtargetL | None = text_field()
  height: str | None = text_field()
  list: str | None = text_field()
  max: str | None = text_field()
  maxlength: str | None = text_field()
  min: str | None = text_field()
  minlength: str | None = text_field()
  multiple: bool | None = bool_field()
  name: str | None = text_field()
  pattern: str | None = text_field()
  placeholder: str | None = text_field()
  popovertarget: str | None = text_field()
  popovertargetaction: str | None = text_field()
  readonly: bool | None = bool_field()
  required: bool | None = bool_field()
  size: str | None = text_field()
  src: str | None = url_field()
  step: str | None = text_field()
  type: InputTypeL | None = text_field()
  value: str | None = text_field()
  width: str | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Ins(Container):
  """
  Represents a range of text that has been added to a document. You can use the `del` element to similarly represent a range of text that has been deleted from the document.
  """
  tag_name: str = field(default="ins", init=False)
  inline: bool = field(default=True, init=False)

  cite: str | None = url_field()
  datetime: str | None = text_field()

#endregion
#region K
@dataclass(kw_only=True, repr=False, eq=False)
class Kbd(Container):
  """
  Represents a span of inline text denoting textual user input from a keyboard, voice input, or any other text entry device. By convention, the user agent defaults to rendering the contents of a `kbd` element using its default monospace font, although this is not mandated by the HTML standard.
  """
  tag_name: str = field(default="kbd", init=False)
  inline: bool = field(default=True, init=False)

#endregion
#region L
@dataclass(kw_only=True, repr=False, eq=False)
class Label(Container):
  """
  Represents a caption for an item in a user interface.
  """
  tag_name: str = field(default="label", init=False)
  inline: bool = field(default=True, init=False)

  for_: str | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Legend(Container):
  """
  Represents a caption for the content of its parent `fieldset`.
  """
  tag_name: str = field(default="legend", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Li(Container):
  """
  Represents an item in a list. It must be contained in a parent element: an ordered list (`ol`), an unordered list (`ul`), or a menu (`menu`). In menus and unordered lists, list items are usually displayed using bullet points. In ordered lists, they are usually displayed with an ascending counter on the left, such as a number or letter.
  """
  tag_name: str = field(default="li", init=False)
  inline: bool = field(default=True, init=False)

  value: str | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Link(Void):
  """
  Specifies relationships between the current document and an external resource. This element is most commonly used to link to CSS but is also used to establish site icons (both 'favicon' style icons and icons for the home screen and apps on mobile devices) among other things.
  """
  tag_name: str = field(default="link", init=False)

  as_: str | None = text_field()
  # blocking: str | None = text_field()
  crossorigin: LinkCrossoriginL | None = text_field()
  disabled: bool | None = bool_field()
  fetchpriority: str | None = text_field()
  href: str | None = url_field()
  hreflang: str | None = text_field()
  imagesizes: str | None = text_field()
  imagesrcset: str | None = url_field()
  integrity: str | None = text_field()
  media: str | None = text_field()
  referrerpolicy: LinkReferrerpolicyL | None = text_field()
  rel: LinkRelL | None = text_field()
  sizes: str | None = text_field()
  type: str | None = text_field()

#endregion
#region M
@dataclass(kw_only=True, repr=False, eq=False)
class Main(Container):
  """
  Represents the dominant content of the body of a document. The main content area consists of content that is directly related to or expands upon the central topic of a document, or the central functionality of an application.
  """
  tag_name: str = field(default="main", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Map(Container):
  """
  Used with `area` elements to define an image map (a clickable link area).
  """
  tag_name: str = field(default="map", init=False)

  name: str | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Mark(Container):
  """
  Represents text which is marked or highlighted for reference or notation purposes due to the marked passage's relevance in the enclosing context.
  """
  tag_name: str = field(default="mark", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Menu(Container):
  """
  A semantic alternative to `ul`, but treated by browsers (and exposed through the accessibility tree) as no different than `ul`. It represents an unordered list of items (which are represented by `li` elements).
  """
  tag_name: str = field(default="menu", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Meta(Void):
  """
  Represents metadata that cannot be represented by other HTML meta-related elements, like `base`, `link`, `script`, `style` and `title`.
  """
  tag_name: str = field(default="meta", init=False)

  charset: str | None = text_field()
  content: str | None = text_field()
  http_equiv: MetaHttp_equivL | None = text_field()
  name: MetaNameL | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Meter(Container):
  """
  Represents either a scalar value within a known range or a fractional value.
  """
  tag_name: str = field(default="meter", init=False)

  form: str | None = text_field()
  high: str | None = text_field()
  low: str | None = text_field()
  max: str | None = text_field()
  min: str | None = text_field()
  optimum: str | None = text_field()
  value: str | None = text_field()

#endregion
#region N
@dataclass(kw_only=True, repr=False, eq=False)
class Nav(Container):
  """
  Represents a section of a page whose purpose is to provide navigation links, either within the current document or to other documents. Common examples of navigation sections are menus, tables of contents, and indexes.
  """
  tag_name: str = field(default="nav", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Noscript(Container):
  """
  Defines a section of HTML to be inserted if a script type on the page is unsupported or if scripting is currently turned off in the browser.
  """
  tag_name: str = field(default="noscript", init=False)
  inline: bool = field(default=True, init=False)

#endregion
#region O
@dataclass(kw_only=True, repr=False, eq=False)
class Object(Container):
  """
  Represents an external resource, which can be treated as an image, a nested browsing context, or a resource to be handled by a plugin.
  """
  tag_name: str = field(default="object", init=False)

  data: str | None = url_field()
  form: str | None = text_field()
  height: str | None = text_field()
  name: str | None = text_field()
  type: str | None = text_field()
  usemap: str | None = text_field()
  width: str | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Ol(Container):
  """
  Represents an ordered list of items — typically rendered as a numbered list.
  """
  tag_name: str = field(default="ol", init=False)

  reversed: bool | None = bool_field()
  start: str | None = text_field()
  type: OlTypeL | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Optgroup(Container):
  """
  Creates a grouping of options within a `select` element.
  """
  tag_name: str = field(default="optgroup", init=False)

  disabled: bool | None = bool_field()
  label: str | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Option(Container):
  """
  Used to define an item contained in a select, an `optgroup`, or a `datalist` element. As such, `option` can represent menu items in popups and other lists of items in an HTML document.
  """
  tag_name: str = field(default="option", init=False)
  inline: bool = field(default=True, init=False)

  disabled: bool | None = bool_field()
  label: str | None = text_field()
  selected: bool | None = bool_field()
  value: str | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Output(Container):
  """
  Container element into which a site or app can inject the results of a calculation or the outcome of a user action.
  """
  tag_name: str = field(default="output", init=False)

  for_: str | None = text_field()
  form: str | None = text_field()
  name: str | None = text_field()

#endregion
#region P
@dataclass(kw_only=True, repr=False, eq=False)
class P(Container):
  """
  Represents a paragraph. Paragraphs are usually represented in visual media as blocks of text separated from adjacent blocks by blank lines and/or first-line indentation, but HTML paragraphs can be any structural grouping of related content, such as images or form fields.
  """
  tag_name: str = field(default="p", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Picture(Container):
  """
  Contains zero or more `source` elements and one `img` element to offer alternative versions of an image for different display/device scenarios.
  """
  tag_name: str = field(default="picture", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Pre(Container):
  """
  Represents preformatted text which is to be presented exactly as written in the HTML file. The text is typically rendered using a non-proportional, or monospaced, font. Whitespace inside this element is displayed as written.
  """
  tag_name: str = field(default="pre", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Progress(Container):
  """
  Displays an indicator showing the completion progress of a task, typically displayed as a progress bar.
  """
  tag_name: str = field(default="progress", init=False)

  max: str | None = text_field()
  value: str | None = text_field()

#endregion
#region Q
@dataclass(kw_only=True, repr=False, eq=False)
class Q(Container):
  """
  Indicates that the enclosed text is a short inline quotation. Most modern browsers implement this by surrounding the text in quotation marks. This element is intended for short quotations that don't require paragraph breaks; for long quotations use the `blockquote` element.
  """
  tag_name: str = field(default="q", init=False)
  inline: bool = field(default=True, init=False)

  cite: str | None = url_field()

#endregion
#region R
@dataclass(kw_only=True, repr=False, eq=False)
class Rp(Container):
  """
  Used to provide fall-back parentheses for browsers that do not support the display of ruby annotations using the `ruby` element. One `rp` element should enclose each of the opening and closing parentheses that wrap the `rt` element that contains the annotation's text.
  """
  tag_name: str = field(default="rp", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Rt(Container):
  """
  Specifies the ruby text component of a ruby annotation, which is used to provide pronunciation, translation, or transliteration information for East Asian typography. The `rt` element must always be contained within a `ruby` element.
  """
  tag_name: str = field(default="rt", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Ruby(Container):
  """
  Represents small annotations that are rendered above, below, or next to base text, usually used for showing the pronunciation of East Asian characters. It can also be used for annotating other kinds of text, but this usage is less common.
  """
  tag_name: str = field(default="ruby", init=False)
  inline: bool = field(default=True, init=False)

#endregion
#region S
@dataclass(kw_only=True, repr=False, eq=False)
class S(Container):
  """
  Renders text with a strikethrough, or a line through it. Use the `s` element to represent things that are no longer relevant or no longer accurate. However, `s` is not appropriate when indicating document edits; for that, use the del and ins elements, as appropriate.
  """
  tag_name: str = field(default="s", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Samp(Container):
  """
  Used to enclose inline text which represents sample (or quoted) output from a computer program. Its contents are typically rendered using the browser's default monospaced font (such as Courier or Lucida Console).
  """
  tag_name: str = field(default="samp", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Script(Container):
  """
  Used to embed executable code or data; this is typically used to embed or refer to JavaScript code. The `script` element can also be used with other languages, such as WebGL's GLSL shader programming language and JSON.
  """
  tag_name: str = field(default="script", init=False)

  async_: bool | None = bool_field()
  blocking: str | None = text_field()
  crossorigin: ScriptCrossoriginL | None = text_field()
  defer: bool | None = bool_field()
  fetchpriority: str | None = text_field()
  integrity: str | None = text_field()
  nomodule: bool | None = bool_field()
  nonce: str | None = text_field()
  referrerpolicy: ScriptReferrerpolicyL | None = text_field()
  src: str | None = url_field()
  type: str | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Section(Container):
  """
  Represents a generic standalone section of a document, which doesn't have a more specific semantic element to represent it. Sections should always have a heading, with very few exceptions.
  """
  tag_name: str = field(default="section", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Select(Container):
  """
  Represents a control that provides a menu of options.
  """
  tag_name: str = field(default="select", init=False)

  autocomplete: SelectAutocompleteL | None = text_field()
  autofocus: bool | None = bool_field()
  disabled: bool | None = bool_field()
  form: str | None = text_field()
  multiple: bool | None = bool_field()
  name: str | None = text_field()
  required: bool | None = bool_field()
  size: str | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Slot(Container):
  """
  Part of the Web Components technology suite, this element is a placeholder inside a web component that you can fill with your own markup, which lets you create separate DOM trees and present them together.
  """
  tag_name: str = field(default="slot", init=False)

  name: str | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Small(Container):
  """
  Represents side-comments and small print, like copyright and legal text, independent of its styled presentation. By default, it renders text within it one font size smaller, such as from 'small' to 'x-small'.
  """
  tag_name: str = field(default="small", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Source(Void):
  """
  Specifies multiple media resources for the picture, the audio element, or the video element. It is a void element, meaning that it has no content and does not have a closing tag. It is commonly used to offer the same media content in multiple file formats in order to provide compatibility with a broad range of browsers given their differing support for image file formats and media file formats.
  """
  tag_name: str = field(default="source", init=False)

  height: str | None = text_field()
  media: str | None = text_field()
  sizes: str | None = text_field()
  src: str | None = url_field()
  srcset: str | None = url_field()
  type: str | None = text_field()
  width: str | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Span(Container):
  """
  A generic inline container for phrasing content, which does not inherently represent anything. It can be used to group elements for styling purposes (using the `class` or `id` attributes), or because they share attribute values, such as `lang`. It should be used only when no other semantic element is appropriate. `span` is very much like a div element, but div is a block-level element whereas a `span` is an inline-level element.
  """
  tag_name: str = field(default="span", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Strong(Container):
  """
  Indicates that its contents have strong importance, seriousness, or urgency. Browsers typically render the contents in bold type.
  """
  tag_name: str = field(default="strong", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Style(Container):
  """
  Contains style information for a document or part of a document. It contains CSS, which is applied to the contents of the document containing this element.
  """
  tag_name: str = field(default="style", init=False)

  blocking: str | None = text_field()
  media: str | None = text_field()
  nonce: str | None = text_field()
  title: str | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Sub(Container):
  """
  Specifies inline text which should be displayed as subscript for solely typographical reasons. Subscripts are typically rendered with a lowered baseline using smaller text.
  """
  tag_name: str = field(default="sub", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Summary(Container):
  """
  Specifies a summary, caption, or legend for a details element's disclosure box. Clicking the `summary` element toggles the state of the parent `details` element open and closed.
  """
  tag_name: str = field(default="summary", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Sup(Container):
  """
  Specifies inline text which is to be displayed as superscript for solely typographical reasons. Superscripts are usually rendered with a raised baseline using smaller text.
  """
  tag_name: str = field(default="sup", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Svg(Container):
  """
  Container defining a new coordinate system and viewport. It is used as the outermost element of SVG documents, but it can also be used to embed an SVG fragment inside an SVG or HTML document.
  """
  tag_name: str = field(default="svg", init=False)

#endregion
#region T
@dataclass(kw_only=True, repr=False, eq=False)
class Table(Container):
  """
  Represents tabular data—that is, information presented in a two-dimensional table comprised of rows and columns of cells containing data.
  """
  tag_name: str = field(default="table", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Tbody(Container):
  """
  Encapsulates a set of table rows (`tr` elements), indicating that they comprise the body of a table's (main) data.
  """
  tag_name: str = field(default="tbody", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Td(Container):
  """
  A child of the `tr` element, it defines a cell of a table that contains data.
  """
  tag_name: str = field(default="td", init=False)
  inline: bool = field(default=True, init=False)

  colspan: str | None = text_field()
  headers: str | None = text_field()
  rowspan: str | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Template(Container):
  """
  A mechanism for holding HTML that is not to be rendered immediately when a page is loaded but may be instantiated subsequently during runtime using JavaScript.
  """
  tag_name: str = field(default="template", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Textarea(Container):
  """
  Represents a multi-line plain-text editing control, useful when you want to allow users to enter a sizeable amount of free-form text, for example, a comment on a review or feedback form.
  """
  tag_name: str = field(default="textarea", init=False)

  autocomplete: TextareaAutocompleteL | None = text_field()
  autocorrect: str | None = text_field()
  autofocus: bool | None = bool_field()
  cols: str | None = text_field()
  dirname: str | None = text_field()
  disabled: bool | None = bool_field()
  form: str | None = text_field()
  maxlength: str | None = text_field()
  minlength: str | None = text_field()
  name: str | None = text_field()
  placeholder: str | None = text_field()
  readonly: bool | None = bool_field()
  required: bool | None = bool_field()
  rows: str | None = text_field()
  spellcheck: str | None = text_field()
  wrap: TextareaWrapL | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Tfoot(Container):
  """
  Encapsulates a set of table rows (`tr` elements), indicating that they comprise the foot of a table with information about the table's columns. This is usually a summary of the columns, e.g., a sum of the given numbers in a column.
  """
  tag_name: str = field(default="tfoot", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Th(Container):
  """
  A child of the `tr` element, it defines a cell as the header of a group of table cells. The nature of this group can be explicitly defined by the `scope` and `headers` attributes.
  """
  tag_name: str = field(default="th", init=False)
  inline: bool = field(default=True, init=False)

  abbr: str | None = text_field()
  colspan: str | None = text_field()
  headers: str | None = text_field()
  rowspan: str | None = text_field()
  scope: ThScopeL | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Thead(Container):
  """
  Encapsulates a set of table rows (`tr` elements), indicating that they comprise the head of a table with information about the table's columns. This is usually in the form of column headers (`th` elements).
  """
  tag_name: str = field(default="thead", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Time(Container):
  """
  Represents a specific period in time. It may include the `datetime` attribute to translate dates into machine-readable format, allowing for better search engine results or custom features such as reminders.
  """
  tag_name: str = field(default="time", init=False)
  inline: bool = field(default=True, init=False)

  datetime: str | None = text_field()

@dataclass(kw_only=True, repr=False, eq=False)
class Title(Container):
  """
  Defines the document's title that is shown in a browser's title bar or a page's tab. It only contains text; tags within the element are ignored.
  """
  tag_name: str = field(default="title", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Tr(Container):
  """
  Defines a row of cells in a table. The row's cells can then be established using a mix of `td` (data cell) and `th` (header cell) elements.
  """
  tag_name: str = field(default="tr", init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Track(Void):
  """
  Used as a child of the media elements, audio and video. It lets you specify timed text tracks (or time-based data), for example to automatically handle subtitles. The tracks are formatted in WebVTT format ('.vtt' files)—Web Video Text Tracks.
  """
  tag_name: str = field(default="track", init=False)

  default: bool | None = bool_field()
  kind: TrackKindL | None = text_field()
  label: str | None = text_field()
  src: str | None = url_field()
  srclang: str | None = text_field()

#endregion
#region U
@dataclass(kw_only=True, repr=False, eq=False)
class U(Container):
  """
  Represents a span of inline text which should be rendered in a way that indicates that it has a non-textual annotation. This is rendered by default as a simple solid underline but may be altered using CSS.
  """
  tag_name: str = field(default="u", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Ul(Container):
  """
  Represents an unordered list of items, typically rendered as a bulleted list.
  """
  tag_name: str = field(default="ul", init=False)

#endregion
#region V
@dataclass(kw_only=True, repr=False, eq=False)
class Var(Container):
  """
  Represents the name of a variable in a mathematical expression or a programming context. It's typically presented using an italicized version of the current typeface, although that behavior is browser-dependent.
  """
  tag_name: str = field(default="var", init=False)
  inline: bool = field(default=True, init=False)

@dataclass(kw_only=True, repr=False, eq=False)
class Video(Container):
  """
  Embeds a media player which supports video playback into the document. You can also use `video` for audio content, but the audio element may provide a more appropriate user experience.
  """
  tag_name: str = field(default="video", init=False)

  autoplay: bool | None = bool_field()
  controls: bool | None = bool_field()
  controlslist: str | None = text_field()
  crossorigin: VideoCrossoriginL | None = text_field()
  disablepictureinpicture: bool | None = bool_field()
  disableremoteplayback: bool | None = bool_field()
  height: str | None = text_field()
  loop: bool | None = bool_field()
  muted: bool | None = bool_field()
  playsinline: bool | None = bool_field()
  poster: str | None = url_field()
  preload: VideoPreloadL | None = text_field()
  src: str | None = url_field()
  width: str | None = text_field()

#endregion
#region W
@dataclass(kw_only=True, repr=False, eq=False)
class Wbr(Void):
  """
  Represents a word break opportunity—a position within text where the browser may optionally break a line, though its line-breaking rules would not otherwise create a break at that location.
  """
  tag_name: str = field(default="wbr", init=False)
  inline: bool = field(default=True, init=False)

#endregion
