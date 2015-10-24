import unittest

def set_analysis(a, b):
“””output intersection of a and b, items in a but not b, items in b but not a”””
    # assume they are lists
    a_dict = {}
    for item in a:
        a_dict[item] = True
    b_dict = {}
    for item in b:
        b_dict[item] = True
    # find intersection of a and b
    intersection_items = []
    for item in a:
        if b_dict.get(item) == True:
            intersection_items.append(item)

    # Find items that are in a but not b
    a_but_not_b_items = []
    for item in a:
        if not (b_dict.get(item) == True):
            a_but_not_b_items.append(item)
    b_but_not_a_items = []
    for item in b:
        if not (a_dict.get(item) == True):
            b_but_not_a_items.append(items)

    return (intersection_items, a_but_not_b_items, b_but_not_a_items)


class TestSetAnalaysis(unittest.TestCase):
    def test_intersection(self):
        result = set_analysis()


_____________________________________________________

CSV
id, parent, weight

id,parent,weight
30,0,10
0,-1,1
20,30,2

Node {
  int id;
  int parent;
  int weight;
  // ... you can add other fields right here, if necessary
}

def find_tree_weight(nodes, target_node_id):
     # [{“id”: 10, “parent”: 30, “weight”: 1}]
     # Treeify nodes
     # First find the root
     root_id = None
     for node in nodes:
         if node[‘parent’] == -1:
             root_id = node[‘id’]

     nodes_by_id = {}
     for node in nodes:
         nodes_by_id[node[‘id’]] == node

     # Now set children references
     for node in nodes:
         parent_node = nodes_by_id[node[‘parent’]]
         if parent_node.get(‘children’) == None:
             parent_node[‘children’] == []
         parent_node[‘children’].append(node[‘id’])

     # Now that we have the tree, let’s walk the subtree and calculate weight
  return calculate_subtree_weight(nodes_by_id, target_node_id)

def calculate_subtree_weight(nodes_by_id, root_id):
    root_node = nodes_by_id[root_id]
    total_weight = root_node[‘weight’]

    # not all nodes have children wacthout!
    if root_node.get(‘children’) is not None:
        for child_id in root_node[‘children’]:
            child = nodes_by_id[child_id]
            if child.get(‘subtree_weight’):
                total_weight += child.get(‘subtree_weight’)
            else:
                child[‘subtree_weight’] = calculate_subtree_weight(child_id)
                total_weight += child[‘subtree_weight’]
    return total_weight



# Does this handle a cyclical (broken) tree?, ie.
# 0, 1, 10
# 1, 0, 10

