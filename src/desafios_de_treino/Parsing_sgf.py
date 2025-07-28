import re
from typing import Dict, List, Union


def parse(input_string: str) -> Dict[str, Union[Dict[str, List[str]], List]]:
    """
    Parse an SGF string into a tree structure represented as nested dictionaries and lists.

    Args:
        input_string: The SGF string to parse

    Returns:
        A dictionary with 'properties' and 'children' keys representing the parsed tree

    Raises:
        ValueError: For various parsing errors with descriptive messages
    """
    if not input_string:
        raise ValueError("tree missing")

    if not (input_string.startswith("(") and input_string.endswith(")")):
        raise ValueError("tree missing")

    content = input_string[1:-1].strip()

    if not content.startswith(";"):
        raise ValueError("tree with no nodes")

    nodes = _split_nodes(content)
    if not nodes:
        raise ValueError("tree with no nodes")

    root_node = nodes[0]
    child_nodes = nodes[1:]

    properties = _parse_properties(root_node)
    children = []

    for child in child_nodes:
        try:
            children.append(parse(f"({child})"))
        except ValueError as e:
            raise ValueError(f"invalid child node: {child}") from e

    return {"properties": properties, "children": children}


def _split_nodes(input_str: str) -> List[str]:
    """
    Split an SGF content string into individual node strings.

    Handles nested nodes and variations in the SGF tree structure.
    """
    nodes = []
    current = []
    depth = 0
    i = 0

    while i < len(input_str):
        char = input_str[i]

        if char == "(":
            if depth == 0 and current and current[0] == ";":
                nodes.append("".join(current))
                current = []
            depth += 1
        elif char == ")":
            depth -= 1

        current.append(char)

        if depth == 0 and current and current[0] == ";":
            nodes.append("".join(current))
            current = []
            # Skip any whitespace between nodes
            while i + 1 < len(input_str) and input_str[i + 1].isspace():
                i += 1

        i += 1

    if depth != 0:
        raise ValueError("unbalanced parentheses")

    return nodes


def _parse_properties(node_str: str) -> Dict[str, List[str]]:
    """
    Parse a single SGF node string into its properties dictionary.

    Properties are key-value pairs where keys must be uppercase and values
    can be multiple values enclosed in brackets.
    """
    if not node_str.startswith(";"):
        raise ValueError("properties without node")

    remaining = node_str[1:].lstrip()
    properties = {}

    while remaining:
        # Match property identifier (must be uppercase)
        prop_match = re.match(r"^([A-Za-z]+)", remaining)
        if not prop_match:
            break

        prop_id = prop_match.group(1)
        if not prop_id.isupper():
            raise ValueError("property must be in uppercase")

        remaining = remaining[len(prop_id) :].lstrip()

        if not remaining.startswith("["):
            raise ValueError("properties without delimiter")

        values = []
        while remaining.startswith("["):
            value, remaining = _parse_value(remaining[1:])
            values.append(value)
            remaining = remaining.lstrip()

        properties[prop_id] = values

    return properties


def _parse_value(value_str: str) -> tuple:
    """
    Parse a single property value from an SGF string.

    Handles escaped characters and special sequences according to SGF Text type rules.
    """
    value = []
    i = 0
    escaped = False

    while i < len(value_str):
        char = value_str[i]

        if escaped:
            if char == "t":
                value.append(" ")
            elif char == "n":
                value.append("\n")
            elif char in ["\\", "]"]:
                value.append(char)
            else:
                value.append("\\")
                value.append(char)
            escaped = False
            i += 1
        elif char == "\\":
            escaped = True
            i += 1
        elif char == "]":
            return ("".join(value), value_str[i + 1 :])
        else:
            value.append(char)
            i += 1

    raise ValueError("unclosed property value")
