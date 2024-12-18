import os
import json

config = {
    "host": "192.168.22.163",
    "port": 5000,
    "database": {
        "db_name": "database",
        "hostname": "localhost",
        "port": 27017
    },
	"uuid_length": 12
}

# Initialize the config file
def loadConfig():
    if os.path.exists("./config.json"):
        d = json.loads(open("./config.json").read())
        for i in d: config[i] = d[i]
        with open("./config.json", "w") as f:
            json.dump(config, f, indent="\t")
    else:
        openfile=open("./config.json", "w")
        d = {}
        for i in d: config[i] = d[i]
        openfile.write(json.dumps(config, indent="\t"))
        openfile.close()
        
    return config
        

if __name__ == "__main__":
    from main import main
    main()