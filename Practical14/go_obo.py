import re
import xml.dom.minidom
import openpyxl as xl

def find_child_nodes(node_id, id_list, is_list, counter):
    if node_id not in is_list:
        return counter
    indices = [i for i, val in enumerate(is_list) if val == node_id]
    for pos in indices:
        counter = find_child_nodes(id_list[pos], id_list, is_list, 
counter)
        counter += 1
    return counter

DOMtree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMtree.documentElement
goobos = collection.getElementsByTagName("term")

is_a_ID = []
is_a = []

for goobo in goobos:
    ID = goobo.getElementsByTagName("id")[0].childNodes[0].data
    child_nodes = goobo.getElementsByTagName("*")
    for node in child_nodes:
        if node.tagName == "is_a":
            for child_node in node.childNodes:
                is_a_ID.append(ID)
                is_a.append(child_node.data)

workbook = xl.Workbook()
sheet = workbook.active
sheet.append(["id", "name", "definition", "childnodes"])

for goobo in goobos:
    defstr = goobo.getElementsByTagName("defstr")[0].childNodes[0].data
    if re.search("Autophagosome", defstr, flags=re.I):
        IDauto = goobo.getElementsByTagName("id")[0].childNodes[0].data
        name = goobo.getElementsByTagName("name")[0].childNodes[0].data
        child_nodes = find_child_nodes(IDauto, is_a_ID, is_a, 0)
        sheet.append([IDauto, name, defstr, child_nodes])

workbook.save(filename='autophagosome.xlsx')
