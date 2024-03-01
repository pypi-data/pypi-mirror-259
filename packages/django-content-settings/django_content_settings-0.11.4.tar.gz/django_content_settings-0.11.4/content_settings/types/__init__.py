PREVIEW_HTML = "html"
PREVIEW_TEXT = "text"
PREVIEW_PYTHON = "python"
PREVIEW_NONE = "none"

PREVIEW_ALL = [
    value for name, value in globals().items() if name.startswith("PREVIEW_")
]


class required:
    pass


class optional:
    pass


def pre(value: str) -> str:
    return "<pre>{}</pre>".format(str(value).replace("<", "&lt;"))
