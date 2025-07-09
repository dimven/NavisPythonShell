# Search
# first build a collection of objects that have an area.
# in order to get a list of all the areas available
# search doesn't work for custom categories, must iterate
areas = dict()
allItems = doc.Models.RootItemDescendantsAndSelf
for item in allItems:
    prop = item.PropertyCategories.FindPropertyByDisplayName('OPD_LineList','Area')
    if prop:
        areaName = prop.Value.ToDisplayString()
        if areaName not in areas.keys():
            mic = ModelItemCollection()
            mic.Add(item)
            areas[areaName] = mic
        else:
            mic = areas[areaName]
            mic.Add(item)
            areas[areaName] = mic

for area, mic in areas.items():
    # remove existing viewpoint if exists
    vps = doc.SavedViewpoints.RootItem.Children
    for svp in vps:
        vpName = svp.DisplayName.ToString()
        if (vpName == area):
            doc.SavedViewpoints.Remove(svp)
    # set all of model transparency
	# might be worth seeing if the viewpoint can just be edited for items visibility instead of editing the model
    doc.Models.OverrideTemporaryTransparency(doc.Models.RootItemDescendants,50)
    # set for current area to no transparency
    doc.Models.OverrideTemporaryTransparency(mic,0)
    bbc = mic.BoundingBox().Center
    nvp = Viewpoint()
    nvp.Position = bbc
    vt = Vector3D(0,1,0)
    nvp.AlignDirection(vt)
    nvp.RenderStyle.Shaded
    nvp.HeightField = 0.872657
    svp = SavedViewpoint(nvp)
    svp.DisplayName = area
    print svp.DisplayName
    doc.SavedViewpoints.AddCopy(svp)
    
