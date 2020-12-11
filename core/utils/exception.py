
exceptions = {
    "project_in_run":{
        "FileNotFoundError": "O diretório expecificado não corresponde a um projeto tenkin!"
    }
}

def exception_project_in_run(exception_name: str):
    if exception_name in exceptions['project_in_run']: return exceptions['project_in_run'][exception_name]
    return True