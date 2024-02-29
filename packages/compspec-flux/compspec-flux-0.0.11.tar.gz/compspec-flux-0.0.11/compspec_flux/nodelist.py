import re


# we assume index parts are sane
def expand_nodeids(nodeids):
    """
    Given a list of node ids, expand.

    This expects only very simple directives.
    """
    for bracket in ["[", "]"]:
        nodeids = nodeids.replace(bracket, "")
    parts = list(set(nodeids.split(",")))
    expanded = []
    for part in parts:
        if "-" in part:
            start, end = part.split("-", 2)
            nodeset = range(int(start), int(end) + 1)
            expanded += nodeset
        else:
            expanded.append(int(part))
    return sorted(expanded)


def parse_nodelist(nodelist):
    """
    Parse a nodelist into an actual node list.
    """
    # index pattern
    regex = re.compile(r"(?P<full>(?P<prefix>\w+)(?P<ids>\d+|\[[\d\,\-]+\]),?)")
    nodes = []
    for nodestr in nodelist:
        match = regex.match(nodestr)
        if not match:
            return
        match = match.groupdict()
        nodeids = expand_nodeids(match["ids"])
        prefix = match["prefix"]
        nodes += [f"{prefix}{n}" for n in nodeids]
    return nodes
