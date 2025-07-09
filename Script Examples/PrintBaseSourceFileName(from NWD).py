for model in doc.Models.First.RootItem.Children:
    prop = model.PropertyCategories.FindPropertyByDisplayName("Item","Source File Name")
    sourcefile_long = prop.Value.ToString()
    sourceFileName = sourcefile_long.Replace("DisplayString:", "")
    print(sourceFileName)