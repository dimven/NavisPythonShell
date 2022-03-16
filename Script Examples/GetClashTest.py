testdata = docclash.TestsData
tests = testdata.Tests
for test in tests:
	SavedItemCollection = test.Children
	for saveitem in SavedItemCollection:
		print(saveitem.DisplayName)
		print(saveitem.Center)