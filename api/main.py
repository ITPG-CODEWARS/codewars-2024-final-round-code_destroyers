from init import *
import api

def main():
    config = loadConfig()
    api.app.run(debug=True)

if __name__ == '__main__':
    main()