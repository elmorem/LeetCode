'''
write a function that, given a string S contains an HTML fragment
- all HTHML tages except (a) and <ing> are completely removed
(a href="url"> tag is replaced with (link:url), where
url is copeid from the orgiinal tag
(img src = 'url"> tage is replaced with image:url) where url is copied from the original tag
in the text all symbols except english letters and digits are removed (=except in the URLS from (a> and <img> tags
words are converted to lower case
all words separated by one space))

'''
from html.parser import HTMLParser
import re

def solution(S):
    class Cleaner(HTMLParser):
        def __init__(self):
            super().__init__()
            # the super() init cal is crutial here because it sets up the parse and makes sure that it get initialized properly
            # so that. without it, our parser wouldn't work properly
            #we need these because we are going to initialize a parser and then feed the string to it.  
            self.out = []
        def handle_starttag( self, tag, attrs):
            attrs = dict(attrs)
            if tag == "a":
                href = attrs.get("href")
                if href:
                    self.out.append(f"(link:{href})")
            elif tag == "img":
                src = attrs.get("src")
                if src:
                    self.out.append(f"(image:{src})")
                    
        def handle_data(self, data):
            words = re.findall(r"[A-Za-z0-9]+", data)
            self.out.extend(w.lower() for w in words)

    parser = Cleaner()
    parser.feed(S)
    parser.close()
    
    return " ".join(parser.out)
if __name__ == "__main__":
    S = '<div>Hello <a href="http://example.com">Example</a>! Here is an image: <img src="http://example.com/image.png"></div>'
    print(solution(S))  # Expected output: "hello (link:http://example.com) example here is an image (image:http://example.com/image.png)"
    S = '<p>Check this out: <a href="https://openai.com">OpenAI</a> and this image <img src="https://openai.com/logo.png"></p>'
    print(solution(S))  # Expected output: "check this out (link:https://openai.com) openai and this image (image:https://openai.com/logo.png)"

    s1 = "<p>hello, ... WORLD!</p>"
    print(solution(s1))
    s2 = "<a href='toptal.com'>Toptal_URL</a>now<img src='logo.png'>end"
    print(solution(s2))  # Expected: "(link:toptal.com) toptal url now (image:logo.png) end"