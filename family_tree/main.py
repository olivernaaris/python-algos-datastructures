from asciitree import LeftAligned
from collections import OrderedDict as OD


class Element:
    def __init__(self, name, index, parent_id):
        self.name = name
        self.index = index
        self.parent_id = parent_id

    def __str__(self):
        return "[{}, {}, {}]".format(self.name, self.index, self.parent_id)

    def __repr__(self):
        return "[{}, {}, {}]".format(self.name, self.index, self.parent_id)


items = {}
items_that_share_parent = {}


with open("family-tree.csv", "r") as fp:
    line = fp.readline()
    idx = 1
    while line:
        stripped = line.strip()
        split = stripped.split(",")
        parent_id = int(split[1])
        name = split[2].strip()
        element = Element(name, idx, parent_id)
        items[idx] = element
        holder = items_that_share_parent.get(parent_id, [])
        holder.append(element)
        items_that_share_parent[parent_id] = holder
        line = fp.readline()
        idx = idx + 1
        if idx > 100:
            break


def build_tree(index, depth):
    if depth <= 0:
        return {}
    children = items_that_share_parent.get(index, [])
    return OD([(e.name, build_tree(e.index, depth -1)) for e in children])


sample_idx = 2
tree = {items[sample_idx].name: build_tree(sample_idx, 10)}
tr = LeftAligned()
print(tr(tree))
