from flask import url_for
from www import app
import urlparse

def static(path):
    root = app.config.get('STATIC_ROOT')
    if app.debug or root is None:
        return url_for('static', filename=path)
    else:
        return urlparse.urljoin(root, path)

def ext(path):
    root = app.config.get('EXT_ROOT')
    if app.debug or root is None:
        return url_for('static', filename=path)
    else:
        return urlparse.urljoin(root, path)

@app.context_processor
def context_processor():
    return dict(static=static, ext=ext)
