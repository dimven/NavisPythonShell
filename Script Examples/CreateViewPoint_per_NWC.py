# Search
s = Search()
s.Selection.SelectAll()
# variant needed for equals Value
# oData = VariantData.FromDisplayString('Rooms')
sc1 = SearchCondition.HasPropertyByDisplayName("Item","Name")
# oSearchCondition = oSearchCondition.EqualValue(oData)
sc1 = sc1.DisplayStringContains('.nwc')
s.SearchConditions.Add(sc1)
a = s.FindAll(doc,False)

# Create Collection and fill it with the items found
modelItems = ModelItemCollection()
a.CopyTo(modelItems)

# Loop through collection of found items
for item in modelItems:
    # Get some properties to build the view name later
    # This would change for OPD use case
    #number = item.PropertyCategories.FindPropertyByDisplayName('Element', 'Number')
    #strnumb = number.Value.ToDisplayString()
    name = item.PropertyCategories.FindPropertyByDisplayName ('Item', 'Name')
    strname = name.Value.ToDisplayString()
    # This next pert is locating the camera, so if we're focusing on an item, 
    # then OPD will again need to tweak this section to put the camera 
    # in the correct location and orientation
    bbc = item.BoundingBox().Center
    nvp = Viewpoint()
    nvp.Position = bbc
    vt = Vector3D(0,1,0)
    nvp.AlignDirection(vt)
    nvp.RenderStyle.Shaded
    nvp.HeightField = 0.872657
    # Save the settings to a view
    svp = SavedViewpoint(nvp)
    #svp.DisplayName = strnumb + " " + strname
    svp.DisplayName = strname
    print svp.DisplayName
    doc.SavedViewpoints.AddCopy(svp)