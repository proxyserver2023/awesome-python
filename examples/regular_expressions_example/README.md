### Anchors - ^ and $
  ```
  ^ - start
  $ - End
  ^The end$ - matches The end
  ```

### Quantifiers - * + ? and {}
  ```
  *           - zero or more
  +           - one or more
  ?           - zero or one
  {n}         - exactly n times
  {n,}        - n+
  {m,n}       - m >= and <= n

  abc*        -  ab followed by zero or more c
  abc+        -  ab followed by one or more c
  abc?        -  ab followed by zero or one c
  abc{2}      -  ab followed by 2 c
  abc{2,}     -  ab followed by 2 or more c
  abc{2,5}    -  ab followed by 2 up to 5 c
  a(bc)*      -  a followed by zero or more copies of the sequence bc
  a(bc){2,5}  -  a followed by 2 up to 5 copies of the sequence bc
  ```

### OR Operator - | or []
  ```
  a(b|c)     matches a string that has a followed by b or c
  a[bc]      same as previous
  ```

### Character classes - \d \w \s and .
  ```
  \d         -  a single character that is a digit
  \D         -  a single character that is NOT a digit
  \w         -  a word character (alphanumeric character plus underscore)
  \W         -  a NON word character (alphanumeric character plus underscore)
  \s         -  a whitespace character (includes tabs and line breaks)
  \S         -  a NON whitespace character (includes tabs and line breaks)
  .          -  any character
  ```

### Flags
  1. g (global) does not return after the first match, restarting the subsequent searches from the end of the previous match
  2. m (multi line) when enabled ^ and $ will match the start and end of a line, instead of the whole string
  3. i (insensitive) makes the whole expression case-insensitive (for instance /aBc/i would match AbC)

### Grouping and Capturing ()
  ```
  a(bc)           parentheses create a capturing group with value bc
  a(?:bc)*        using ?: we disable the capturing group
  a(?<foo>bc)     using ?<foo> we put a name to the group
  ```

### Bracket Expressions - []
  ```
  [abc]               - a or b or c
  [a-c]               - a or b or c
  [a-fA-F0-9]         - a-f or A-F or 0-9
  [0-9]%              - a character from 0 to 9 before a % sign.
  [^a-zA-Z]           - NOT [a-z or A-Z]
  ```
