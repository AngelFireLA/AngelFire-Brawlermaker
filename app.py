import csv
import os
import platform
import random
import shutil
import sys
import time
import tkinter
import tkinter as tk
from tkinter import filedialog, ttk
from zipfile import ZipFile

import pandas as pd
import requests
from PIL import Image, ImageTk
from mega import Mega
from pandas import DataFrame


def is_windows():
    return platform.system().lower() == 'windows'


class Brawler:
    def __init__(self, brawlername="AngelFire", description="I'm the creator of AngelFire's Brawler Maker !", rarity="rare",
                 attack_name="attack name", attack_description="attack description", ulti_name="Ulti name",
                 ulti_description="Ulti description", speed="720", hp="4000", icon="shelly", scale="116", range="20",
                 reloadtime="1000", ammonumber="3",
                 damage="1000", spread="0", numberofprojectiles="1", projectile="shelly", timebetweenattacks="100",
                 attackduration="150",
                 chosen_projectile="ShotGunGirl"):
        self.brawlername = brawlername
        self.capbrawlername = brawlername.upper()
        self.description = description
        self.rarity = rarity
        self.attack_name = attack_name
        self.attack_description = attack_description
        self.ulti_name = ulti_name
        self.ulti_description = ulti_description
        self.speed = speed
        self.hp = hp
        self.icon = icon
        self.scale = scale
        self.range = range
        self.reloadtime = reloadtime
        self.ammonumber = ammonumber
        self.damage = damage
        self.spread = spread
        self.numberofprojectiles = numberofprojectiles
        self.projectile = projectile
        self.timebetweenattacks = timebetweenattacks
        self.attackduration = attackduration
        self.chosen_projectile = chosen_projectile

    def __str__(self):
        return (f"Name: {self.brawlername}\n"
                f"Description: {self.description}\n"
                f"Rarity: {self.rarity}\n"
                f"Attack Name: {self.attack_name}\n"
                f"Attack Description: {self.attack_description}\n"
                f"Ultimate Name: {self.ulti_name}\n"
                f"Ultimate Description: {self.ulti_description}\n"
                f"Speed: {self.speed}\n"
                f"HP: {self.hp}\n"
                f"Icon: {self.icon}\n"
                f"Scale: {self.scale}\n"
                f"Range: {self.range}\n"
                f"Reload Time: {self.reloadtime}\n"
                f"Ammo Number: {self.ammonumber}\n"
                f"Damage: {self.damage}\n"
                f"Spread: {self.spread}\n"
                f"Number of Projectiles: {self.numberofprojectiles}\n"
                f"Projectile: {self.projectile}\n"
                f"Time Between Attacks: {self.timebetweenattacks}\n"
                f"Attack Duration: {self.attackduration}\n"
                f"Chosen Projectile: {self.chosen_projectile}")

    def __repr__(self):
        return self.__str__()


def my_path(path_name):
    """Return the appropriate path for data files based on execution context"""
    if getattr(sys, 'frozen', False):
        # running in a bundle
        return os.path.join(sys._MEIPASS, path_name)
    else:
        # running live
        return path_name


mega = Mega()

taskbar_height = 0
if is_windows():
    from win32api import GetMonitorInfo, MonitorFromPoint

    monitor_info = GetMonitorInfo(MonitorFromPoint((0, 0)))
    monitor_area = monitor_info.get("Monitor")
    work_area = monitor_info.get("Work")
    taskbar_height = monitor_area[3] - work_area[3]

root = tk.Tk()
root.state('zoomed')
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight() - taskbar_height}+0+0")
root.title("AngelFire's Brawler Maker")
height -= taskbar_height

csv_logic_path = ""
csv_localization_path = ""
current_path = os.path.abspath(os.getcwd())

default_apk_link = 'https://mega.nz/file/cANAhBya#8wFHevhnng_a09IMWPet9BihJaJd3nLDHaEhGqgmIM4'
default_apk = 'BrawlStarsOfflinev29'

brawler = Brawler()

chosen_option = 0

projectiles_dict = {
    "shelly main attack": "ShotgunGirlProjectile",
    "colt main attack": "GunslingerProjectile",
    "bull main attack": "BullDudeProjectile",
    "brock main attack": "RocketGirlProjectile",
    "rico main attack": "TrickshotDudeProjectile",
    "spike main attack": "CactusProjectile",
    "barley main attack": "BarkeepProjectile",
    "jessie main attack": "MechanicProjectile1",
    "nita main attack": "ShamanProjectile",
    "dynamike main attack": "TntDudeProjectile",
    "el_primo main attack": "PrimoDefProjectile",
    "crow main attack": "CrowProjectile",
    "poco main attack": "DeadMariachiProjectile",
    "bo main attack": "BowDudeProjectile",
    "piper main attack": "SniperProjectile",
    "pam main attack": "MinigunDudeProjectile",
    "tara main attack": "BlackHoleProjectile",
    "darryl main attack": "BarrelBotProjectile",
    "penny main attack": "ArtilleryDudeProjectile",
    "frank main attack": "HammerDudeProjectile",
    "gene main attack": "HookProjectile",
    "tick main attack": "ClusterBombProjectile",
    "leon main attack": "LeonDefProjectile",
    "rosa main attack": "RosaProjectile",
    "carl main attack": "WhirlwindProjectile",
    "eight_bit main attack": "ArcadeProjectile",
    "sandy main attack": "SandstormProjectile",
    "bea main attack": "BeeSniperProjectile",
    "emz main attack": "MummyProjectile",
    "mister_p main attack": "SpawnerDudeProjectile",
    "max main attack": "SpeedyProjectile",
    "gale main attack": "BlowerProjectile",
    "nani main attack": "ControllerProjectile",
    "sprout main attack": "WallyProjectile",
    "surge main attack": "PowerLevelerProjectile",
    "colette main attack": "PercenterProjectile",
    "shelly super": "ShotgunGirlUltiProjectile",
    "colt super": "GunslingerUltiProjectile",
    "brock super": "RocketGirlUltiProjectile",
    "rico super": "TrickshotDudeUltiProjectile",
    "spike super": "CactusUltiProjectile",
    "barley super": "BarkeepUltiProjectile",
    "dynamike super": "TntDudeUltiProjectile",
    "mortis super": "UndertakerUltiProjectile",
    "poco super": "DeadMariachiUltiProjectile",
    "tara super": "BlackHoleUltiProjectile",
    "frank super": "HammerDudeUltiProjectile",
    "gene super": "HookDudeProjectile",
    "bibi super": "BaseballUltiProjectile",
    "sandy super": "SandstormUltiProjectile",
    "bea super": "BeeSniperUltiProjectile",
    "gale super": "BlowerUltiProjectile",
    "nani super": "ControllerUltiProjectile",
    "sprout super": "WallyUltiProjectile",
}

