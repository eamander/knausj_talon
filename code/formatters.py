from talon import Module, Context, actions, ui
from typing import List, Union

ctx = Context()
key = actions.key

words_to_keep_lowercase = "a,an,the,at,by,for,in,is,of,on,to,up,and,as,but,or,nor".split(",")

def surround(by):
    def func(i, word, last):
        if i == 0:
            word = by + word
        if last:
            word += by
        return word

    return func

def FormatText(m, fmtrs):
    if m._words[-1] == "over":
        m._words = m._words[:-1]
    try:
        words = actions.dictate.parse_words(m)
        words = actions.dictate.replace_words(words)
    except AttributeError:
        with clip.capture() as s:
            edit.copy()
        words = s.get().split(" ")
        if not words:
            return
    
    return format_text_helper(words, fmtrs)

def format_text_helper(words, fmtrs):
    tmp = []
    spaces = True
    for i, w in enumerate(words):
        for name in reversed(fmtrs):
            smash, func = formatters_dict[name]
            w = func(i, w, i == len(words) - 1)
            spaces = spaces and not smash
        tmp.append(w)
    words = tmp

    sep = " "
    if not spaces:
        sep = ""
    return sep.join(words)

NOSEP = True
SEP   = False

def words_with_joiner(joiner):
    def formatter_function(i, word, _):
        return word if i == 0 else joiner + word
    return (NOSEP, formatter_function)

formatters_dict = {
    # True -> no separator
    "dunder": (NOSEP, lambda i, word, _: "__%s__" % word if i == 0 else word),
    "camel": (NOSEP, lambda i, word, _: word if i == 0 else word.capitalize()),
    "hammer" : (NOSEP, lambda i, word, _: word.capitalize()),
    "snake": (NOSEP, lambda i, word, _: word.lower() if i == 0 else "_" + word.lower()),
    "smash": (NOSEP, lambda i, word, _: word),
    "kebab": words_with_joiner("-"),
    "packed": words_with_joiner("::"),
    "allcaps": (SEP, lambda i, word, _: word.upper()),
    "alldown": (SEP, lambda i, word, _: word.lower()),
    "dubstring": (SEP, surround('"')),
    "string": (SEP, surround("'")),
    "padded": (SEP, surround(" ")),
    "dotted": words_with_joiner("."),
    "slasher": (NOSEP, lambda i, word, _: "/" + word),
    "sentence": (SEP, lambda i, word, _: word.capitalize() if i == 0 else word),
    "title": (SEP, lambda i, word, _:  word.capitalize() if i == 0 or word not in words_to_keep_lowercase else word)
}

mod = Module()
mod.list('formatters', desc='list of formatters')

@mod.capture
def formatters(m) -> List[str]:
    "Returns a list of formatters"

@mod.capture
def format_text(m) -> str:
    "Formats the text and returns a string"

@mod.action_class
class Actions:
    def formatters_format_text(text: Union[str, List[str]], fmtrs: List[str]) -> str:
        """Formats a list of parsed words given a list of formatters"""
        if isinstance(text, list):
            return format_text_helper(text, fmtrs)
        else:
            return format_text_helper([text], fmtrs)
        
@ctx.capture(rule='{self.formatters}+')
def formatters(m):
    return m.formatters
 
@ctx.capture(rule='<self.formatters> <dgndictation>')
def format_text(m):
    return FormatText(m.dgndictation, m.formatters)

ctx.lists['self.formatters'] = formatters_dict.keys()