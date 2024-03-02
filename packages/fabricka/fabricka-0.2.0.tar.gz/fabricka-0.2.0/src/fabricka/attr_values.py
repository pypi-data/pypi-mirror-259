from typing import Literal

AutocompleteL = Literal[
  "additional-name",
  "address-level1",
  "address-level2",
  "address-level3",
  "address-level4",
  "address-line1",
  "address-line2",
  "address-line3",
  "bday",
  "bday-day",
  "bday-month",
  "bday-year",
  "billing",
  "cc-additional-name",
  "cc-csc",
  "cc-exp",
  "cc-exp-month",
  "cc-exp-year",
  "cc-family-name",
  "cc-given-name",
  "cc-name",
  "cc-number",
  "cc-type",
  "country",
  "country-name",
  "current-password",
  "email",
  "family-name",
  "fax",
  "given-name",
  "home",
  "honorific-prefix",
  "honorific-suffix",
  "impp",
  "language",
  "mobile",
  "name",
  "new-password",
  "nickname",
  "off",
  "on",
  "organization",
  "organization-title",
  "pager",
  "photo",
  "postal-code",
  "sex",
  "shipping",
  "street-address",
  "tel",
  "tel-area-code",
  "tel-country-code",
  "tel-extension",
  "tel-local",
  "tel-local-prefix",
  "tel-local-suffix",
  "tel-national",
  "transaction-amount",
  "transaction-currency",
  "url",
  "username",
  "work"
]
CrossoriginL = Literal[
  "anonymous",
  "use-credentials"
]
# DirL = Literal[
#   "auto",
#   "ltr",
#   "rtl"
# ]
EnctypeL = Literal["application/x-www-form-urlencoded", "multipart/form-data", "text/plain"]
LoadingL = Literal[
  "eager",
  "lazy"
]
MethodL = Literal[
  "get",
  "post"
]
PreloadL = Literal[
  "auto",
  "metadata",
  "none"
]
PseudoBoolL = Literal[
  "false",
  "true"
]
ReferrerpolicyL = Literal[
  "no-referrer",
  "no-referrer-when-downgrade",
  "origin",
  "origin-when-cross-origin",
  "same-origin",
  "strict-origin-when-cross-origin",
  "unsafe-url"
]
RelL = Literal[
  "alternate",
  "author",
  "bookmark",
  "external",
  "help",
  "license",
  "next",
  "nofollow",
  "noreferrer",
  "noopener",
  "prev",
  "search",
  "tag"
]
TargetL = Literal[
  "_blank",
  "_self",
  "_parent",
  "_top"
]