brawler_names_list = {'shelly': 'shelly', 'colt': 'colt', 'bull': 'bull', 'brock': 'brock', 'rico': 'rick',
                      'spike': 'spike', 'barley': 'barley', 'jessie': 'jess', 'nita': 'nita', 'dynamike': 'mike',
                      'el_primo': 'primo', 'mortis': 'mortis', 'crow': 'crow', 'poco': 'poco', 'bo': 'bo',
                      'piper': 'piper', 'pam': 'mj', 'tara': 'taro', 'darryl': 'barrel_bot', 'penny': 'penny',
                      'frank': 'frank', 'gene': 'gene', 'tick': 'tick', 'leon': 'leon', 'rosa': 'rosa', 'carl': 'carl',
                      'bibi': 'bibi', 'eight_bit': '8bit', 'sandy': 'sandy', 'bea': 'bea', 'emz': 'emz',
                      'mister_p': 'mrp', 'max': 'max', 'jacky': 'jacky', 'gale': 'gale', 'nani': 'nani',
                      'sprout': 'sprout', 'surge': 'surge', 'colette': 'colette'}


def start_button():
    startButton.place_forget()
    apk_or_csv__csv.place(x=width / 1.5, y=height / 2, anchor=tk.CENTER)
    apk_or_csv__csv.config(command=lambda: get_csv_manually())
    apk_or_csv__apk.place(x=width / 3, y=height / 2, anchor=tk.CENTER)
    apk_or_csv__apk.config(command=lambda: get_csv_from_apk())
    background_label.configure(image=background)


def get_csv_from_apk():
    apk_or_csv__csv.place_forget()
    apk_or_csv__apk.place_forget()
    normal_brawlers__apk.place(x=width / 2, y=height / 2)
    normal_brawlers__apk.config(command=lambda: result_is_automatic())
    startButtonManual.pack()
    startButtonManual.place(x=width / 2, y=height / 1.5, anchor=tk.CENTER)
    startButtonManual.config(command=lambda: result_is_automatic_with_manual_apk())
    ProgramStoppedResponding.place(x=width / 1.93, y=height / 4.5, anchor=tk.CENTER)


def result_is_automatic():
    global chosen_option
    chosen_option = 3
    global csv_logic_path
    global csv_localization_path
    ProgramStoppedResponding.place_forget()
    normal_brawlers__apk.place_forget()
    startButtonManual.place_forget()
    if not os.path.exists(os.path.join(current_path, default_apk + ".apk")) and not os.path.exists(
            os.path.join(current_path, default_apk + ".zip")):
        try:
            print("Starting to download base APK")
            mega.download_url(default_apk_link, dest_filename=f"{default_apk}.zip",
                              dest_path=current_path)
            print("Finished downloading base APK")
        except PermissionError:
            pass

    if os.path.exists(os.path.join(current_path, default_apk + "/assets/csv_logic")):
        shutil.rmtree(os.path.join(current_path, default_apk))
        print("Found and removed existing base folder")
    print("Starting to extract base zip file")
    with ZipFile(default_apk + ".zip", 'r') as zipp:
        zipp.extractall(os.path.join(current_path, default_apk))
        csv_logic_path = os.path.join(default_apk, "assets/csv_logic")
        csv_localization_path = os.path.join(default_apk, "assets/localization")
        print("Finished extracting base zip file")
        set_brawler_texts_csv_1()


def create_backup(file_path, move=False):
    print("Starting to backup", file_path)
    backup_folder = os.path.join(current_path, "backup")
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    base_name = os.path.basename(file_path)
    backup_path = os.path.join(backup_folder, base_name)

    # Handle file name collision in the backup folder
    if os.path.exists(backup_path):
        base, ext = os.path.splitext(base_name)
        counter = 1
        while os.path.exists(backup_path):
            backup_path = os.path.join(backup_folder, f"{base}_{counter}{ext}")
            counter += 1
    if move:
        shutil.move(file_path, backup_path)
    else:
        shutil.copy(file_path, backup_path)
    print("Finished backing up", file_path)

def result_is_automatic_with_manual_apk():
    global chosen_option
    chosen_option = 3
    global csv_logic_path
    global csv_localization_path
    ProgramStoppedResponding.place_forget()
    normal_brawlers__apk.place_forget()
    startButtonManual.place_forget()

    apk_path = os.path.join(current_path, f"{default_apk}.apk").replace("\\", "/")
    zip_path = os.path.join(current_path, f"{default_apk}.zip").replace("\\", "/")

    file_path = filedialog.askopenfilename(filetypes=[("APK/ZIP files", "*.apk *.zip")])

    if not file_path:
        print("No file was selected (please restart AngelFire's Brawler Maker")
        return

    if file_path == zip_path:
        print("Selected File already exists in folder and has the base zip name, just making a backup in case.")
        create_backup(file_path)
    elif file_path == apk_path:
        print("Selected File already exists in folder and has the base APK name, just making a backup in case.")
        create_backup(file_path)
        if os.path.exists(zip_path):
            print("Base zip file already exists, making a backup aswell")
            create_backup(zip_path, move=True)
        shutil.copy(file_path, zip_path)
    else:
        if file_path.startswith(current_path):
            print("Selected file already exists in the folder with a custom name, just making a backup in case.")
            create_backup(file_path)
        if os.path.exists(zip_path) and file_path.endswith(".zip"):
            print("Base zip file exists and the selected file is a zip, making a backup and copying the file.")
            create_backup(zip_path, move=True)
            shutil.copy(file_path, zip_path)
        if os.path.exists(apk_path):
            print("Base APK file already exists, making a backup.")
            create_backup(apk_path, move=True)
        if file_path.endswith(".apk"):
            if os.path.exists(zip_path):
                print("Deleting existing zip file to replace it with the selected APK.")
                os.remove(zip_path)
            print("Copying selected APK file to zip path.")
            shutil.copy(file_path, zip_path)

    if os.path.exists(os.path.join(current_path, default_apk, "assets/csv_logic")):
        shutil.rmtree(os.path.join(current_path, default_apk))
        print("removed old folder")
    print("Starting to extract base zip file")
    with ZipFile(zip_path, 'r') as zipp:
        zipp.extractall(os.path.join(current_path, default_apk))
        csv_logic_path = os.path.join(default_apk, "assets/csv_logic")
        csv_localization_path = os.path.join(default_apk, "assets/localization")
        print("Finished extracting base zip file")
        set_brawler_texts_csv_1()

