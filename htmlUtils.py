import markdownify, markdown, mammoth
from html2docx import html2docx

def convertDocx2HTMl(docx):
    if docx is not None:
        htmlContent = mammoth.convert_to_html(docx).value
        return htmlContent
    return None

def convertHTML2MD(html):
    if html is not None:
        return markdownify.markdownify(html, heading_style="ATX")
    return None

def convertHTML2Docx(html):
    if html is not None:
        return html2docx(html, title="gen_doc")
    return html2docx("<p> ur goofy </p>", title="gen_doc")

def convertMD2HTML(md):
    if md is not None:
        return markdown.markdown(md)
    return None

def convertMD2Docx(md):
    pass

def convertDocx2MD(docx):
    if docx is not None:
        return convertHTML2MD(convertDocx2HTMl(docx))
    return None

