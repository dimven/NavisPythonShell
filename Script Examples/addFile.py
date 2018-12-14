#doc = Application.ActiveDocument #this is already defined in the init script
path1 = r"path-to-your-file"

try:
    with doc.BeginTransaction("test") as t1:
        doc.AppendFile(path1)
        t1.Commit()
        print "%s appended successfully" % path1
except Exception, ex:
    print str(ex)
