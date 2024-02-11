import sys, requests, time, shutil, os, yaml
from zipfile import ZipFile
from datetime import datetime


def main():
    try:
        time.sleep(3)
        print("Download...")

        url = sys.argv[1]
        # download zip
        r = requests.get(url)
        if r.status_code != 200:
            print("Failed to download zip; status code:", r.status_code)
            return
        with open("update.zip", "wb") as f:
            f.write(r.content)

        print("Extract...")

        # extract zip to update_tmp folder
        with ZipFile("update.zip", "r") as zip_ref:
            zip_ref.extractall("update_tmp")
        
        print("Move files...")
        
        # copy files in "db" (except "master.db") to "update_tmp/_internal/db"
        for fname in os.listdir("_internal/db"):
            if fname != "master.db":
                shutil.copy(f"_internal/db/{fname}", f"update_tmp/_internal/db/{fname}")
        
        # remove _internal folder
        shutil.rmtree("_internal")
        
        # move all folder and files in update_tmp to . (except ../update.exe)
        for fname in os.listdir("update_tmp"):
            if fname != "update.exe":
                shutil.move(f"update_tmp/{fname}", f"{fname}")
        
        # remove update_tmp and update.zip
        shutil.rmtree("update_tmp")
        os.remove("update.zip")

        print("Update complete")

        if os.path.exists("_internal/db/config.yaml"):
            with open('_internal/db/config.yaml', 'r') as f:
                config = yaml.load(f, Loader=yaml.FullLoader)

            config["last_version_check"] = datetime.now()
            with open('_internal/db/config.yaml', 'w') as f:
                yaml.dump(config, f)

        # exit current process and run Trickcal Manager.exe
        os.startfile("Trickcal Manager.exe")
    
    except Exception as e:
        print("Error:", e)
        input("Press Enter to exit")


if __name__ == "__main__":
    main()