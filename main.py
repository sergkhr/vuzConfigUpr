import json
with open("civgraph.json", "r") as f:
    civ = json.load(f)
    with open("Makefile", "w") as fout:
        for key in civ.keys():
            fout.write(key + ': ' + ' '.join(civ[key]) + "\n\t@echo \"" + key + "\"\n" + "\t@echo . > " + key +\
                       "\n")
