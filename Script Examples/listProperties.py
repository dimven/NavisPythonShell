from npw import doc, selection

if selection.Count > 0:
    mi = selection[0]
    for pc in mi.PropertyCategories:
        print('\n')
        print('Property Category: {} ({})'.format(pc.DisplayName, pc.Name))
        for dp in pc.Properties:
            if dp.Value.IsDisplayString:
                value = dp.Value.ToString()
            elif dp.Value.IsDateTime:
                value = dp.Value.ToDateTime().ToShortTimeString()
            else:
                value = dp.Value.ToString()

            print('\t{} ({}): {}'.format(dp.DisplayName, dp.Name, value))
