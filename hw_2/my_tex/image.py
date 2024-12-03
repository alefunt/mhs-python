def preamble(path_to_images:str):
    return f"""\\usepackage{{graphicx}}
\\graphicspath{{ {{{path_to_images}}} }}
"""

def create_image(name:str):
    return f"\\includegraphics{{{name}}}"