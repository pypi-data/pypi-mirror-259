# dlangtools
This module will help you write tokenizers and parsers for your toy languages.

### Lex

Usage of CharIterator:
```python
from dlangtools.lex import CharIterator

src = "Hello, world!"
it = CharIterator(src)

while not it.end():
  if it.check(str.isspace):
    it.skip(str.isspace)
  elif it.check(str.isalnum):
    print(it.location(), 'word:', it.consume(str.isalnum))
  elif it.check(',!'):
    print(it.location(), 'symbol', it.next())
```

Output:
```
(1, 1) word: Hello
(1, 6) symbol ,
(1, 8) word: world
(1, 13) symbol !
```

### Parser
The module has only (for now) an LL(1) parser, which is sufficient for many simple cases such as arithmetic expressions.

Using of Parser:
```python
from dlangtools.parsing import Parser
from dataclasses import dataclasses

@dataclass
class Token:
    type_: str
    value: str
    location: tuple # position in source code (line, column)

tokens = [
    Token(type_='number',    value='1', location=(1, 1)),
    Token(type_='operation', value='+', location=(1, 3)),
    Token(type_='number',    value='2', location=(1, 5)),
    Token(type_='operation', value='*', location=(1, 7)),
    Token(type_='number',    value='3', location=(1, 9)),
]

# BNF form for parser below:
# <additive> ::= <primary> | <primary> '+' <additive>
#  <primary> ::= <value> | <value> '*' <primary>
#    <value> ::= <number> | '(' <additive> ')'

def parse(tokens):
    p = Parser(tokens)

    def value():
        if p.match(('symbol', '(')):
            expr = additive()
            p.consume(('symbol', ')'))
            return expr
        elif p.check('number'): 
            return int(p.next().value)
        else:
            p.error('"(" or number expected instead of "%s"')

    def primary():
        first = value()
        if p.match(('operation', '*')):
            second = primary()
            return ('mul', first, second)
        return first
    
    def additive():
        first = primary()
        if p.match(('operation', '+')):
            second = additive()
            return ('sum', first, second)
        return first
    
    return additive()

tree = parse(tokens)
print(tree) # ('sum', 1, ('mul', 2, 3))
```