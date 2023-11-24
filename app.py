import csv
import os
import platform
import random
import shutil
import sys
import tkinter
import tkinter as tk
from tkinter import filedialog
from zipfile import ZipFile

from PIL import Image, ImageTk
from mega import Mega


def is_windows():
    return platform.system().lower() == 'windows'


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

height -= taskbar_height

csv_logic_path = ""
csv_localization_path = ""
current_path = os.path.abspath(os.getcwd())

multibrawl_classic_link = 'https://mega.nz/file/cANAhBya#8wFHevhnng_a09IMWPet9BihJaJd3nLDHaEhGqgmIM4'
multibrawl_classic_name = 'BrawlStarsOfflinev29'
brawlername = "AngelFire"
capbrawlername = ""
description = "AngelFire is a brawler"

rarity = ""
attack_name = ""
attack_description = ""
ulti_name = ""
ulti_description = ""

speed = 720
hp = 5000
icon = "shelly"
scale = 116

range = 10
reloadtime = 1000
ammonumber = 3
weapon_or_ulti = ""
damage = "1000"
spread = "60"
numberofprojectiles = 1
projectile = "shelly"
timebetweenattacks = 100
attackduration = "150"
projectiletype = ""
projectiles = ""

button_hidden = 0

chosen_option = 0


def my_path(path_name):
    """Return the appropriate path for data files based on execution context"""
    if getattr(sys, 'frozen', False):
        # running in a bundle
        return os.path.join(sys._MEIPASS, path_name)
    else:
        # running live
        return path_name


projectiles_dict = {
    "shelly": "ShotgunGirl",
    "colt": "Gunslinger",
    "bull": "BullDude",
    "brock": "RocketGirl",
    "rico": "TrickshotDude",
    "spike": "CactusDude",
    "barley": "Barkeep",
    "jessie": "Mechanic1",
    "nita": "Shaman",
    "dynamike": "TntDude",
    "el_primo": "Luchador",
    "mortis": "Undertaker",
    "crow": "Crow",
    "poco": "DeadMariachi",
    "bo": "BowDude",
    "piper": "Sniper",
    "pam": "MinigunDude",
    "tara": "BlackHole",
    "darryl": "BarrelBot",
    "penny": "ArtilleryDude",
    "frank": "HammerDude",
    "gene": "HookDude",
    "tick": "ClusterBombDude",
    "leon": "Ninja",
    "rosa": "Rosa",
    "carl": "Whirlwind",
    "bibi": "Baseball",
    "eight_bit": "Arcade",
    "sandy": "Sandstorm",
    "bea": "BeeSniper",
    "emz": "Mummy",
    "mister_p": "SpawnerDude",
    "max": "Speedy",
    "jacky": "Driller",
    "gale": "Blower",
    "nani": "Controller",
    "sprout": "Wally",
    "surge": "PowerLeveler",
    "colette": "Percenter"
}

brawler_names_list = ['shelly', 'colt', 'bull', 'brock', 'rico', 'spike', 'barley', 'jessie', 'nita', 'dynamike',
                      'el_primo', 'mortis', 'crow', 'poco', 'bo', 'piper', 'pam', 'tara', 'darryl', 'penny', 'frank',
                      'gene', 'tick', 'leon', 'rosa', 'carl', 'bibi', 'eight_bit', 'sandy', 'bea', 'emz', 'mister_p',
                      'max', 'jacky', 'gale', 'nani', 'sprout', 'surge', 'colette']


def start_button():
    startButton.place_forget()
    apk_or_csv__csv.place(x=width / 3, y=height / 2, anchor=tk.CENTER)
    apk_or_csv__csv.config(command=lambda: get_csv_manually())
    apk_or_csv__apk.place(x=width / 1.5, y=height / 2, anchor=tk.CENTER)
    apk_or_csv__apk.config(command=lambda: get_csv_from_apk())
    background_label.configure(image=background)


def get_csv_from_apk():
    apk_or_csv__csv.place_forget()
    apk_or_csv__apk.place_forget()
    normal_brawlers__apk.place(x=width / 2, y=height / 2)
    normal_brawlers__apk.config(command=lambda: result_have_normal_brawlers_only())
    ProgramStoppedResponding.place(x=width / 1.93, y=height / 4.5, anchor=tk.CENTER)


