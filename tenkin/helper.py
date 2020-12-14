from tenkin.uix.styles import styles_global
import json

def generate_css_from_list(tag_list: list):
    css = ''
    for tag in tag_list:
        style_json = json.dumps(styles_global[tag],indent=4)
        style = str(style_json).replace('"',"").replace(",",";").replace('\\','"')
        css += "."+tag+" "+style+"\n"
    return css