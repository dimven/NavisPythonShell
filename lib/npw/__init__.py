import clr
clr.AddReference('Autodesk.Navisworks.Api')
import Autodesk.Navisworks.Api as API


doc = API.Application.ActiveDocument
selection = doc.CurrentSelection.SelectedItems
