import json
with open("civgraph.json", "r") as f:
    civ = json.load(f)
    with open("Makefile", "w") as fout:
        fout.write(".PHONY: clean\n")
        for key in civ.keys():
            fout.write(key + ': ' + ' '.join(civ[key]) + "\n\t@echo \"" + key + "\"\n" + "\t@echo . > " + key +\
                       "\n")
        fout.write("clean: \n\t@del ")
        for key in civ.keys():
            fout.write(key + ' ')
