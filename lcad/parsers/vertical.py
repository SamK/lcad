"""
Print elements in a "vertical" format (like MySQL)
"""
from lcad import log


def dump(data, _):  # pylint: disable=missing-function-docstring
    # friendly convertion from dict to list
    if isinstance(data, dict):
        log.info("Friendly convertion from dict to list")
        data = [data]

    lines = []
    for element in data:
        lines.append("*" * 40)
        col_width = len(max(element.keys()))
        for key, value in element.items():
            lines.append(f"{key: >{col_width}}: {value}")
    return "\n".join(lines)