def get_csv_manually():
    global chosen_option
    chosen_option = 1
    apk_or_csv__csv.place_forget()
    apk_or_csv__apk.place_forget()
    openFolder.pack()
    openFolder.place(x=width / 2, y=height / 2, anchor=tk.CENTER)


def csv_logic_path_selector():
    global csv_logic_path
    csv_logic_path = filedialog.askdirectory(
        title="Select Csv Logic Folder")
    if "csv_logic" in csv_logic_path:
        if os.path.join(current_path, "csv_logic") != csv_logic_path.replace('/', "\\"):
            print(os.path.join(current_path, "csv_logic"), csv_logic_path)
            if os.path.exists(os.path.join(current_path, "csv_logic")):
                shutil.rmtree(os.path.join(current_path, "csv_logic"))
                print("Deleted csv logic folder")
            shutil.copytree(csv_logic_path, os.path.join(current_path, "csv_logic"))
            print("copied csv logic folder")
        openFolder.place_forget()
        openLocalization.place(x=width / 2, y=height / 2, anchor=tk.CENTER)
        openLocalization.config(command=lambda: csv_localization_pack_selector())


def csv_localization_pack_selector():
    global csv_localization_path
    csv_localization_path = filedialog.askdirectory(
        title="Select Localization Folder")
    if "localization" in csv_localization_path:
        if os.path.join(current_path, "localization") != csv_localization_path.replace('/', "\\"):
            if os.path.exists(os.path.join(current_path, "localization")):
                shutil.rmtree(os.path.join(current_path, "localization"))
                print("Deleted localization folder")
            shutil.copytree(csv_localization_path, os.path.join(current_path, "localization"))
            print("copied localization folder")
        openLocalization.place_forget()
        set_brawler_texts_csv_1()


def hide_and_clear_texts():
    text_entry1.place_forget()
    text_entry2.place_forget()
    text_entry3.place_forget()
    text_entry4.place_forget()
    text_entry5.place_forget()
    text_entry6.place_forget()
    text_entry7.place_forget()
    text_entry8.place_forget()
    text_entry9.place_forget()

    text_entry1.delete(0, tkinter.END)
    text_entry2.delete(0, tkinter.END)
    text_entry3.delete(0, tkinter.END)
    text_entry4.delete(0, tkinter.END)
    text_entry5.delete(0, tkinter.END)
    text_entry6.delete(0, tkinter.END)
    text_entry7.delete(0, tkinter.END)
    text_entry8.delete(0, tkinter.END)
    text_entry9.delete(0, tkinter.END)
    projectiles_dropdown.place_forget()
    projectiles_dropdown.current(0)
    icons_dropdown.place_forget()
    icons_dropdown.current(0)
    model_dropdown.current(0)
    skin_dropdown.current(0)
    skinDropdownLabel.place_forget()
    modelDropdownLabel.place_forget()
    skin_dropdown.place_forget()
    model_dropdown.place_forget()


def set_brawler_texts_csv_1():
    text_entry1.place(x=width / 19.2, y=height / 5.16)
    text_entry2.place(x=width / 1.92, y=height / 5.4)
    text_entry3.place(x=width / 19.2, y=height / 2.16)
    text_entry4.place(x=width / 19.2, y=height / 1.54)
    text_entry5.place(x=width / 1.92, y=height / 2.16)
    text_entry6.place(x=width / 1.92, y=height / 1.54)

    brawlerNameButton.place(x=width / 19.2, y=height / 4)
    brawlerDescriptionButton.place(x=width / 1.92, y=height / 4)
    brawlerAttackName.place(x=width / 19.2, y=height / 1.96)
    brawlerAttackDescription.place(x=width / 19.2, y=height / 1.44)
    brawlerUltiName.place(x=width / 1.92, y=height / 1.96)
    brawlerUltiDescription.place(x=width / 1.92, y=height / 1.44)

    confirmTextsButton.config(command=lambda: set_brawler_texts_csv_2())
    confirmTextsButton.place(x=width / 2.25, y=height / 1.24, anchor=tk.CENTER)


