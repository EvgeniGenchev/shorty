import os
import json
import getpass
import keyboard

def run_program(full_path):
    name = full_path.split("\\")[-1]
    path = full_path[:len(full_path)-len(name)]
    
    os.chdir(path)
    os.system(name)

def get_config():
    user_dir = f"C:\\Users\\{getpass.getuser()}"
    config_dir = f"{user_dir}\\.shorty"
    
    try:
        config = {}
        with open(f"{config_dir}\\config.json", "r") as sett:
            for s in json.load(sett)['shortcuts']:
                config[s["shortcut"]] = s["destination"]
        return config
    except:
        os.mkdir(config_dir)
        os.chdir(config_dir)
        with open("config.json", "w") as f:
            default = """{
    "shortcuts": [
        {
	"shortcut": "win+enter",
	"destination": "D:\\\\wt"
	}

    ]
}
"""
            f.write(default)
        return get_config()
        

config = get_config()

print(config)
for k in config:
    keyboard.add_hotkey(k, run_program, args=(config[k],))

keyboard.wait()



