import markdown
from markdown.extensions.toc import TocExtension
from pathlib import Path

ANCHORLINK = True
TOC_DEPTH_DEFAULT = 3
MD_PATH = r"rules-ue.md"
HEAD_PATH = r"header.html"
FOOT_PATH = r"footer.html"

def input_toc_depth(default=True):
    print("Setting ToC Depth")
    output = TOC_DEPTH_DEFAULT
    if not default:
        toc_input = input(f"ToC Depth = {TOC_DEPTH_DEFAULT}, update? ")
        if toc_input != "":
            output = toc_input
    return output

def set_out_path(depth):
    print("Setting destination file")
    base_dir = Path(__file__).resolve().parent
    out_dir = base_dir.joinpath()
    name = "rules-toc"
    out_path = out_dir.joinpath(f'site/{name}{depth}.html')
    return out_path

def md_to_html_file(p,toc_depth,out_path):
    """pathlib.Path markdown file to html file"""
    with open(p, "r", encoding="utf-8") as input_file:
        text = input_file.read()
    md = markdown.Markdown(extensions=[TocExtension(toc_depth=toc_depth, anchorlink=ANCHORLINK)])
    html = md.convert(text)
    print(f" md_to_html: SAVING .md as .html: {out_path}")
    with open(out_path, "a", encoding="utf-8", errors="xmlcharrefreplace") as out_file:
        out_file.write(html)
    return out_path

def add_to_file(add_file, out_path, new_file):
    if new_file is True:
        permission = "w"
    else:
        permission = "a"
    with open(add_file, "r", encoding="utf-8") as input_file:
        style = input_file.read()
    with open(out_path, permission, encoding="utf-8", errors="xmlcharrefreplace") as out_file:
        out_file.write(style)

def build_file(depth, out_path):
    print("Building file")
    add_to_file(HEAD_PATH, out_path, True)
    md_to_html_file(MD_PATH, depth, out_path)
    add_to_file(FOOT_PATH, out_path, False)

def main(input=False):
    depth = input_toc_depth(default= not input)
    out_path = set_out_path(depth)
    build_file(depth, out_path)
    if not input:
        depth = 2
        out_path = set_out_path(depth)
        build_file(depth, out_path)

if __name__ == '__main__':
    main()
