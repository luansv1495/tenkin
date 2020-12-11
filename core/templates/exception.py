
def html_base(content: str):
    return f"<html><head><meta charset=\"UTF-8\"></head><body>{content}</body></html>"

def template_project_run_found(error: str):
    return html_base(content=f"<center><strong>{error}</strong></center>")