def set_brawler_texts_csv_2():
    brawler.brawlername = text_entry1.get()
    brawler.description = text_entry2.get()
    brawler.attack_name = text_entry3.get()
    brawler.attack_description = text_entry4.get()
    brawler.ulti_name = text_entry5.get()
    brawler.ulti_description = text_entry6.get()
    brawler.capbrawlername = brawler.brawlername.upper()
    # Define the path to the localization folder
    localization_folder_path = os.path.join(current_path, csv_localization_path)
    print("Starting to add texts to language files...")
    # Loop through each file in the localization folder
    for filename in os.listdir(localization_folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(localization_folder_path, filename)
            with open(file_path, 'a', newline="") as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(['TID_' + brawler.capbrawlername, brawler.brawlername])
                csv_writer.writerow(['TID_' + brawler.capbrawlername + '_DESC', brawler.description])
                csv_writer.writerow(
                    ['TID_' + brawler.capbrawlername + '_SHORT_DESC', "Made with AngelFire's Brawler Maker"])
                csv_writer.writerow(['TID_' + brawler.capbrawlername + '_WEAPON', brawler.attack_name])
                csv_writer.writerow(['TID_' + brawler.capbrawlername + '_WEAPON_DESC', brawler.attack_description])
                csv_writer.writerow(['TID_' + brawler.capbrawlername + '_ULTI', brawler.ulti_name])
                csv_writer.writerow(['TID_' + brawler.capbrawlername + '_ULTI_DESC', brawler.ulti_description])
    print("Done adding texts to language files")
    hide_and_clear_texts()
    confirmTextsButton.place_forget()
    brawlerNameButton.place_forget()
    brawlerDescriptionButton.place_forget()
    brawlerAttackName.place_forget()
    brawlerAttackDescription.place_forget()
    brawlerUltiName.place_forget()
    brawlerUltiDescription.place_forget()

    background_label.configure(image=rarity_image)

    brawlerRarityCommon.place(x=width / 6.4, y=height / 7.2)
    brawlerRarityCommon.config(command=lambda: set_brawler_cards_csv("common"))

    brawlerRarityRare.place(x=width / 6.4, y=height / 1.96)
    brawlerRarityRare.config(command=lambda: set_brawler_cards_csv("rare"))

    brawlerRaritySuperRare.place(x=width / 2.4, y=height / 1.96)
    brawlerRaritySuperRare.config(command=lambda: set_brawler_cards_csv("super_rare"))

    brawlerRarityEpic.place(x=width / 1.47, y=height / 1.96)
    brawlerRarityEpic.config(command=lambda: set_brawler_cards_csv("epic"))

    brawlerRarityMythic.place(x=width / 2.4, y=height / 7.2)
    brawlerRarityMythic.config(command=lambda: set_brawler_cards_csv("mega_epic"))

    brawlerRarityLegendary.place(x=width / 1.47, y=height / 7.2)
    brawlerRarityLegendary.config(command=lambda: set_brawler_cards_csv("legendary"))


def set_brawler_cards_csv(rarity):
    print("Chosen rarity is ", rarity)
    background_label.configure(image=background)
    brawlerRarityRare.place_forget()
    brawlerRaritySuperRare.place_forget()
    brawlerRarityEpic.place_forget()
    brawlerRarityMythic.place_forget()
    brawlerRarityLegendary.place_forget()
    brawlerRarityCommon.place_forget()
    brawlernumber = random.randint(1000, 1999)
    print("Starting to add content to cards.csv ...")
    filename = os.path.join(os.path.join(current_path, csv_logic_path), 'cards.csv')
    with open(filename, 'a', newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(
            [brawler.brawlername + '_unlock', 'sc/ui.sc', '', brawler.brawlername, '', '', '0', '', 'unlock', '', '',
             '', '', rarity,
             '', '', '', '', '', '', brawlernumber, ''])
        csv_writer.writerow(
            [brawler.brawlername + '_hp', 'sc/ui.sc', 'health_icon', brawler.brawlername, '', '', '1', '', 'hp', '', '',
             '', '',
             'common', 'TID_ARMOR', 'TID_ARMOR', '', '', 'genicon_health', '', '', ''])
        csv_writer.writerow(
            [brawler.brawlername + '_abi', 'sc/ui.sc', 'attack_icon', brawler.brawlername, '', '', '2', '', 'skill',
             brawler.brawlername + 'Weapon', '', '', '', 'common', 'TID_' + brawler.capbrawlername + '_WEAPON',
             'TID_STAT_DAMAGE', '', '', 'genicon_damage', '', '', ''])
        csv_writer.writerow(
            [brawler.brawlername + '_ulti', 'sc/ui.sc', 'ulti_icon', brawler.brawlername, '', '', '3', '', 'skill',
             brawler.brawlername + 'Ulti', '', '', '', 'common', 'TID_' + brawler.capbrawlername + '_ULTI',
             'TID_STAT_DAMAGE', '', '', 'genicon_damage', '', '', ''])
    print("Done adding content to cards.csv")
    set_brawler_characters_csv_1()


def get_skins_combo() -> dict:
    filename = os.path.join(current_path, csv_logic_path, 'skins.csv')
    # Use pandas to read the CSV file
    df = pd.read_csv(filename, skiprows=lambda x: x == 1)

    data_dict = {}

    for index, row in df.iterrows():
        key = row.iloc[0]

        values = [x.strip() for x in row.iloc[15:19].astype(str).tolist()]
        for value in values:
            while value[0] == ' ':
                value = value[1:]
            while value[-1] == ' ':
                value = value[:-1]
        if isinstance(key, float):
            print("ERROR (please report this to @angelfirela) this shouldn't be a float :", key)
        data_dict[
            str(key)] = f',,,,,,,,,,,,,"{values[0].strip()}","{values[1].strip()}","{values[2].strip()}","{values[3].strip()}",'

    return data_dict


def prepare_skin_confs_line(chosen_skin, brawler_name) -> str:
    filename = os.path.join(current_path, csv_logic_path, 'skin_confs.csv')
    df = pd.read_csv(filename)
    print(chosen_skin)
    base_line = df[df['Name'] == chosen_skin].iloc[0]  # Replace 'FirstColumnName' with the actual column name
    new_line: DataFrame = base_line.copy()
    new_line['Name'] = brawler_name + "Default"  # Adjust column name as needed
    new_line['Character'] = brawler_name  # Adjust column name as needed
    columns_to_clear = ['MainAttackProjectile', 'SecondaryProjectile', 'UltiProjectile', 'AutoAttackProjectile',
                        'ProjectileForShockyStarPower', 'IncendiaryStarPowerAreaEffect']
    for col in columns_to_clear:
        new_line[col] = ''  # Set to empty

    new_line_str = new_line.fillna('').astype(str).values.tolist()  # Fill NaN with empty strings and convert to list
    csv_line = ','.join(new_line_str)  # Join the list into a comma-separated string
    return csv_line


def set_brawler_characters_csv_1():
    all_skin_names = list(get_skins_combo().keys())
    skin_dropdown["values"] = ["Custom texture (select file after continuing)"] + sorted(all_skin_names)
    skin_dropdown.current(0)
    model_dropdown["values"] = sorted(all_skin_names)

    hide_and_clear_texts()

    text_entry1.place(x=width / 19.2, y=height / 3.5)
    text_entry2.place(x=width / 1.92, y=height / 4)
    text_entry3.place(x=width / 19.2, y=height / 1.8)
    icons_dropdown.place(x=width / 19.2, y=height / 1.44)
    skin_dropdown.place(x=width / 1.92, y=height / 1.8)
    model_dropdown.place(x=width / 1.92, y=height / 1.44)

    brawlerSpeedButton.place(x=width / 19.2, y=height / 5)
    brawlerHealthButton.place(x=width / 1.92, y=height / 5)
    brawlerScaleButton.place(x=width / 19.2, y=height / 2.16)
    brawlerIconButton.place(x=width / 19.2, y=height / 1.54)
    skinDropdownLabel.place(x=width / 1.92, y=height / 2.06)
    modelDropdownLabel.place(x=width / 1.92, y=height / 1.54)

    confirmCharacterButton.place(x=width / 2.25, y=height / 1.24, anchor=tk.CENTER)
    confirmCharacterButton.config(command=lambda: set_brawler_characters_csv_2())


def set_brawler_characters_csv_2():
    speed = text_entry1.get()
    try:
        int(speed)
    except ValueError:
        speed = str(720)
    if int(speed) > 10000:
        speed = str(10000)

    hp = text_entry2.get()
    try:
        int(hp)
    except ValueError:
        hp = str(4000)
    if int(hp) > 30000:
        hp = str(30000)
    if int(hp) < 1:
        hp = str(1)

    scale = text_entry3.get()
    try:
        int(scale)
    except ValueError:
        scale = str(116)
    if int(scale) > 580:
        scale = str(580)

    icon = icons_dropdown.get()
    if icon.lower() not in list(brawler_names_list.keys()):
        icon = "shelly"
    icon = brawler_names_list[icon]
    ultichargemul = random.randint(90, 135)
    ultichargeultimul = random.randint(90, 150)
    print("Starting to add content to characters.csv ...")
    filename = os.path.join(os.path.join(current_path, csv_logic_path), 'characters.csv')
    with open(filename, 'a', newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([''])
        csv_writer.writerow(
            [brawler.brawlername, '', '', 'bull', brawler.brawlername + 'Weapon', brawler.brawlername + 'Ulti', '',
             speed, hp, '', '', '', '',
             '', '', '', '12', '', ultichargemul, ultichargeultimul, "Hero", '', brawler.brawlername + 'Default', '',
             '', '',
             '', '', '', 'takedamage_gen', 'death_shotgun_girl', 'Gen_move_fx', 'reload_shotgun_girl',
             'No_ammo_shotgungirl', 'Dry_fire_shotgungirl', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
             '', '', '30', '', '80', '80', '', '', '35', scale, '210', '284', '90', '175', '260', '', '', '', '-25',
             '40', '120', 'Medium', '-48', '', '450', '', '', 'TID_' + brawler.capbrawlername, '', 'sc/ui.sc',
             'hero_icon_' + icon, '0', 'human', 'footstep', '25', '250', '200', '', '', '1', '3', '2', '', '', '', '',
             '', '', '', '', '', 'ShellyTutorial', '', '', '', '', '', '3', '3', '3'])
    print("Done adding content to characters.csv")
    generate_brawler_skin_files(model_dropdown.get(), skin_dropdown.get())


def generate_brawler_skin_files(chosen_model, chosen_texture):
    skins_combo = get_skins_combo()
    filename = os.path.join(os.path.join(current_path, csv_logic_path), 'skins.csv')
    print("Starting to add content to skins.csv ...")
    with open(filename, 'a', newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([''])
        if chosen_texture == "Custom texture (select file after continuing)":
            # Specify the file types
            file_types = [
                ('PNG files', '*.png'),
                ('KTX files', '*.ktx'),
                ('PVR files', '*.pvr'),
            ]

            # Open the file dialog and ask the user to choose a file
            file_path = filedialog.askopenfilename(title="Select your brawler's texture file", filetypes=file_types)
            file_name = os.path.basename(file_path)
            file.write(
                brawler.brawlername + 'Default,' + brawler.brawlername + 'Default,' + f", , , , , , , , , , , , , {file_name}, {file_name},{file_name},{file_name}," + "\n")
            sc3d_path = default_apk + "/assets/sc3d"
            shutil.copy(file_path, sc3d_path)
        else:
            file.write(
                brawler.brawlername + 'Default,' + brawler.brawlername + 'Default,' + skins_combo[chosen_texture])
    print("Done adding content to skins.csv")
    print("Starting to add content to skin_confs.csv ...")
    filename = os.path.join(os.path.join(current_path, csv_logic_path), 'skin_confs.csv')
    with open(filename, 'a', newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([''])
        file.write(prepare_skin_confs_line(chosen_model, brawler.brawlername) + "\n")
    print("Done adding content to skin_confs.csv")
    set_brawler_skill_csv_attack_1()


def set_brawler_skill_csv_attack_1():
    hide_and_clear_texts()
    confirmCharacterButton.place_forget()
    brawlerSpeedButton.place_forget()
    brawlerHealthButton.place_forget()
    brawlerScaleButton.place_forget()
    brawlerIconButton.place_forget()

    text_entry1.place(x=width / 19.2, y=height / 3.8)
    projectiles_dropdown.place(x=width / 1.92, y=height / 4.32)
    text_entry5.place(x=width / 19.2, y=height / 1.7)
    text_entry6.place(x=width / 1.92, y=height / 1.37)
    text_entry7.place(x=width / 1.92, y=height / 1.85)
    text_entry8.place(x=width / 19.2, y=height / 1.3)
    text_entry9.place(x=width / 19.2, y=height / 2.25)

    brawlerAttackRange.place(x=width / 19.2, y=height / 5.4)
    brawlerAttackProjectile.place(x=width / 1.92, y=height / 5.4)
    brawlerAttackProjectileNumber.place(x=width / 19.2, y=height / 1.85)
    brawlerAttackDamage.place(x=width / 1.92, y=height / 1.54)
    brawlerAttackReloadTime.place(x=width / 1.92, y=height / 2.16)
    brawlerAttackAmmoNumber.place(x=width / 19.2, y=height / 1.45)
    brawlerAttackSpread.place(x=width / 19.2, y=height / 3)
    MainAttackLabel.place(x=width / 2, y=height / 10, anchor=tk.CENTER)
    NextButton.place(x=width / 2.25, y=height / 1.24, anchor=tk.CENTER)
    NextButton.config(command=lambda: set_brawler_skill_csv_attack_2())


def set_brawler_skill_csv_attack_2():
    brawler.range = text_entry1.get()
    try:
        brawler.chosen_projectile = projectiles_dict[projectiles_dropdown.get()]
    except KeyError:
        brawler.chosen_projectile = projectiles_dict["shelly main attack"]
    brawler.numberofprojectiles = text_entry5.get()
    try:
        int(brawler.numberofprojectiles)
    except ValueError:
        brawler.numberofprojectiles = str(1)
    if int(brawler.numberofprojectiles) > 20:
        brawler.numberofprojectiles = str(20)
    brawler.damage = text_entry6.get()
    try:
        int(brawler.damage)
    except ValueError:
        brawler.damage = str(1000)
    if int(brawler.damage) > 10000:
        brawler.damage = str(10000)
    brawler.reloadtime = text_entry7.get()
    try:
        int(brawler.reloadtime)
    except ValueError:
        brawler.reloadtime = str(1000)
    if int(brawler.reloadtime) > 4999:
        brawler.reloadtime = str(4999)
    if int(brawler.reloadtime) < 1:
        brawler.reloadtime = str(1)
    brawler.ammonumber = text_entry8.get()
    try:
        int(brawler.ammonumber)
    except ValueError:
        brawler.ammonumber = str(3)
    if int(brawler.ammonumber) > 4:
        brawler.ammonumber = str(4)
    if int(brawler.ammonumber) < 1:
        brawler.ammonumber = str(1)
    brawler.spread = text_entry9.get()
    try:
        int(brawler.spread)
    except ValueError:
        brawler.spread = str(0)
    if int(brawler.spread) > 359:
        brawler.spread = str(359)
    print("Starting to add basic attack to skills.csv ...")
    filename = os.path.join(os.path.join(current_path, csv_logic_path), 'skills.csv')
    with open(filename, 'a', newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([''])
        csv_writer.writerow(
            [brawler.brawlername + "Weapon", 'Attack', 'true', 'true', 'true', '', '50', brawler.attackduration, '',
             brawler.range, '', '',
             '', '', brawler.reloadtime, brawler.ammonumber, brawler.damage, '', brawler.timebetweenattacks,
             brawler.spread, '', brawler.numberofprojectiles, '',
             'true', '', '', '', '', '', '', '', '', brawler.chosen_projectile, '', '', '', '', '', '', '', '',
             'sc/ui.sc', 'rapid_fire_button', 'rico_def_atk', '', '', '', '', '', '', '', '', '', '', '', ''])
    print("Done adding basic attack to skills.csv")
    set_brawler_skill_csv_super_1()


def set_brawler_skill_csv_super_1():
    hide_and_clear_texts()
    MainAttackLabel.place_forget()
    NextButton.place_forget()
    brawlerAttackRange.place_forget()
    brawlerAttackAmmoNumber.place_forget()
    brawlerAttackDamage.place_forget()
    brawlerAttackProjectile.place_forget()
    brawlerAttackProjectileNumber.place_forget()
    brawlerAttackReloadTime.place_forget()
    brawlerAttackSpread.place_forget()

    text_entry1.place(x=width / 19.2, y=height / 3.8)
    projectiles_dropdown.place(x=width / 1.92, y=height / 4.32)
    text_entry5.place(x=width / 19.2, y=height / 1.7)
    text_entry6.place(x=width / 1.92, y=height / 1.37)
    text_entry9.place(x=width / 19.2, y=height / 2.25)

    brawlerSuperRange.place(x=width / 19.2, y=height / 5.4)
    brawlerSuperProjectile.place(x=width / 1.92, y=height / 5.4)
    brawlerSuperProjectileNumber.place(x=width / 19.2, y=height / 1.85)
    brawlerSuperDamage.place(x=width / 1.92, y=height / 1.54)
    brawlerSuperSpread.place(x=width / 19.2, y=height / 3)
    SuperLabel.place(x=width / 2, y=height / 10, anchor=tk.CENTER)
    NextButton.place(x=width / 2.25, y=height / 1.24, anchor=tk.CENTER)
    NextButton.config(command=lambda: set_brawler_skill_csv_super_2())


def set_brawler_skill_csv_super_2():
    brawler.range = text_entry1.get()

    try:
        brawler.chosen_projectile = projectiles_dict[projectiles_dropdown.get()]
    except KeyError:
        brawler.chosen_projectile = projectiles_dict["shelly main attack"]

    brawler.numberofprojectiles = text_entry5.get()
    try:
        int(brawler.numberofprojectiles)
    except ValueError:
        brawler.numberofprojectiles = str(1)
    if int(brawler.numberofprojectiles) > 20:
        brawler.numberofprojectiles = str(20)

    brawler.damage = text_entry6.get()
    try:
        int(brawler.damage)
    except ValueError:
        brawler.damage = str(1000)
    if int(brawler.damage) > 10000:
        brawler.damage = str(10000)

    brawler.spread = text_entry9.get()
    try:
        int(brawler.spread)
    except ValueError:
        brawler.spread = str(0)
    if int(brawler.spread) > 359:
        brawler.spread = str(359)
    filename = os.path.join(os.path.join(current_path, csv_logic_path), 'skills.csv')
    print("Starting to add super to skills.csv ...")
    with open(filename, 'a', newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([''])
        csv_writer.writerow(
            [brawler.brawlername + "Ulti", 'Attack', 'true', 'true', 'true', '', '50', brawler.attackduration, '',
             brawler.range, '', '',
             '', '', '', '', brawler.damage, '', brawler.timebetweenattacks, brawler.spread, '',
             brawler.numberofprojectiles, '',
             'true', '', '', '', '', '', '', '', '', brawler.chosen_projectile, '', '', '', '', '', '', '', '',
             'sc/ui.sc', 'rapid_fire_button', 'rico_def_atk', '', '', '', '', '', '', '', '', '', '', '', ''])
    print("Done adding super to skills.csv")
    hide_and_clear_texts()
    brawlerSuperRange.place_forget()
    brawlerSuperProjectile.place_forget()
    brawlerSuperProjectileNumber.place_forget()
    brawlerSuperDamage.place_forget()
    brawlerSuperSpread.place_forget()
    SuperLabel.place_forget()
    NextButton.place_forget()

    if chosen_option == 1:
        print("Done making brawler in manual mode.")
        background_label.configure(image=your_folder_is_ready)
    elif chosen_option == 3:
        if os.path.exists(os.path.join(current_path, default_apk + "-BrawlerMaker")):
            print("Removing old base folder ...")
            shutil.rmtree(os.path.join(current_path, default_apk + "-BrawlerMaker"))
            print("Done removing old base folder.")

        print("Starting to compress base folder into apk ...")
        renamed = False
        while not renamed:
            try:
                os.rename(default_apk, default_apk + "-BrawlerMaker")
                renamed = True
            except PermissionError:
                time.sleep(0.5)

        if os.path.exists(os.path.join(current_path, default_apk + "-BrawlerMaker" + ".zip")):
            os.remove(os.path.join(current_path, default_apk + "-BrawlerMaker" + ".zip"))

        if os.path.exists(os.path.join(current_path, default_apk + "-BrawlerMaker" + ".apk")):
            os.remove(os.path.join(current_path, default_apk + "-BrawlerMaker" + ".apk"))

        shutil.make_archive(default_apk + "-BrawlerMaker", "zip",
                            os.path.join(current_path, default_apk + "-BrawlerMaker"))

        os.rename(os.path.join(current_path, default_apk + "-BrawlerMaker" + ".zip"),
                  default_apk.replace(' ', '-') + "-BrawlerMaker" + ".apk")
        print("Done compressing base folder into apk.")
        print("Starting to sign apk ...")
        signed = False
        try:
            os.system('java -jar ' + my_path("uber-apk-signer.jar") + ' -a "' + current_path + "/" + default_apk + '-BrawlerMaker' + '.apk"')
            signed = True
        except Exception as e:
            print(e)
            print("Error while signing apk, you may have to sign apk with APK editor.")

        try:
            target_file = os.path.join(current_path, "BrawlStarsOfflinev29-AngelFire's BrawlerMaker.apk")
            # Check if the target file already exists
            if os.path.exists(target_file):
                print("Old completed APK already exists, making a backup...")
                create_backup(target_file, move=True)  # Remove the existing file
            print("Done making backup.")
            print("Renaming APK into final form...")
            if signed:
                # Rename the file
                os.rename(
                    os.path.join(current_path, "BrawlStarsOfflinev29-BrawlerMaker-aligned-debugSigned.apk"),
                    target_file
                )
            else:
                os.rename(
                    os.path.join(current_path, "BrawlStarsOfflinev29-BrawlerMaker.apk"),
                    target_file
                )
            print("Done renaming APK.")

            print("Deleting old APK ...")
            # If renaming is successful, delete the old file
            os.remove(os.path.join(current_path, "BrawlStarsOfflinev29-BrawlerMaker.apk"))
            print("Done deleting old APK.")
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please use the apk ending with 'debug-aligned' instead.")
        send_message_to_webhook()
        background_label.configure(image=your_folder_is_ready)
        print("Done making brawler in automatic mode !")


def send_message_to_webhook():
    try:
        webhook_url = 'https://discord.com/api/webhooks/1267146970066059315/Nz9e2NUqTGFYJ5qJEPoPgAzao_bjwiH370AZXNEA9jDMG-J02feIoFgN3I4fqL8AVGaC'
        message = {
            "content": f"Someone used AngelFire's Brawler Maker \n {str(brawler)}"
        }

        requests.post(webhook_url, json=message)
    except:
        pass


canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

background = Image.open(my_path("BG.gif"))
main_menu = (Image.open((my_path("mainmenu.gif"))))
rarity_image = (Image.open(my_path("rarity.gif")))
program_may_stop_responding = (Image.open(my_path("stopresponding.gif")))
your_folder_is_ready = (Image.open(my_path("yourfolderisready.gif")))

rarity_image = rarity_image.resize((width, height), Image.LANCZOS)
background = background.resize((width, height), Image.LANCZOS)
main_menu = main_menu.resize((width, height), Image.LANCZOS)
program_may_stop_responding = program_may_stop_responding.resize((width, height), Image.LANCZOS)
your_folder_is_ready = your_folder_is_ready.resize((width, height), Image.LANCZOS)

rarity_image = ImageTk.PhotoImage(rarity_image)
background = ImageTk.PhotoImage(background)
main_menu = ImageTk.PhotoImage(main_menu)
program_may_stop_responding = ImageTk.PhotoImage(program_may_stop_responding)
your_folder_is_ready = ImageTk.PhotoImage(your_folder_is_ready)

background_label = tkinter.Label(root, image=main_menu)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

rebrawlModsWarning = tk.Label(root, text="Apk Provided made by S.B ! Works only for v29 servers !",
                              font=("Times", 20, "bold"), fg="red")
rebrawlModsWarning.pack()
rebrawlModsWarning.place(x=0, y=0)

ProgramFinished = tk.Label(root, text="Your Files are Ready !", font=("Times", 40, "bold"), fg="black")
startButton = tk.Button(root, text="Start", font=("Times", 40, "bold"), fg="black")
startButton.pack()
startButton.place(x=width / 2, y=height / 2, anchor=tk.CENTER)
startButton.config(command=lambda: start_button())

ProgramStoppedResponding = tk.Label(root,
                                    text="This will download the needed basic files but should be faster the next time you use AngelFire's Brawler Maker. \nThe program may stop responding now and at the end of the script.\n The time needed depends on your wifi's speed and your computer's power.\n (May take up to a few minutes, and longer the first time).",
                                    font=("Times", 25, "bold"), fg="black")

apk_or_csv__apk = tk.Button(root, text="Automatic Export to APK", font=("Times", 36, "bold"), fg="black")
apk_or_csv__csv = tk.Button(root, text="Manual Setup \n(advanced users only)", font=("Times", 36, "bold"), fg="black")

normal_brawlers__apk = tk.Button(root, text="Start", font=("Times", 30, "bold"), fg="black")

startButtonManual = tk.Button(root, text="Start but select base APK manually", font=("Times", 40, "bold"), fg="black")

openFolder = tk.Button(root, text="Open CSV Logic Folder", font=("Times", 40, "bold"), fg="black",
                       command=csv_logic_path_selector)
openLocalization = tk.Button(root, text="Open Localization Folder", font=("Times", 40, "bold"), fg="black",
                             command=csv_localization_pack_selector)
text_entry1 = tk.Entry(root, font=("Times", 20))
text_entry2 = tk.Entry(root, font=("Times", 20))
text_entry3 = tk.Entry(root, font=("Times", 20))
text_entry4 = tk.Entry(root, font=("Times", 20))
text_entry5 = tk.Entry(root, font=("Times", 20))
text_entry6 = tk.Entry(root, font=("Times", 20))
text_entry7 = tk.Entry(root, font=("Times", 20))
text_entry8 = tk.Entry(root, font=("Times", 20))
text_entry9 = tk.Entry(root, font=("Times", 20))

brawlerNameButton = tk.Label(root, text="Enter Brawler Name", font=("Times", 20, "bold"))
brawlerDescriptionButton = tk.Label(root, text="Enter Brawler Description", font=("Times", 20, "bold"))

common_rarity_image = tk.PhotoImage(file=(my_path("common_rarity.gif")))
rare_rarity_image = tk.PhotoImage(file=(my_path("rare_rarity.gif")))
super_rare_rarity_image = tk.PhotoImage(file=(my_path("super_rare_rarity.gif")))
epic_rarity_image = tk.PhotoImage(file=(my_path("epic_rarity.gif")))
mythic_rarity_image = tk.PhotoImage(file=(my_path("mythic_rarity.gif")))
legendary_rarity_image = tk.PhotoImage(file=(my_path("legendary_rarity.gif")))

brawlerRarityCommon = tk.Button(root, image=common_rarity_image)
brawlerRarityRare = tk.Button(root, image=rare_rarity_image)
brawlerRaritySuperRare = tk.Button(root, image=super_rare_rarity_image)
brawlerRarityEpic = tk.Button(root, image=epic_rarity_image)
brawlerRarityMythic = tk.Button(root, image=mythic_rarity_image)
brawlerRarityLegendary = tk.Button(root, image=legendary_rarity_image)

brawlerAttackName = tk.Label(root, text="Enter the Name of the Attack of your brawler", font=("Times", 20, "bold"))
brawlerAttackDescription = tk.Label(root, text="Enter the Description of the Attack of your brawler",
                                    font=("Times", 20, "bold"))
brawlerUltiName = tk.Label(root, text="Enter the Name of the Super of your brawler)", font=("Times", 20, "bold"))
brawlerUltiDescription = tk.Label(root, text="Enter the Description of the Super of your brawler",
                                  font=("Times", 20, "bold"))

confirmTextsButton = tk.Button(root, text="Next", font=("Times", 30, "bold"))

brawlerSpeedButton = tk.Label(root, text="Enter Brawler Speed \n(720 is default)", font=("Times", 20, "bold"))
brawlerHealthButton = tk.Label(root, text="Enter Brawler Health", font=("Times", 20, "bold"))
brawlerIconButton = tk.Label(root,
                             text="From which brawler do you want the icon",
                             font=("Times", 20, "bold"))
brawlerScaleButton = tk.Label(root, text="Enter Brawler Scale \n(116 is default)", font=("Times", 20, "bold"))
confirmCharacterButton = tk.Button(root, text="Next", font=("Times", 30, "bold"))

NextButton = tk.Button(root, text="Next", font=("Times", 30, "bold"))

MainAttackLabel = tk.Label(root, text="Brawler's Main Attack", font=("Times", 30, "bold"), fg="black")
SuperLabel = tk.Label(root, text="Brawler's Super", font=("Times", 30, "bold"), fg="black")

brawlerAttackRange = tk.Label(root, text="Enter Attack Range \n(see wiki for example values)",
                              font=("Times", 20, "bold"))
brawlerAttackReloadTime = tk.Label(root, text="Enter Reload time per ammo \n(in milliseconds so 1s=1000)",
                                   font=("Times", 20, "bold"))
brawlerAttackAmmoNumber = tk.Label(root, text="Enter Number of Ammo \n(may crash for too big number)",
                                   font=("Times", 20, "bold"))
brawlerAttackDamage = tk.Label(root, text="Enter Attack Damage \n(per projectile)", font=("Times", 20, "bold"))
brawlerAttackSpread = tk.Label(root,
                               text="Enter Attack Spread \n(how wide is an attack)\n(see wiki for example values)",
                               font=("Times", 20, "bold"))
brawlerAttackProjectileNumber = tk.Label(root, text="How many projectiles do you want your attack to have ?",
                                         font=("Times", 20, "bold"))
brawlerAttackProjectile = tk.Label(root,
                                   text="From which Brawler do you want the projectile from ",
                                   font=("Times", 20, "bold"))


def selected(event):
    pass


big_font = ("Times", 20)

icons_dropdown = ttk.Combobox(root, values=list(brawler_names_list.keys()), font=big_font, state="readonly", width=20)
icons_dropdown.current(0)  # To set the default value to the first option
icons_dropdown.bind("<<ComboboxSelected>>", selected)

projectiles_dropdown = ttk.Combobox(root, values=sorted(list(projectiles_dict.keys())), font=big_font, state="readonly",
                                    width=20)
projectiles_dropdown.current(0)  # To set the default value to the first option
projectiles_dropdown.bind("<<ComboboxSelected>>", selected)

skin_dropdown = ttk.Combobox(root, values=['Why are you seeing this ?'], font=big_font, state="readonly", width=20)
skin_dropdown.current(0)  # To set the default value to the first option
skin_dropdown.bind("<<ComboboxSelected>>", selected)
skinDropdownLabel = tk.Label(root,
                             text="Which brawler's skin do you want to use for the TEXTURE",
                             font=("Times", 20, "bold"))

model_dropdown = ttk.Combobox(root, values=['Why are you seeing this ?'], font=big_font, state="readonly", width=20)
model_dropdown.current(0)  # To set the default value to the first option
model_dropdown.bind("<<ComboboxSelected>>", selected)
modelDropdownLabel = tk.Label(root,
                              text="Which brawler's skin do you want to use for the MODEL",
                              font=("Times", 20, "bold"))
brawlerAttackProjectileAttackOrUlti_Attack = tk.Button(root, text="Do you want his/her main attack projectile)",
                                                       font=("Times", 20, "bold"))
brawlerAttackProjectileAttackOrUlti_Super = tk.Button(root, text="Do  you want his/her super's projectile",
                                                      font=("Times", 20, "bold"))

brawlerSuperRange = tk.Label(root, text="Enter Super Range \n(see wiki for example values)", font=("Times", 20, "bold"))
brawlerSuperDamage = tk.Label(root, text="Enter Super Damage \n(per projectile)", font=("Times", 20, "bold"))
brawlerSuperSpread = tk.Label(root,
                              text="Enter Super Spread \n(how wide is a super)\n(see wiki for example values)",
                              font=("Times", 20, "bold"))
brawlerSuperProjectileNumber = tk.Label(root, text="How many projectiles do you want your super to have ?",
                                        font=("Times", 20, "bold"))
brawlerSuperProjectile = tk.Label(root,
                                  text="From which Brawler do you want the projectile from",
                                  font=("Times", 20, "bold"))
brawlerSuperProjectileAttackOrUlti_Attack = tk.Button(root, text="Do you want his/her main attack projectile)",
                                                      font=("Times", 20, "bold"))
brawlerSuperProjectileAttackOrUlti_Super = tk.Button(root, text="Do  you want his/her super's projectile",
                                                     font=("Times", 20, "bold"))

root.mainloop()
