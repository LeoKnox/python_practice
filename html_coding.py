Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
>>> sys.platorm
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    sys.platorm
AttributeError: module 'sys' has no attribute 'platorm'
>>> import html
>>> html.escape("This HTML fragmanet contains a <script>script</script> tag.")
'This HTML fragmanet contains a &lt;script&gt;script&lt;/script&gt; tag.'
>>> html.unescape ("I &hearts; Python's &lt;standard library&gt;.")
"I ♥ Python's <standard library>."
>>> 