#FreeCAD macro, designed to be run from inside the program
import Part

doc = FreeCAD.newDocument()
#doc = FreeCAD.ActiveDocument()
box = doc.addObject("Part::Box", "CanisterBottom")
box.Height = 2
box.Width = 10
box.Length = box.Width

#recompute after changing an object's properties
doc.recompute()

box = doc.addObject("Part::Box", "CanisterTop")
box.Height = 2
box.Width = 10
box.Length = box.Width
box.Placement.Base = (0,0,10)
#movevector = FreeCAD.Vector(0,0,10)
#doc.setEdit('CanisterTop',0)
#box.Placement.Base = movevector

#adding the fuel cells
FuelCell = doc.addObject("Part::Box", "Cell1")
FuelCell.Height = 2
FuelCell.Width = 8
FuelCell.Length = FuelCell.Width
FuelCell.Placement.Base = (1,1,2)
FuelCell = doc.addObject("Part::Box", "Cell2")
FuelCell.Height = 2
FuelCell.Width = 8
FuelCell.Length = FuelCell.Width
FuelCell.Placement.Base = (1,1,4)
FuelCell = doc.addObject("Part::Box", "Cell3")
FuelCell.Height = 2
FuelCell.Width = 8
FuelCell.Length = FuelCell.Width
FuelCell.Placement.Base = (1,1,6)
FuelCell = doc.addObject("Part::Box", "Cell4")
FuelCell.Height = 2
FuelCell.Width = 8
FuelCell.Length = FuelCell.Width
FuelCell.Placement.Base = (1,1,8)
doc.recompute()

#make bolts that hold top to bottom
LeftFrontBolt = Part.makeCylinder(1,12)
LeftFrontBolt.Placement.Base = (1,1,0)
RightFrontBolt = Part.makeCylinder(1,12)
RightFrontBolt.Placement.Base = (box.Width-1,1,0)
LeftRearBolt = Part.makeCylinder(1,12)
LeftRearBolt.Placement.Base = (1,box.Length-1,0)
RightRearBolt = Part.makeCylinder(1,12)
RightRearBolt.Placement.Base = (box.Width-1,box.Length-1,0)
doc.recompute()

#Handles for the cell
LeftHandle = doc.addObject
doc.recompute()

#Electrical lines

doc.recompute
#final line
doc.recompute()


#How to query an object
#myObject = FreeCAD.ActiveDocument.Get("myObjectname")
#myObject.<type>