def result_have_normal_brawlers_only():
    global chosen_option
    chosen_option = 3
    global csv_logic_path
    global csv_localization_path
    ProgramStoppedResponding.place_forget()
    normal_brawlers__apk.place_forget()
    if not os.path.exists(os.path.join(current_path, multibrawl_classic_name + ".apk")) and not os.path.exists(
            os.path.join(current_path, multibrawl_classic_name + ".zip")):
        try:
            print("Starting to download APK")
            mega.download_url(multibrawl_classic_link, dest_filename=f"{multibrawl_classic_name}.zip",
                              dest_path=current_path)
            print("Finish downloading APK")
        except PermissionError:
            pass

    if os.path.exists(os.path.join(current_path, multibrawl_classic_name + "/assets/csv_logic")):
        shutil.rmtree(os.path.join(current_path, multibrawl_classic_name))
    with ZipFile(multibrawl_classic_name + ".zip", 'r') as zipp:
        zipp.extractall(os.path.join(current_path, multibrawl_classic_name))
        csv_logic_path = multibrawl_classic_name + "/assets/csv_logic"
        csv_localization_path = multibrawl_classic_name + "/assets/localization"
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
        initialdir="/", title="Select Csv Logic Folder")
    if "csv_logic" in csv_logic_path:
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
        initialdir="/", title="Select Localization Folder")
    if "localization" in csv_localization_path:
        if os.path.exists(os.path.join(current_path, "localization")):
            shutil.rmtree(os.path.join(current_path, "localization"))
            print("Deleted localization folder")
        shutil.copytree(csv_localization_path, os.path.join(current_path, "localization"))
        print("copied localization folder")
        openLocalization.place_forget()
        set_brawler_texts_csv_1()


def hide_button_1(x):
    x.place_forget()
    global button_hidden
    button_hidden = button_hidden + 1
    print(button_hidden)
    if button_hidden == 6:
        text_entry1.place_forget()
        text_entry2.place_forget()
        text_entry3.place_forget()
        text_entry4.place_forget()
        text_entry5.place_forget()
        text_entry6.place_forget()
        set_brawler_texts_csv_2()
    if button_hidden == 10:
        text_entry1.place_forget()
        text_entry2.place_forget()
        text_entry3.place_forget()
        text_entry4.place_forget()
        set_brawler_characters_csv_2()
    if button_hidden == 18:
        text_entry1.place_forget()
        text_entry2.place_forget()
        text_entry3.place_forget()
        text_entry4.place_forget()
        text_entry5.place_forget()
        text_entry6.place_forget()
        text_entry7.place_forget()
        text_entry8.place_forget()
        text_entry9.place_forget()
        set_brawler_skill_csv_attack_2()
    if button_hidden == 24:
        text_entry1.place_forget()
        text_entry2.place_forget()
        text_entry3.place_forget()
        text_entry4.place_forget()
        text_entry5.place_forget()
        text_entry6.place_forget()
        text_entry7.place_forget()
        text_entry8.place_forget()
        text_entry9.place_forget()
        set_brawler_skill_csv_super_2()


def set_brawler_texts_csv_1():
    brawlerNameButton.place(x=width / 19.2, y=height / 4)
    brawlerNameButton.config(command=lambda: hide_button_1(brawlerNameButton))
    text_entry1.place(x=100, y=200)
    brawlerDescriptionButton.place(x=width / 1.92, y=height / 4)
    brawlerDescriptionButton.config(command=lambda: hide_button_1(brawlerDescriptionButton))
    text_entry2.place(x=width / 1.92, y=height / 5.4)
    brawlerAttackName.place(x=width / 19.2, y=height / 1.96)
    brawlerAttackName.config(command=lambda: hide_button_1(brawlerAttackName))
    text_entry3.place(x=width / 19.2, y=height / 2.16)
    brawlerAttackDescription.place(x=width / 19.2, y=height / 1.44)
    brawlerAttackDescription.config(command=lambda: hide_button_1(brawlerAttackDescription))
    text_entry4.place(x=width / 19.2, y=height / 1.54)
    brawlerUltiName.place(x=width / 1.92, y=height / 1.96)
    brawlerUltiName.config(command=lambda: hide_button_1(brawlerUltiName))
    text_entry5.place(x=width / 1.92, y=height / 2.16)
    brawlerUltiDescription.place(x=width / 1.92, y=height / 1.44)
    brawlerUltiDescription.config(command=lambda: hide_button_1(brawlerUltiDescription))
    text_entry6.place(x=width / 1.92, y=height / 1.54)


