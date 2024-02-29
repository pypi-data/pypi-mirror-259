class IteratorException(Exception):
    def __init__(self, line, column, message):
        super().__init__(message)
        self.line = line
        self.column = column

class CharIterator:
    def __init__(self, string):
        self.string = string
        self.reset()

    def end(self):
        return self.pos >= len(self.string)

    def current(self):
        if self.end(): return chr(0)
        else: return self.string[self.pos]

    def next(self, line_separator='\n'):
        ch = self.current()
        self.pos += 1
        if ch == line_separator:
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        return ch

    def check(self, checker):
        ch = self.current()
        if self.end(): return False

        if callable(checker):
            return checker(ch)
        elif type(checker) == str:
            return (ch in checker)
        else:
            return False

    def match(self, checker):
        is_matched = False
        if self.check(checker):
            self.next()
            is_matched = True
        return is_matched

    def consume(self, checker):
        buffer = []
        while self.check(checker):
            buffer.append(self.next())
        return "".join(buffer)

    def expect(self, checker, message):
        if not self.match(checker):
            raise IteratorExcepton(self.line, self.column, message)

    def skip(self, checker):
        while self.check(checker): self.next()

    def location(self):
        return self.line, self.column

    def reset(self):
        self.pos = 0
        self.line = 1
        self.column = 1

    def truncate(self):
        self.string = self.string[max(self.pos-1, 0):]
