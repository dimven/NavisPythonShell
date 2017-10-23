from npw import doc, selection

if selection.Count > 0:
    mi = selection[0]
    for pc in mi.PropertyCategories:
        print('\n')
        print('Display Name: {}  Internal Name: {}'.format(pc.DisplayName, pc.Name))
        print('\tProperties')
        for dp in pc.Properties:
            print('\tDisplay Name: {}  Internal Name: {}'.format(dp.DisplayName, dp.Name))
            if dp.Value.IsDisplayString:
                print('\t\t[Value]: {}'.format(dp.Value.ToString()))
            elif dp.Value.IsDateTime:
                print('\t\t[Value]: {}'.format(dp.Value.ToDateTime().ToShortTimeString()))
            else:
                print('\t\t[Value]: {}'.format(dp.Value.ToString()))
