import csv
import os
import platform
import random
import shutil
import sys
import tkinter
import tkinter as tk
from tkinter import filedialog, ttk
from zipfile import ZipFile

from PIL import Image, ImageTk
from mega import Mega


def is_windows():
    return platform.system().lower() == 'windows'


class Brawler:
    def __init__(self, brawlername="AngelFire", description="I'm the creator of brawler Maker !", rarity="rare",
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

default_apk_link = 'https://mega.nz/file/cANAhBya#8wFHevhnng_a09IMWPet9BihJaJd3nLDHaEhGqgmIM4'
default_apk = 'BrawlStarsOfflinev29'

brawler = Brawler()

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
    "shelly main attack": "ShotgunGirlProjectile",
    "colt main attack": "GunslingerProjectile",
    "bull main attack": "BullDudeProjectile",
    "brock main attack": "RocketGirlProjectile",
    "rico main attack": "TrickshotDudeProjectile",
    "spike main attack": "CactusDudeProjectile",
    "barley main attack": "BarkeepProjectile",
    "jessie main attack": "Mechanic1Projectile",
    "nita main attack": "ShamanProjectile",
    "dynamike main attack": "TntDudeProjectile",
    "el_primo main attack": "LuchadorProjectile",
    "mortis main attack": "UndertakerProjectile",
    "crow main attack": "CrowProjectile",
    "poco main attack": "DeadMariachiProjectile",
    "bo main attack": "BowDudeProjectile",
    "piper main attack": "SniperProjectile",
    "pam main attack": "MinigunDudeProjectile",
    "tara main attack": "BlackHoleProjectile",
    "darryl main attack": "BarrelBotProjectile",
    "penny main attack": "ArtilleryDudeProjectile",
    "frank main attack": "HammerDudeProjectile",
    "gene main attack": "HookDudeProjectile",
    "tick main attack": "ClusterBombDudeProjectile",
    "leon main attack": "NinjaProjectile",
    "rosa main attack": "RosaProjectile",
    "carl main attack": "WhirlwindProjectile",
    "bibi main attack": "BaseballProjectile",
    "eight_bit main attack": "ArcadeProjectile",
    "sandy main attack": "SandstormProjectile",
    "bea main attack": "BeeSniperProjectile",
    "emz main attack": "MummyProjectile",
    "mister_p main attack": "SpawnerDudeProjectile",
    "max main attack": "SpeedyProjectile",
    "jacky main attack": "DrillerProjectile",
    "gale main attack": "BlowerProjectile",
    "nani main attack": "ControllerProjectile",
    "sprout main attack": "WallyProjectile",
    "surge main attack": "PowerLevelerProjectile",
    "colette main attack": "PercenterProjectile",
    "shelly super": "ShotgunGirlUltiProjectile",
    "colt super": "GunslingerUltiProjectile",
    "bull super": "BullDudeUltiProjectile",
    "brock super": "RocketGirlUltiProjectile",
    "rico super": "TrickshotDudeUltiProjectile",
    "spike super": "CactusDudeUltiProjectile",
    "barley super": "BarkeepUltiProjectile",
    "jessie super": "Mechanic1UltiProjectile",
    "nita super": "ShamanUltiProjectile",
    "dynamike super": "TntDudeUltiProjectile",
    "el_primo super": "LuchadorUltiProjectile",
    "mortis super": "UndertakerUltiProjectile",
    "crow super": "CrowUltiProjectile",
    "poco super": "DeadMariachiUltiProjectile",
    "bo super": "BowDudeUltiProjectile",
    "piper super": "SniperUltiProjectile",
    "pam super": "MinigunDudeUltiProjectile",
    "tara super": "BlackHoleUltiProjectile",
    "darryl super": "BarrelBotUltiProjectile",
    "penny super": "ArtilleryDudeUltiProjectile",
    "frank super": "HammerDudeUltiProjectile",
    "gene super": "HookDudeUltiProjectile",
    "tick super": "ClusterBombDudeUltiProjectile",
    "leon super": "NinjaUltiProjectile",
    "rosa super": "RosaUltiProjectile",
    "carl super": "WhirlwindUltiProjectile",
    "bibi super": "BaseballUltiProjectile",
    "eight_bit super": "ArcadeUltiProjectile",
    "sandy super": "SandstormUltiProjectile",
    "bea super": "BeeSniperUltiProjectile",
    "emz super": "MummyUltiProjectile",
    "mister_p super": "SpawnerDudeUltiProjectile",
    "max super": "SpeedyUltiProjectile",
    "jacky super": "DrillerUltiProjectile",
    "gale super": "BlowerUltiProjectile",
    "nani super": "ControllerUltiProjectile",
    "sprout super": "WallyUltiProjectile",
    "surge super": "PowerLevelerUltiProjectile",
    "colette super": "PercenterUltiProjectile",
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
    if not os.path.exists(os.path.join(current_path, default_apk + ".apk")) and not os.path.exists(
            os.path.join(current_path, default_apk + ".zip")):
        try:
            print("Starting to download APK")
            mega.download_url(default_apk_link, dest_filename=f"{default_apk}.zip",
                              dest_path=current_path)
            print("Finish downloading APK")
        except PermissionError:
            pass

    if os.path.exists(os.path.join(current_path, default_apk + "/assets/csv_logic")):
        shutil.rmtree(os.path.join(current_path, default_apk))
    with ZipFile(default_apk + ".zip", 'r') as zipp:
        zipp.extractall(os.path.join(current_path, default_apk))
        csv_logic_path = default_apk + "/assets/csv_logic"
        csv_localization_path = default_apk + "/assets/localization"
        set_brawler_texts_csv_1()

    csv_logic_path = default_apk + "/assets/csv_logic"
    csv_localization_path = default_apk + "/assets/localization"
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
    combo.place_forget()
    combo.current(0)
    icon_combo.place_forget()
    icon_combo.current(0)


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
    filename = os.path.join(current_path, csv_localization_path) + '/texts.csv'
    with open(filename, 'a', newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([''])
        csv_writer.writerow(['TID_' + brawler.capbrawlername, brawler.brawlername])
        csv_writer.writerow(['TID_' + brawler.capbrawlername + '_DESC', brawler.description])
        csv_writer.writerow(['TID_' + brawler.capbrawlername + '_WEAPON', brawler.attack_name])
        csv_writer.writerow(['TID_' + brawler.capbrawlername + '_WEAPON_DESC', brawler.attack_description])
        csv_writer.writerow(['TID_' + brawler.capbrawlername + '_ULTI', brawler.ulti_name])
        csv_writer.writerow(['TID_' + brawler.capbrawlername + '_ULTI_DESC', brawler.ulti_description])

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
    background_label.configure(image=background)
    brawlerRarityRare.place_forget()
    brawlerRaritySuperRare.place_forget()
    brawlerRarityEpic.place_forget()
    brawlerRarityMythic.place_forget()
    brawlerRarityLegendary.place_forget()
    brawlerRarityCommon.place_forget()
    brawlernumber = random.randint(1500, 9999)
    filename = os.path.join(os.path.join(current_path, csv_logic_path), 'cards.csv')
    with open(filename, 'a', newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(
            ['', '', '', '', '', '', '', '', '', '', '', '', '', '',
             '', '', '', '', '', '', '', ''])
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
    set_brawler_characters_csv_1()


def set_brawler_characters_csv_1():
    hide_and_clear_texts()

    text_entry1.place(x=width / 19.2, y=height / 3.5)
    text_entry2.place(x=width / 1.92, y=height / 4)
    text_entry3.place(x=width / 19.2, y=height / 1.8)
    icon_combo.place(x=width / 19.2, y=height / 1.44)

    brawlerSpeedButton.place(x=width / 19.2, y=height / 5)
    brawlerHealthButton.place(x=width / 1.92, y=height / 5)
    brawlerScaleButton.place(x=width / 19.2, y=height / 2.16)
    brawlerIconButton.place(x=width / 19.2, y=height / 1.54)

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

    icon = icon_combo.get()
    if icon.lower() not in brawler_names_list:
        icon = "shelly"
    ultichargemul = random.randint(90, 135)
    ultichargeultimul = random.randint(90, 150)
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
    generate_brawler_skin_files()


def generate_brawler_skin_files():
    filename = os.path.join(os.path.join(current_path, csv_logic_path), 'skins.csv')
    with open(filename, 'a', newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([''])
        csv_writer.writerow(
            [brawler.brawlername + 'Default', brawler.brawlername + 'Default', '', '', '', '', '', '', '', '', '', '',
             '', '', '',
             'shelly_v2_01.pvr', 'shelly_v2_01.pvr', 'shelly_v2_01.pvr', 'shelly_v2_01.pvr'])
    filename = os.path.join(os.path.join(current_path, csv_logic_path), 'skin_confs.csv')
    with open(filename, 'a', newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([''])
        csv_writer.writerow(
            [brawler.brawlername + 'Default', brawler.brawlername, 'shelly_geo.scw', '', '', 'shelly_base_cam.scw',
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
    set_brawler_skill_csv_attack_1()


def set_brawler_skill_csv_attack_1():
    hide_and_clear_texts()
    confirmCharacterButton.place_forget()
    brawlerSpeedButton.place_forget()
    brawlerHealthButton.place_forget()
    brawlerScaleButton.place_forget()
    brawlerIconButton.place_forget()

    text_entry1.place(x=width / 19.2, y=height / 3.8)
    combo.place(x=width / 1.92, y=height / 4.32)
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
        brawler.chosen_projectile = projectiles_dict[combo.get()]
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
    combo.place(x=width / 1.92, y=height / 4.32)
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
        brawler.chosen_projectile = projectiles_dict[combo.get()]
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
    hide_and_clear_texts()
    brawlerSuperRange.place_forget()
    brawlerSuperProjectile.place_forget()
    brawlerSuperProjectileNumber.place_forget()
    brawlerSuperDamage.place_forget()
    brawlerSuperSpread.place_forget()
    SuperLabel.place_forget()
    NextButton.place_forget()

    if chosen_option == 1:
        background_label.configure(image=your_folder_is_ready)
    elif chosen_option == 3:
        if os.path.exists(os.path.join(current_path, default_apk + " - Brawler Maker")):
            shutil.rmtree(os.path.join(current_path, default_apk + " - Brawler Maker"))
        os.rename(default_apk, default_apk + " - Brawler Maker")
        if os.path.exists(os.path.join(current_path, default_apk + " - Brawler Maker" + ".zip")):
            os.remove(os.path.join(current_path, default_apk + " - Brawler Maker" + ".zip"))
        if os.path.exists(
                os.path.join(current_path, default_apk.replace(' ', '-') + "-BrawlerMaker" + ".apk")):
            os.remove(os.path.join(current_path, default_apk.replace(' ', '-') + "-BrawlerMaker" + ".apk"))
        shutil.make_archive(default_apk + " - Brawler Maker", "zip",
                            os.path.join(current_path, default_apk + " - Brawler Maker"))
        os.rename(os.path.join(current_path, default_apk + " - Brawler Maker" + ".zip"),
                  default_apk.replace(' ', '-') + "-BrawlerMaker" + ".apk")
        os.system('java -jar ' + my_path(
            "uber-apk-signer.jar") + ' -a "' + current_path + "/" + default_apk + '-BrawlerMaker' + '.apk"')
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
    print(combo.get())


big_font = ("Times", 20)

icon_combo = ttk.Combobox(root, values=brawler_names_list, font=big_font, state="readonly", width=20)
icon_combo.current(0)  # To set the default value to the first option
icon_combo.bind("<<ComboboxSelected>>", selected)

combo = ttk.Combobox(root, values=sorted(list(projectiles_dict.keys())), font=big_font, state="readonly", width=20)
combo.current(0)  # To set the default value to the first option
combo.bind("<<ComboboxSelected>>", selected)
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
