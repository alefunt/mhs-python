def create_document(body:str):
    return f"""\\documentclass{{article}}
\\begin{{document}}

{body}

\\end{{document}}"""