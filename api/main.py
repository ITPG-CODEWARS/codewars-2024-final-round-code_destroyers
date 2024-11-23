from init import *
import api

def main():
    config = loadConfig()
    print(config)
    api.main()
    

if __name__ == '__main__':
    main()