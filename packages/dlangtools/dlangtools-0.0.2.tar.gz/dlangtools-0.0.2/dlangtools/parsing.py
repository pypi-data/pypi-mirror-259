class ParsingError(Exception):
    def __init__(self, location, message):
        self.location = location
        self.message = message
    
    def __str__(self):
        return f'{self.location}: {self.message}'


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    
    def eof(self):
        return self.pos >= len(self.tokens)
    
    def check(self, predicate):
        if self.eof(): return False
        if type(predicate) == tuple:
            t = self.tokens[self.pos]
            return predicate == (t.type_, t.value) 
        elif callable(predicate):
            return predicate(self.tokens[self.pos])
        elif type(predicate) == str:
            return predicate == self.tokens[self.pos].type_
        else:
            return False
    
    def next(self):
        if self.eof():
            return None
        token = self.tokens[self.pos]
        self.pos += 1
        return token
    
    def match(self, predicate):
        if self.check(predicate):
            return self.next()
        return False
    
    def consume(self, predicate):
        result = self.match(predicate)
        if not result:
            t = self.next()
            raise ParsingError(t.location, f"unexpected token '{t.value}'")
        return result
    
    def error(self, message):
        t = self.next()
        raise ParsingError(t.location, message % t.value)