virtualenv -q VENV
.\VENV\scripts\activate -q && pip3 -q install --upgrade pandas tldextract && python iab_google_mapping.py && deactivate