import os
import json

config = {
    "host": "",
    "port": 69420
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
        

if __name__ == "__main__":
    from main import main
    main()