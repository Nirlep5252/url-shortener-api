import re


def is_valid_url(url: str) -> bool:
    regex = re.compile(
        r"(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})(\.[a-zA-Z0-9]{2,})?",
        re.IGNORECASE,
    )
    return re.match(regex, url) is not None
