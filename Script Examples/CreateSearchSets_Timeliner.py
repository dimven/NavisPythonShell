import datetime
# build period names from start to end
# set the periods from the beginning of the job to the end of the job
SearchFolderName = 'OPD_TimeLiner'
yr_beg = 2023
wk_beg = 51
yr_end = 2025
wk_end = 9
listof = []
for y in range(yr_beg, yr_end + 1):
    if yr_beg == yr_end:
        wlist = [str(y)] + [str(y) + '.' + element.__str__() for element in range(wk_beg, wk_end + 1)]
    elif y == yr_end:
        wlist = [str(y)] + [str(y) + '.' + element.__str__() for element in range(1, wk_end + 1)]
    elif y == yr_beg:
        wlist = [str(y)] + [str(y) + '.' + element.__str__() for element in range(wk_beg, 53 + 1)]
    else:
        wlist = [str(y)] + [str(y) + '.' + element.__str__() for element in range(1, 53 + 1)]
    listof.append(wlist)

#confirm SearchFolderName doesn't already exist, rename _old
for ss in doc.SelectionSets.RootItem.Children:
    if ss.DisplayName == SearchFolderName and ss.IsGroup:
        doc.SelectionSets.EditDisplayName(ss, SearchFolderName + "_old")
        # perhaps the old one should just be deleted

#create new "timeliner" folder at the end of the existing search sets
nextIndex = doc.SelectionSets.RootItem.Children.Count
savedFolder = FolderItem()
savedFolder.DisplayName = SearchFolderName

for y in listof:
    yr = y[0]
    yearFolder = FolderItem()
    yearFolder.DisplayName = str(yr)
    for wk in y[1:]:
        # create another folder group for each year
        s = Search()
        # sc = SearchCondition.HasPropertyByDisplayName('OPD_LineList','SCHEDULED INSTALL')
        # ABOVE IS CORRECT, BELOW IS FOR TESTING AND PROOF OF CONCEPT
        sc = SearchCondition.HasPropertyByDisplayName('OPD_Schedule','SCHEDULED INSTALL')
        oData = VariantData.FromDisplayString(wk)
        sc = sc.EqualValue(oData)
        s.SearchConditions.Add(sc)
        s.Selection.SelectAll()
        s.Locations = SearchLocations.DescendantsAndSelf
        savedSet = SelectionSet(s)
        savedSet.DisplayName = wk
        yearFolder.Children.Add(savedSet)
    savedFolder.Children.Add(yearFolder)

doc.SelectionSets.InsertCopy(nextIndex, savedFolder)


