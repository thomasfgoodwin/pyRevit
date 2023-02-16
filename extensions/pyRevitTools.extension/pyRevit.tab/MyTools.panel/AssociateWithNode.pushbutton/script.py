
__title__ = 'Associate a family with a Graphviz node'
from Autodesk.Revit import DB


doc = __revit__.ActiveUIDocument.Document
selection = __revit__.ActiveUIDocument.Selection

selection = [doc.GetElement(x) for x in selection.GetElementIds()]

t = DB.Transaction(doc, __title__)
t.Start()
for x in selection:
    node_parameter = x.LookupParameter('Node')
    print(node_parameter.AsString())
    node_parameter.Set('Set by script')
    print(node_parameter.AsString())
    for p in x.Parameters:
        if p.IsShared:
            print(p.Definition.Name, p.Id)
t.Commit()

# Creating collector instance and collecting all the walls from the model
wall_collector = DB.FilteredElementCollector(doc)\
                   .OfCategory(DB.BuiltInCategory.OST_Walls)\
                   .WhereElementIsNotElementType()


# Iterate over wall and collect Volume data
total_volume = 0.0
selected_volume = 0.0

for wall in wall_collector:
    vol_param = wall.Parameter[DB.BuiltInParameter.HOST_VOLUME_COMPUTED]
    if vol_param:
        total_volume = total_volume + vol_param.AsDouble()


for wall in selection:
    vol_param = wall.Parameter[DB.BuiltInParameter.HOST_VOLUME_COMPUTED]
    if vol_param:
        selected_volume = selected_volume + vol_param.AsDouble()

# now that results are collected, print the total
print("Total Volume of selected walls in model is: {}".format(selected_volume))

print("Total Volume of all walls in model is: {}".format(total_volume))


"""from Autodesk.Revit.DB import *
outlet_ID = ElementId(1109535)
outlet = doc.GetElement(outlet_ID)
print(list(outlet.Parameters))
for p in outlet.Parameters:
	print(p.Definition.Name)"""