AreaReferrerpolicyL = ReferrerpolicyL
AreaRelL = RelL
AreaShapeL = Literal[
  "circle",
  "default",
  "poly",
  "rect"
]
AreaTargetL = TargetL
AReferrerpolicyL = ReferrerpolicyL
ARelL = RelL
ATargetL = TargetL
AudioCrossoriginL = CrossoriginL
AudioPreloadL = PreloadL
BaseTargetL = TargetL
ButtonFormenctypeL = EnctypeL
ButtonFormmethodL = MethodL
ButtonFormtargetL = TargetL
ButtonTypeL = Literal[
  "button",
  "reset",
  "submit"
]
DirL = Literal[
  "auto",
  "ltr",
  "rtl"
]
DraggableL = PseudoBoolL
FormAutocompleteL = AutocompleteL
FormEnctypeL = EnctypeL
FormMethodL = MethodL
FormRelL = RelL
FormTargetL = TargetL
HtmlXmlnsL = Literal["http://www.w3.org/1999/xhtml"]
IframeAllowfullscreenL = PseudoBoolL
IframeLoadingL = LoadingL
IframeReferrerpolicyL = ReferrerpolicyL
IframeSandboxL = Literal[
  "allow-forms",
  "allow-pointer-lock",
  "allow-popups",
  "allow-same-origin",
  "allow-scripts",
  "allow-top-navigation"
]
ImgCrossoriginL = CrossoriginL
ImgDecodingL = Literal[
  "async",
  "auto",
  "sync"
]
ImgFetchpriorityL = Literal[
  "auto",
  "high",
  "low"
]
ImgLoadingL = LoadingL
ImgReferrerpolicyL = ReferrerpolicyL
InputAcceptL = Literal[
  "audio/*", 
  "video/*", 
  "image/*"
]
InputAutocompleteL = AutocompleteL
InputFormenctypeL = EnctypeL
InputFormmethodL = MethodL
InputFormtargetL = TargetL
InputmodeL = Literal[
  "email",
  "full-width-latin",
  "kana",
  "kana-name",
  "katakana",
  "latin",
  "latin-name",
  "latin-prose",
  "numeric",
  "tel",
  "url",
  "verbatim"
]
InputTypeL = Literal[
  "button",
  "checkbox",
  "color",
  "date",
  "datetime",
  "datetime-local",
  "email",
  "file",
  "hidden",
  "image",
  "month",
  "number",
  "password",
  "radio",
  "range",
  "reset",
  "search",
  "submit",
  "tel",
  "text",
  "time",
  "url",
  "week"
]
LinkCrossoriginL = CrossoriginL
LinkReferrerpolicyL = ReferrerpolicyL
LinkRelL = RelL
MetaHttp_equivL = Literal[
  "content-security-policy",
  "content-type",
  "default-style",
  "refresh"
]
MetaNameL = Literal[
  "application-name",
  "author",
  "description",
  "generator",
  "keywords",
  "viewport"
]
OlTypeL = Literal[
  "1",
  "A",
  "I",
  "a",
  "i"
]
RoleL = Literal[
  "alert",
  "alertdialog",
  "application",
  "article",
  "banner",
  "button",
  "cell",
  "checkbox",
  "columnheader",
  "combobox",
  "complementary",
  "contentinfo",
  "definition",
  "dialog",
  "directory",
  "doc-abstract",
  "doc-acknowledgments",
  "doc-afterword",
  "doc-appendix",
  "doc-backlink",
  "doc-biblioentry",
  "doc-bibliography",
  "doc-biblioref",
  "doc-chapter",
  "doc-colophon",
  "doc-conclusion",
  "doc-cover",
  "doc-credit",
  "doc-credits",
  "doc-dedication",
  "doc-endnote",
  "doc-endnotes",
  "doc-epigraph",
  "doc-epilogue",
  "doc-errata",
  "doc-example",
  "doc-footnote",
  "doc-foreword",
  "doc-glossary",
  "doc-glossref",
  "doc-index",
  "doc-introduction",
  "doc-noteref",
  "doc-notice",
  "doc-pagebreak",
  "doc-pagelist",
  "doc-part",
  "doc-preface",
  "doc-prologue",
  "doc-pullquote",
  "doc-qna",
  "doc-subtitle",
  "doc-tip",
  "doc-toc",
  "document",
  "feed",
  "figure",
  "form",
  "grid",
  "gridcell",
  "group",
  "heading",
  "img",
  "link",
  "list",
  "listbox",
  "listitem",
  "log",
  "main",
  "marquee",
  "math",
  "menu",
  "menubar",
  "menuitem",
  "menuitemcheckbox",
  "menuitemradio",
  "navigation",
  "none",
  "note",
  "option",
  "presentation",
  "progressbar",
  "radio",
  "radiogroup",
  "region",
  "region",
  "row",
  "rowgroup",
  "rowheader",
  "scrollbar",
  "search",
  "searchbox",
  "separator",
  "slider",
  "spinbutton",
  "status",
  "switch",
  "tab",
  "table",
  "tablist",
  "tabpanel",
  "term",
  "text",
  "textbox",
  "timer",
  "toolbar",
  "tooltip",
  "tree",
  "treegrid",
  "treeitem"
]
ScriptCrossoriginL = CrossoriginL
ScriptReferrerpolicyL = ReferrerpolicyL
SelectAutocompleteL = AutocompleteL
SpellcheckL = PseudoBoolL
TextareaAutocompleteL = AutocompleteL
TextareaWrapL = Literal[
  "hard",
  "soft"
]
ThScopeL = Literal[
  "col",
  "colgroup",
  "row",
  "rowgroup"
]
TrackKindL = Literal[
  "captions",
  "chapters",
  "descriptions",
  "metadata",
  "subtitles"
]
TranslateL = Literal[
  "no",
  "yes"
]
VideoCrossoriginL = CrossoriginL
VideoPreloadL = PreloadL
