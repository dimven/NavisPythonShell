root = doc.Models[0].RootItem

total = 0

def getTotal(x):
	if x.DisplayName == "Body":
		return 1
	return sum(map(getTotal, x.Children))

for c in root.Children:
	t = getTotal(c)
	total += t
	print c.DisplayName, " | ", t

print "Total items: ", total
