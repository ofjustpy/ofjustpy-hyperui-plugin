from .component_builder import build_all_components

component_database = {}

for cat_title, component_pyds, fn_comp_map in build_all_components("Alerts"):
    print("-----------------------------")
    print (fn_comp_map['1.html'])
    component_database[cat_title] = []
    for fn in fn_comp_map.keys():
        cid = fn[0:-5]
        is_dark = False
        if 'dark' in cid:
            cid = cid.replace('-dark', "")
            is_dark = True
        # mdd metadata dict
        cmd = None
        for mdd in component_pyds:
            if mdd['id'] == int(cid):
                cmd = mdd
                break
        
        assert cmd is not None

        print(f"For comp {fn} the title is ", cmd["title"], is_dark)
        comp_db_entry =  {'title': cmd["title"],
                                  'is_dark': is_dark,
                                  'the_gen': fn_comp_map[fn],
                                  }
        
        print(comp_db_entry)
        
        
        component_database[cat_title].append(comp_db_entry)

    break

def get_component(cat_title, comp_title, is_dark, **comp_kwargs):
    assert cat_title in component_database
    comp_db = None
    for comp_db in component_database[cat_title]:
        if comp_title in comp_db['title']:
            break

    assert comp_db is not None
    the_comp, updaters = comp_db['the_gen']()
    for kw, kv in comp_kwargs:
        print("updating component", kw)
        assert 'kw' in comp_kwargs
        updaters['kw'](kv)
        

# [{'id': 1, 'title': 'Popup', 'dark': True}, {'id': 2, 'title': 'Popup with Actions', 'dark': True}, {'id': 3, 'title': 'Content', 'dark': True}, {'id': 4, 'title': 'Content with Icon', 'dark': True}