def set_brawler_texts_csv_2():
    global capbrawlername
    global brawlername
    global attack_name
    global attack_description
    global ulti_description
    global ulti_name
    global description
    brawlername = text_entry1.get()
    description = text_entry2.get()
    attack_name = text_entry3.get()
    attack_description = text_entry4.get()
    ulti_name = text_entry5.get()
    ulti_description = text_entry6.get()
    capbrawlername = brawlername.upper()
    print(current_path)
    print(csv_localization_path)
    print(os.path.join(current_path, csv_localization_path))
    filename = os.path.join(current_path, csv_localization_path) + '/texts.csv'
    with open(filename, 'a', newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([''])
        csv_writer.writerow(['TID_' + capbrawlername, brawlername])
        csv_writer.writerow(['TID_' + capbrawlername + '_DESC', description])
        csv_writer.writerow(['TID_' + capbrawlername + '_WEAPON', attack_name])
        csv_writer.writerow(['TID_' + capbrawlername + '_WEAPON_DESC', attack_description])
        csv_writer.writerow(['TID_' + capbrawlername + '_ULTI', ulti_name])
        csv_writer.writerow(['TID_' + capbrawlername + '_ULTI_DESC', ulti_description])
    background_label.configure(image=rarity)
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
    background_label.configure(image=background)
    brawlerRarityRare.place_forget()
    brawlerRaritySuperRare.place_forget()
    brawlerRarityEpic.place_forget()
    brawlerRarityMythic.place_forget()
    brawlerRarityLegendary.place_forget()
    brawlerRarityCommon.place_forget()
    brawlernumber = random.randint(1500, 9999)
    text_entry1.delete(0, tkinter.END)
    filename = os.path.join(os.path.join(current_path, csv_logic_path), 'cards.csv')
    with open(filename, 'a', newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(
            ['', '', '', '', '', '', '', '', '', '', '', '', '', '',
             '', '', '', '', '', '', '', ''])
        csv_writer.writerow(
            [brawlername + '_unlock', 'sc/ui.sc', '', brawlername, '', '', '0', '', 'unlock', '', '', '', '', rarity,
             '', '', '', '', '', '', brawlernumber, ''])
        csv_writer.writerow(
            [brawlername + '_hp', 'sc/ui.sc', 'health_icon', brawlername, '', '', '1', '', 'hp', '', '', '', '',
             'common', 'TID_ARMOR', 'TID_ARMOR', '', '', 'genicon_health', '', '', ''])
        csv_writer.writerow([brawlername + '_abi', 'sc/ui.sc', 'attack_icon', brawlername, '', '', '2', '', 'skill',
                             brawlername + 'Weapon', '', '', '', 'common', 'TID_' + capbrawlername + '_WEAPON',
                             'TID_STAT_DAMAGE', '', '', 'genicon_damage', '', '', ''])
        csv_writer.writerow([brawlername + '_ulti', 'sc/ui.sc', 'ulti_icon', brawlername, '', '', '3', '', 'skill',
                             brawlername + 'Ulti', '', '', '', 'common', 'TID_' + capbrawlername + '_ULTI',
                             'TID_STAT_DAMAGE', '', '', 'genicon_damage', '', '', ''])
    set_brawler_characters_csv_1()


def set_brawler_characters_csv_1():
    text_entry1.delete(0, tkinter.END)
    text_entry2.delete(0, tkinter.END)
    text_entry3.delete(0, tkinter.END)
    text_entry4.delete(0, tkinter.END)
    text_entry5.delete(0, tkinter.END)
    text_entry6.delete(0, tkinter.END)
    brawlerSpeedButton.place(x=width / 19.2, y=height / 4)
    brawlerSpeedButton.config(command=lambda: hide_button_1(brawlerSpeedButton))
    text_entry1.place(x=width / 19.2, y=height / 5)
    brawlerHealthButton.place(x=width / 1.92, y=height / 4)
    brawlerHealthButton.config(command=lambda: hide_button_1(brawlerHealthButton))
    text_entry2.place(x=width / 1.92, y=height / 5)
    brawlerScaleButton.place(x=width / 19.2, y=height / 1.96)
    brawlerScaleButton.config(command=lambda: hide_button_1(brawlerScaleButton))
    text_entry3.place(x=width / 19.2, y=height / 2.16)
    brawlerIconButton.place(x=width / 19.2, y=height / 1.44)
    brawlerIconButton.config(command=lambda: hide_button_1(brawlerIconButton))
    text_entry4.place(x=width / 19.2, y=height / 1.54)


def set_brawler_characters_csv_2():
    global capbrawlername
    global speed
    global hp
    global icon
    global scale
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
    icon = text_entry4.get()
    if icon.lower() not in brawler_names_list or icon not in brawler_names_list:
        icon = "shelly"
    ultichargemul = random.randint(90, 135)
    ultichargeultimul = random.randint(90, 150)
    capbrawlername = brawlername.upper()
    filename = os.path.join(os.path.join(current_path, csv_logic_path), 'characters.csv')
    with open(filename, 'a', newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([''])
        csv_writer.writerow(
            [brawlername, '', '', 'bull', brawlername + 'Weapon', brawlername + 'Ulti', '', speed, hp, '', '', '', '',
             '', '', '', '12', '', ultichargemul, ultichargeultimul, "Hero", '', brawlername + 'Default', '', '', '',
             '', '', '', 'takedamage_gen', 'death_shotgun_girl', 'Gen_move_fx', 'reload_shotgun_girl',
             'No_ammo_shotgungirl', 'Dry_fire_shotgungirl', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
             '', '', '30', '', '80', '80', '', '', '35', scale, '210', '284', '90', '175', '260', '', '', '', '-25',
             '40', '120', 'Medium', '-48', '', '450', '', '', 'TID_' + capbrawlername, '', 'sc/ui.sc',
             'hero_icon_' + icon, '0', 'human', 'footstep', '25', '250', '200', '', '', '1', '3', '2', '', '', '', '',
             '', '', '', '', '', 'ShellyTutorial', '', '', '', '', '', '3', '3', '3'])
    generate_brawler_skin_files()


def generate_brawler_skin_files():
    filename = os.path.join(os.path.join(current_path, csv_logic_path), 'skins.csv')
    with open(filename, 'a', newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([''])
        csv_writer.writerow(
            [brawlername + 'Default', brawlername + 'Default', '', '', '', '', '', '', '', '', '', '', '', '', '',
             'shelly_v2_01.pvr', 'shelly_v2_01.pvr', 'shelly_v2_01.pvr', 'shelly_v2_01.pvr'])
    filename = os.path.join(os.path.join(current_path, csv_logic_path), 'skin_confs.csv')
    with open(filename, 'a', newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([''])
        csv_writer.writerow(
            [brawlername + 'Default', brawlername, 'shelly_geo.scw', '', '', 'shelly_base_cam.scw',
             'shelly_intro_pose.scw',
             '', 'ShellyIdle', 'ShellyWalk', 'ShellyPrimary', 'ShellySecondary', 'ShellyRecoil', '', 'ShellyRecoil', '',
             'ShellyReload', 'ShellyPushback', 'ShellyWin', 'ShellyWinloop', 'ShellyLose', 'ShellyLoseloop',
             'ShellyIdle',
             'ShellyWin', 'ShellyWinloop', 'ShellyWin', 'ShellyIdle', 'ShellyIdle', 'ShellyProfile', 'ShellyIntro', '',
             '',
             '', '', '', 'ShellyFace', 'ShellyFace', 'ShellyHappy', 'ShellyFace', 'ShellySad', 'ShellySadLoop',
             'ShellyFace', 'ShellyHappy', 'ShellyFace', 'ShellyHappy', 'ShellyStill', 'ShellyStill', '', '', '', 'true',
             'true', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
             '',
             '', '', '', '', '', ', '', ', '', '', '', ''])
    MainAttackNextButton.place(x=width / 2, y=height / 2)
    MainAttackNextButton.config(command=lambda: set_brawler_skill_csv_attack_1())


def set_brawler_skill_csv_attack_1():
    text_entry1.delete(0, tkinter.END)
    text_entry2.delete(0, tkinter.END)
    text_entry3.delete(0, tkinter.END)
    text_entry4.delete(0, tkinter.END)
    text_entry5.delete(0, tkinter.END)
    text_entry6.delete(0, tkinter.END)
    text_entry7.delete(0, tkinter.END)
    text_entry8.delete(0, tkinter.END)
    MainAttackNextButton.place_forget()
    brawlerAttackRange.place(x=width / 19.2, y=height / 7.2)
    brawlerAttackRange.config(command=lambda: hide_button_1(brawlerAttackRange))
    text_entry1.place(x=width / 19.2, y=height / 10.8)
    brawlerAttackProjectile.place(x=width / 1.92, y=height / 4.32)
    brawlerAttackProjectile.config(command=lambda: show_attack_or_ulti_buttons())
    text_entry2.place(x=width / 1.92, y=height / 5.4)
    brawlerAttackProjectileNumber.place(x=width / 19.2, y=height / 1.96)
    brawlerAttackProjectileNumber.config(command=lambda: hide_button_1(brawlerAttackProjectileNumber))
    text_entry5.place(x=width / 19.2, y=height / 2.16)
    brawlerAttackDamage.place(x=width / 1.92, y=height / 1.44)
    brawlerAttackDamage.config(command=lambda: hide_button_1(brawlerAttackDamage))
    text_entry6.place(x=width / 1.92, y=height / 1.54)
    brawlerAttackReloadTime.place(x=width / 1.92, y=height / 1.96)
    brawlerAttackReloadTime.config(command=lambda: hide_button_1(brawlerAttackReloadTime))
    text_entry7.place(x=width / 1.92, y=height / 2.16)
    brawlerAttackAmmoNumber.place(x=width / 38.4, y=height / 1.44)
    brawlerAttackAmmoNumber.config(command=lambda: hide_button_1(brawlerAttackAmmoNumber))
    text_entry8.place(x=width / 38.4, y=height / 1.54)
    brawlerAttackSpread.place(x=width / 19.2, y=height / 3.08)
    brawlerAttackSpread.config(command=lambda: hide_button_1(brawlerAttackSpread))
    text_entry9.place(x=width / 19.2, y=height / 3.6)


def show_attack_or_ulti_buttons():
    brawlerAttackProjectile.place_forget()
    text_entry2.place_forget()
    brawlerAttackProjectileAttackOrUlti_Attack.place(x=width / 1.92, y=height / 4)
    brawlerAttackProjectileAttackOrUlti_Attack.config(command=lambda: set_attack_projectile_ulti_or_attack(1))
    brawlerAttackProjectileAttackOrUlti_Super.place(x=width / 1.92, y=height / 3.08)
    brawlerAttackProjectileAttackOrUlti_Super.config(command=lambda: set_attack_projectile_ulti_or_attack(1))


def set_attack_projectile_ulti_or_attack(number):
    global projectiletype
    if number == 1:
        projectiletype = "Projectile"
        hide_button_1(brawlerAttackProjectileAttackOrUlti_Attack)
        hide_button_1(brawlerAttackProjectileAttackOrUlti_Super)
    elif number == 2:
        projectiletype = "UltiProjectile"
        hide_button_1(brawlerAttackProjectileAttackOrUlti_Attack)
        hide_button_1(brawlerAttackProjectileAttackOrUlti_Super)


def set_brawler_skill_csv_attack_2():
    global range
    range = text_entry1.get()
    global projectile
    global projectiles
    projectile = text_entry2.get()
    try:
        projectiles = projectiles_dict[projectile.lower()]
    except KeyError:
        projectiles = projectiles_dict["shelly"]
    global numberofprojectiles
    numberofprojectiles = text_entry5.get()
    try:
        int(numberofprojectiles)
    except ValueError:
        numberofprojectiles = str(1)
    if int(numberofprojectiles) > 20:
        numberofprojectiles = str(20)
    global damage
    damage = text_entry6.get()
    try:
        int(damage)
    except ValueError:
        damage = str(1000)
    if int(damage) > 10000:
        damage = str(10000)
    global reloadtime
    reloadtime = text_entry7.get()
    try:
        int(reloadtime)
    except ValueError:
        reloadtime = str(1000)
    if int(reloadtime) > 4999:
        reloadtime = str(4999)
    if int(reloadtime) < 1:
        reloadtime = str(1)
    global ammonumber
    ammonumber = text_entry8.get()
    try:
        int(ammonumber)
    except ValueError:
        ammonumber = str(3)
    if int(ammonumber) > 4:
        ammonumber = str(4)
    if int(ammonumber) < 1:
        ammonumber = str(1)
    global spread
    spread = text_entry9.get()
    try:
        int(spread)
    except ValueError:
        spread = str(1000)
    if int(spread) > 359:
        spread = str(4999)
    filename = os.path.join(os.path.join(current_path, csv_logic_path), 'skills.csv')
    with open(filename, 'a', newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([''])
        csv_writer.writerow(
            [brawlername + "Weapon", 'Attack', 'true', 'true', 'true', '', '50', attackduration, '', range, '', '',
             '', '', reloadtime, ammonumber, damage, '', timebetweenattacks, spread, '', numberofprojectiles, '',
             'true', '', '', '', '', '', '', '', '', projectiles + projectiletype, '', '', '', '', '', '', '', '',
             'sc/ui.sc', 'rapid_fire_button', 'rico_def_atk', '', '', '', '', '', '', '', '', '', '', '', ''])

    SuperNextButton.place(x=500, y=350)
    SuperNextButton.config(command=lambda: set_brawler_skill_csv_super_1())


def set_brawler_skill_csv_super_1():
    text_entry1.delete(0, tkinter.END)
    text_entry2.delete(0, tkinter.END)
    text_entry3.delete(0, tkinter.END)
    text_entry4.delete(0, tkinter.END)
    text_entry5.delete(0, tkinter.END)
    text_entry6.delete(0, tkinter.END)
    text_entry7.delete(0, tkinter.END)
    text_entry8.delete(0, tkinter.END)
    SuperNextButton.place_forget()
    brawlerSuperRange.place(x=width / 19.2, y=height / 7.2)
    brawlerSuperRange.config(command=lambda: hide_button_1(brawlerSuperRange))
    text_entry1.place(x=width / 19.2, y=height / 10.8)
    brawlerSuperProjectile.place(x=width / 1.92, y=height / 3.08)
    brawlerSuperProjectile.config(command=lambda: show_attack_or_ulti_buttons_super())
    text_entry2.place(x=width / 1.92, y=height / 3.6)
    brawlerSuperProjectileNumber.place(x=100, y=height / 1.96)
    brawlerSuperProjectileNumber.config(command=lambda: hide_button_1(brawlerSuperProjectileNumber))
    text_entry5.place(x=width / 19.2, y=height / 2.16)
    brawlerSuperDamage.place(x=width / 19.2, y=height / 1.44)
    brawlerSuperDamage.config(command=lambda: hide_button_1(brawlerSuperDamage))
    text_entry6.place(x=width / 19.2, y=height / 1.54)
    brawlerSuperSpread.place(x=width / 19.2, y=height / 3.08)
    brawlerSuperSpread.config(command=lambda: hide_button_1(brawlerSuperSpread))
    text_entry9.place(x=width / 19.2, y=height / 3.6)


def show_attack_or_ulti_buttons_super():
    brawlerSuperProjectile.place_forget()
    text_entry2.place_forget()
    brawlerSuperProjectileAttackOrUlti_Attack.place(x=width / 1.92, y=height / 4.32)
    brawlerSuperProjectileAttackOrUlti_Attack.config(command=lambda: set_attack_projectile_ulti_or_attack_super(1))
    brawlerSuperProjectileAttackOrUlti_Super.place(x=width / 1.92, y=height / 3.08)
    brawlerSuperProjectileAttackOrUlti_Super.config(command=lambda: set_attack_projectile_ulti_or_attack_super(2))


def set_attack_projectile_ulti_or_attack_super(number):
    global projectiletype
    if number == 1:
        projectiletype = "Projectile"
        hide_button_1(brawlerSuperProjectileAttackOrUlti_Attack)
        hide_button_1(brawlerSuperProjectileAttackOrUlti_Super)
    elif number == 2:
        projectiletype = "UltiProjectile"
        hide_button_1(brawlerSuperProjectileAttackOrUlti_Attack)
        hide_button_1(brawlerSuperProjectileAttackOrUlti_Super)


def set_brawler_skill_csv_super_2():
    global range
    range = text_entry1.get()
    global projectile
    global projectiles
    projectile = text_entry2.get()
    try:
        projectiles = projectiles_dict[projectile.lower()]
    except KeyError:
        projectiles = projectiles_dict["shelly"]
    global numberofprojectiles
    numberofprojectiles = text_entry5.get()
    try:
        int(numberofprojectiles)
    except ValueError:
        numberofprojectiles = str(1)
    if int(numberofprojectiles) > 20:
        numberofprojectiles = str(20)
    global damage
    damage = text_entry6.get()
    try:
        int(damage)
    except ValueError:
        damage = str(1000)
    if int(damage) > 10000:
        damage = str(10000)
    global reloadtime
    reloadtime = text_entry7.get()
    try:
        int(reloadtime)
    except ValueError:
        reloadtime = str(1000)
    if int(reloadtime) > 4999:
        reloadtime = str(4999)
    if int(reloadtime) < 1:
        reloadtime = str(1)
    global ammonumber
    ammonumber = text_entry8.get()
    try:
        int(ammonumber)
    except ValueError:
        ammonumber = str(3)
    if int(ammonumber) > 4:
        ammonumber = str(4)
    if int(ammonumber) < 1:
        ammonumber = str(1)
    global spread
    spread = text_entry9.get()
    try:
        int(spread)
    except ValueError:
        spread = str(1000)
    if int(spread) > 359:
        spread = str(4999)
    filename = os.path.join(os.path.join(current_path, csv_logic_path), 'skills.csv')
    with open(filename, 'a', newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([''])
        csv_writer.writerow(
            [brawlername + "Ulti", 'Attack', 'true', 'true', 'true', '', '50', attackduration, '', range, '', '',
             '', '', reloadtime, ammonumber, damage, '', timebetweenattacks, spread, '', numberofprojectiles, '',
             'true', '', '', '', '', '', '', '', '', projectiles + projectiletype, '', '', '', '', '', '', '', '',
             'sc/ui.sc', 'rapid_fire_button', 'rico_def_atk', '', '', '', '', '', '', '', '', '', '', '', ''])
    if chosen_option == 1:
        background_label.configure(image=your_folder_is_ready)
    elif chosen_option == 3:
        if os.path.exists(os.path.join(current_path, multibrawl_classic_name + " - Brawler Maker")):
            shutil.rmtree(os.path.join(current_path, multibrawl_classic_name + " - Brawler Maker"))
        os.rename(multibrawl_classic_name, multibrawl_classic_name + " - Brawler Maker")
        if os.path.exists(os.path.join(current_path, multibrawl_classic_name + " - Brawler Maker" + ".zip")):
            os.remove(os.path.join(current_path, multibrawl_classic_name + " - Brawler Maker" + ".zip"))
        if os.path.exists(
                os.path.join(current_path, multibrawl_classic_name.replace(' ', '-') + "-BrawlerMaker" + ".apk")):
            os.remove(os.path.join(current_path, multibrawl_classic_name.replace(' ', '-') + "-BrawlerMaker" + ".apk"))
        shutil.make_archive(multibrawl_classic_name + " - Brawler Maker", "zip",
                            os.path.join(current_path, multibrawl_classic_name + " - Brawler Maker"))
        os.rename(os.path.join(current_path, multibrawl_classic_name + " - Brawler Maker" + ".zip"),
                  multibrawl_classic_name.replace(' ', '-') + "-BrawlerMaker" + ".apk")
        os.system('java -jar ' + my_path(
            "uber-apk-signer.jar") + ' -a "' + current_path + "/" + multibrawl_classic_name + '-BrawlerMaker' + '.apk"')
        background_label.configure(image=your_folder_is_ready)


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
                                    text="Program may stop responding here and at the end of the script. Duration depends on your wifi and your computer.",
                                    font=("Times", 25, "bold"), fg="black")

apk_or_csv__apk = tk.Button(root, text="Setup Automatically", font=("Times", 40, "bold"), fg="black")
apk_or_csv__csv = tk.Button(root, text="Choose Folders Manually", font=("Times", 40, "bold"), fg="black")

normal_brawlers__apk = tk.Button(root, text="Start", font=("Times", 30, "bold"), fg="black")

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

brawlerNameButton = tk.Button(root, text="Enter Brawler Name", font=("Times", 20, "bold"))
brawlerDescriptionButton = tk.Button(root, text="Enter Brawler Description", font=("Times", 20, "bold"))

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

brawlerAttackName = tk.Button(root, text="Enter the Name of the Attack of your brawler", font=("Times", 20, "bold"))
brawlerAttackDescription = tk.Button(root, text="Enter the Description of the Attack of your brawler",
                                     font=("Times", 20, "bold"))
brawlerUltiName = tk.Button(root, text="Enter the Name of the Super of your brawler)", font=("Times", 20, "bold"))
brawlerUltiDescription = tk.Button(root, text="Enter the Description of the Super of your brawler",
                                   font=("Times", 20, "bold"))

brawlerSpeedButton = tk.Button(root, text="Enter Brawler Speed \n(720 is default)", font=("Times", 20, "bold"))
brawlerHealthButton = tk.Button(root, text="Enter Brawler Health", font=("Times", 20, "bold"))
brawlerIconButton = tk.Button(root,
                              text="From what brawler do you want the icon \n(exeptions : 8bit = eight_bit, primo = el_primo \nand mr.P = mister_p)",
                              font=("Times", 20, "bold"))
brawlerScaleButton = tk.Button(root, text="Enter Brawler Scale \n(116 is default)", font=("Times", 20, "bold"))

MainAttackNextButton = tk.Button(root, text="Now let's continue with the main attack", font=("Times", 20, "bold"))
SuperNextButton = tk.Button(root, text="Now let's continue with the super", font=("Times", 20, "bold"))

brawlerAttackRange = tk.Button(root, text="Enter Attack Range \n(bull is 16 and rico 29)", font=("Times", 20, "bold"))
brawlerAttackReloadTime = tk.Button(root, text="Enter Reload time \n(in milliseconds so 1s=1000)\n(per ammo) ",
                                    font=("Times", 20, "bold"))
brawlerAttackAmmoNumber = tk.Button(root, text="Enter Number of Ammo \n(may crash for too big number)",
                                    font=("Times", 20, "bold"))
brawlerAttackDamage = tk.Button(root, text="Enter Attack Damage \n(per projectile)", font=("Times", 20, "bold"))
brawlerAttackSpread = tk.Button(root,
                                text="Enter Attack Spread \n(how wide is an attack)\n(shelly is 60, bow is 30 and poco is 130)",
                                font=("Times", 20, "bold"))
brawlerAttackProjectileNumber = tk.Button(root, text="How Many Projectiles do you want for your attack ?",
                                          font=("Times", 20, "bold"))
brawlerAttackProjectile = tk.Button(root,
                                    text="From what Brawler do you want the projectile from \n(brawler name no cap)\n(exeptions : 8bit = eight_bit, primo = el_primo \nand mr.P = mister_p)",
                                    font=("Times", 20, "bold"))
brawlerAttackProjectileAttackOrUlti_Attack = tk.Button(root, text="Do you want his/her main attack projectile)",
                                                       font=("Times", 20, "bold"))
brawlerAttackProjectileAttackOrUlti_Super = tk.Button(root, text="Do  you want his/her super's projectile",
                                                      font=("Times", 20, "bold"))

SuperAttackNextButton = tk.Button(root, text="Now let's continue with the super", font=("Times", 20, "bold"))

brawlerSuperRange = tk.Button(root, text="Enter Super Range \n(bull is 16 and rico 29)", font=("Times", 20, "bold"))
brawlerSuperDamage = tk.Button(root, text="Enter Super Damage \n(per projectile)", font=("Times", 20, "bold"))
brawlerSuperSpread = tk.Button(root,
                               text="Enter Super Spread \n(how wide is a super)\n(shelly is 60, bow is 30 and poco is 130)",
                               font=("Times", 20, "bold"))
brawlerSuperProjectileNumber = tk.Button(root, text="How Many Projectiles do you want for your super ?",
                                         font=("Times", 20, "bold"))
brawlerSuperProjectile = tk.Button(root,
                                   text="From what Brawler do you want the projectile from \n(brawler name no cap)\n(exeptions : 8bit = eight_bit, primo = el_primo \nand mr.P = mister_p)",
                                   font=("Times", 20, "bold"))
brawlerSuperProjectileAttackOrUlti_Attack = tk.Button(root, text="Do you want his/her main attack projectile)",
                                                      font=("Times", 20, "bold"))
brawlerSuperProjectileAttackOrUlti_Super = tk.Button(root, text="Do  you want his/her super's projectile",
                                                     font=("Times", 20, "bold"))

root.mainloop()
