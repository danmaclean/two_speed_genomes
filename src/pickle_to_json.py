import pickle
import json
import sys

#reads in names of pickle files, combines them into one object by adding
#adding a key of the filename and dumps JSON of the whole thing
all = {}
for f in sys.stdin:
	sys.stderr.write(f)
	f = f.rstrip()
	all[f.replace("/", "_")] = pickle.load( open( f, "rb" ) )
	
print json.dumps(all)
