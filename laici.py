#!/usr/bin/env python3.6

import re
import requests

from bs4 import BeautifulSoup


def format_line(line):
    line = re.sub(re.compile(r"^<center>(.*)</center>$", re.MULTILINE|re.DOTALL), "\\\\begin{center}\\1\end{center}", str(line).strip())
    line = re.sub(r"<br/>", "\n", line)
    line = line.replace("<b>", "\\textbf{").replace("</b>", "}")
    line = line.replace("<i>", "\\textit{").replace("</i>", "}")
    line = re.sub(re.compile(r"<p.*?>", re.MULTILINE|re.DOTALL), "", line)
    line = re.sub(re.compile(r"</p>", re.MULTILINE|re.DOTALL), "", line)
    line = re.sub(re.compile(r"<font.*?>", re.MULTILINE|re.DOTALL), "", line)
    line = re.sub(re.compile(r"</font>", re.MULTILINE|re.DOTALL), "", line)
    line = re.sub(re.compile(r"<span.*?>", re.MULTILINE|re.DOTALL), "", line)
    line = re.sub(re.compile(r"</span>", re.MULTILINE|re.DOTALL), "", line)
    line = re.sub(re.compile(r"<a.*?>", re.MULTILINE|re.DOTALL), "", line)
    line = re.sub(re.compile(r"</a>", re.MULTILINE|re.DOTALL), "", line)
    return(line)


if __name__ == '__main__':
    url = "http://w2.vatican.va/content/john-paul-ii/en/apost_exhortations/documents/hf_jp-ii_exh_30121988_christifideles-laici.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    text_selector = "#corpo > div.documento > div > div.text.parbase.container.vaticanrichtext"
    text_html = soup.select(text_selector)[0]
    lines = []
    for child in text_html.children:
        try:
            if child.text.strip():
                lines.append(child)
        except AttributeError:
            if child.strip():
                lines.append("<p>{}</p>".format(child))

    lines = [format_line(line) for line in lines]
    output = "\n".join(lines)
    with open("laici.tex", "w") as f:
        f.write(output)
