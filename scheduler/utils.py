from typing import List


def str_tags_to_list(content: str) -> List:
    content_list = content.split("\n")
    content_list = [item.strip("- ").strip() for item in content_list]

    return content_list
