#! python3
import sys
import clr

import Autodesk.Revit.DB as DB

__title__ = 'Associate a family with a Graphviz node'
# from Autodesk.Revit import DB
from pyrevit import script
# import json
# import sys
# import graphviz
# import graphviz
# print(help("modules"))
# doc = __revit__.ActiveUIDocument.Document
# selection = __revit__.ActiveUIDocument.Selection

# selection_ids = [x for x in selection.GetElementIds()]

# data = {}
# for item_id in selection_ids:
#     element = doc.GetElement(item_id)
#     unique_id = element.UniqueId
#     # parameter = element.LookupParameter('Node')
#     parameter = DB.BuiltInParameter.ALL_MODEL_MARK
#     mark = element.get_Parameter(parameter).AsString()
#     data[unique_id] = 'Set by script'


# file = script.get_document_data_file('node_table', 'json', add_cmd_name=False)
# print(file)
# print(data)
# with open(file, 'w') as write_file:
#          json.dump(data, write_file)

