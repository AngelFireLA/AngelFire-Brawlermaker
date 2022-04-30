import csv
import os
import random
import shutil
import tkinter
import tkinter as tk
import zipfile
import apk_signer as signer

import mega
from mega import Mega
from tkinter import filedialog
from zipfile import ZipFile



mega = Mega()

root = tk.Tk()
root.state('zoomed')

csv_logic_path = ""
csv_localization_path = ""
current_path = os.path.abspath(os.getcwd())

multibrawl_mod_link = 'https://mega.nz/file/zxFXiYwS#59n4MtQ6kTuM2SKCSVIn-fgHyYSmI5yHJG9-5F6lW5U'
multibrawl_mod_name = 'Multi Brawl V38 Online'
multibrawl_classic_link = 'https://mega.nz/file/4UUDSZyQ#txA_jXb0m6zFL5_V7uxNGGG9jEgl9Ldz0rwBde9u-LQ'
multibrawl_classic_name = 'Multi Brawl Cl V37.9'
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


def start_button():
    startButton.place_forget()
    apk_or_csv__csv.place(x=630, y=540, anchor=tk.CENTER)
    apk_or_csv__csv.config(command=lambda: get_csv_manually())
    apk_or_csv__apk.place(x=1290, y=540, anchor=tk.CENTER)
    apk_or_csv__apk.config(command=lambda: get_csv_from_apk())


def get_csv_from_apk():
    apk_or_csv__csv.place_forget()
    apk_or_csv__apk.place_forget()
    normal_brawlers__apk.place(x=130, y=540)
    normal_brawlers__apk.config(command=lambda: result_have_normal_brawlers_only())
    custom_brawlers__apk.place(x=990, y=540)
    custom_brawlers__apk.config(command=lambda: result_have_custom_brawlers())
    ProgramStoppedResponding.place(x=930, y=240, anchor=tk.CENTER)


def result_have_normal_brawlers_only():
    global chosen_option
    chosen_option = 3
    global csv_logic_path
    global csv_localization_path
    ProgramStoppedResponding.place_forget()
    normal_brawlers__apk.place_forget()
    custom_brawlers__apk.place_forget()
    if not os.path.exists(os.path.join(current_path, multibrawl_classic_name + ".apk")) and not os.path.exists(os.path.join(current_path, multibrawl_classic_name + ".zip")):
        mega.download_url(multibrawl_classic_link)
    if not os.path.exists(os.path.join(current_path, multibrawl_classic_name + ".zip")):
        os.rename(os.path.join(current_path, multibrawl_classic_name + ".apk"), multibrawl_classic_name + ".zip")
    if os.path.exists(os.path.join(current_path, multibrawl_classic_name + "/assets/csv_logic")):
        shutil.rmtree(os.path.join(current_path, multibrawl_classic_name))
    with ZipFile(multibrawl_classic_name + ".zip", 'r') as zip:
        zip.extractall(os.path.join(current_path, multibrawl_classic_name))
        csv_logic_path = multibrawl_classic_name + "/assets/csv_logic"
        csv_localization_path = multibrawl_classic_name + "/assets/localization"
        set_brawler_texts_csv_1()


def result_have_custom_brawlers():
    global chosen_option
    chosen_option = 2
    global csv_logic_path
    global csv_localization_path
    ProgramStoppedResponding.place_forget()
    normal_brawlers__apk.place_forget()
    custom_brawlers__apk.place_forget()
    if not os.path.exists(os.path.join(current_path, multibrawl_mod_name + ".apk")) and not os.path.exists(os.path.join(current_path, multibrawl_mod_name + ".zip")):
        print(os.path.join(current_path, multibrawl_mod_name + ".apk"))
        print(os.path.join(current_path, multibrawl_mod_name + ".zip"))
        mega.download_url(multibrawl_mod_link)
    if not os.path.exists(os.path.join(current_path, multibrawl_mod_name + ".zip")):
        os.rename(os.path.join(current_path, multibrawl_mod_name + ".apk"), multibrawl_mod_name + ".zip")
        print(os.path.join(current_path, multibrawl_mod_name + ".zip"))
    elif os.path.exists(os.path.join(current_path, multibrawl_mod_name + "/assets/csv_logic")):
        print(os.path.join(current_path, multibrawl_mod_name + "/assets/csv_logic"))
        shutil.rmtree(os.path.join(current_path, multibrawl_mod_name))
    with ZipFile(multibrawl_mod_name + ".zip", 'r') as zip:
        zip.extractall(os.path.join(current_path, multibrawl_mod_name))
        csv_logic_path = multibrawl_mod_name + "/assets/csv_logic"
        csv_localization_path = multibrawl_mod_name + "/assets/localization"
        set_brawler_texts_csv_1()


def get_csv_manually():
    global chosen_option
    chosen_option = 1
    apk_or_csv__csv.place_forget()
    apk_or_csv__apk.place_forget()
    openFolder.pack()
    openFolder.place(x=960, y=540, anchor=tk.CENTER)


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
        openLocalization.place(x=960, y=540, anchor=tk.CENTER)
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
    brawlerNameButton.place(x=100, y=250)
    brawlerNameButton.config(command=lambda: hide_button_1(brawlerNameButton))
    text_entry1.place(x=100, y=200)
    brawlerDescriptionButton.place(x=1000, y=250)
    brawlerDescriptionButton.config(command=lambda: hide_button_1(brawlerDescriptionButton))
    text_entry2.place(x=1000, y=200)
    brawlerAttackName.place(x=100, y=550)
    brawlerAttackName.config(command=lambda: hide_button_1(brawlerAttackName))
    text_entry3.place(x=100, y=500)
    brawlerAttackDescription.place(x=100, y=750)
    brawlerAttackDescription.config(command=lambda: hide_button_1(brawlerAttackDescription))
    text_entry4.place(x=100, y=700)
    brawlerUltiName.place(x=1000, y=550)
    brawlerUltiName.config(command=lambda: hide_button_1(brawlerUltiName))
    text_entry5.place(x=1000, y=500)
    brawlerUltiDescription.place(x=1000, y=750)
    brawlerUltiDescription.config(command=lambda: hide_button_1(brawlerUltiDescription))
    text_entry6.place(x=1000, y=700)


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
    brawlerRarityCommon.place(x=300, y=150)
    brawlerRarityCommon.config(command=lambda: set_brawler_cards_csv("common"))
    brawlerRarityRare.place(x=300, y=550)
    brawlerRarityRare.config(command=lambda: set_brawler_cards_csv("rare"))
    brawlerRaritySuperRare.place(x=800, y=550)
    brawlerRaritySuperRare.config(command=lambda: set_brawler_cards_csv("super_rare"))
    brawlerRarityEpic.place(x=1300, y=550)
    brawlerRarityEpic.config(command=lambda: set_brawler_cards_csv("epic"))
    brawlerRarityMythic.place(x=800, y=150)
    brawlerRarityMythic.config(command=lambda: set_brawler_cards_csv("mega_epic"))
    brawlerRarityLegendary.place(x=1300, y=150)
    brawlerRarityLegendary.config(command=lambda: set_brawler_cards_csv("legendary"))


def set_brawler_cards_csv(rarity):
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
    brawlerSpeedButton.place(x=100, y=250)
    brawlerSpeedButton.config(command=lambda: hide_button_1(brawlerSpeedButton))
    text_entry1.place(x=100, y=200)
    brawlerHealthButton.place(x=1000, y=250)
    brawlerHealthButton.config(command=lambda: hide_button_1(brawlerHealthButton))
    text_entry2.place(x=1000, y=200)
    brawlerScaleButton.place(x=100, y=550)
    brawlerScaleButton.config(command=lambda: hide_button_1(brawlerScaleButton))
    text_entry3.place(x=100, y=500)
    brawlerIconButton.place(x=100, y=750)
    brawlerIconButton.config(command=lambda: hide_button_1(brawlerIconButton))
    text_entry4.place(x=100, y=700)


def set_brawler_characters_csv_2():
    global capbrawlername
    global speed
    global hp
    global icon
    global scale
    speed = text_entry1.get()
    hp = text_entry2.get()
    scale = text_entry3.get()
    icon = text_entry4.get()
    ultichargemul = random.randint(80, 135)
    ultichargeultimul = random.randint(85, 150)
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
    MainAttackNextButton.place(x=500, y=350)
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
    brawlerAttackRange.place(x=100, y=150)
    brawlerAttackRange.config(command=lambda: hide_button_1(brawlerAttackRange))
    text_entry1.place(x=100, y=100)
    brawlerAttackProjectile.place(x=1000, y=250)
    brawlerAttackProjectile.config(command=lambda: show_attack_or_ulti_buttons())
    text_entry2.place(x=1000, y=200)
    brawlerAttackProjectileNumber.place(x=100, y=550)
    brawlerAttackProjectileNumber.config(command=lambda: hide_button_1(brawlerAttackProjectileNumber))
    text_entry5.place(x=100, y=500)
    brawlerAttackDamage.place(x=1000, y=750)
    brawlerAttackDamage.config(command=lambda: hide_button_1(brawlerAttackDamage))
    text_entry6.place(x=1000, y=700)
    brawlerAttackReloadTime.place(x=1000, y=550)
    brawlerAttackReloadTime.config(command=lambda: hide_button_1(brawlerAttackReloadTime))
    text_entry7.place(x=1000, y=500)
    brawlerAttackAmmoNumber.place(x=50, y=750)
    brawlerAttackAmmoNumber.config(command=lambda: hide_button_1(brawlerAttackAmmoNumber))
    text_entry8.place(x=50, y=700)
    brawlerAttackSpread.place(x=100, y=350)
    brawlerAttackSpread.config(command=lambda: hide_button_1(brawlerAttackSpread))
    text_entry9.place(x=100, y=300)


def show_attack_or_ulti_buttons():
    brawlerAttackProjectile.place_forget()
    text_entry2.place_forget()
    brawlerAttackProjectileAttackOrUlti_Attack.place(x=1000, y=250)
    brawlerAttackProjectileAttackOrUlti_Attack.config(command=lambda: set_attack_projectile_ulti_or_attack(1))
    brawlerAttackProjectileAttackOrUlti_Super.place(x=1000, y=350)
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
    if projectile == "shelly":
        projectiles = "ShotgunGirl"
    elif projectile == "colt":
        projectiles = "Gunslinger"
    elif projectile == "bull":
        projectiles = "BullDude"
    elif projectile == "brock":
        projectiles = "RocketGirl"
    elif projectile == "rico":
        projectiles = "TrickshotDude"
    elif projectile == "spike":
        projectiles = "CactusDude"
    elif projectile == "barley":
        projectiles = "Barkeep"
    elif projectile == "jessie":
        projectiles = "Mechanic"
    elif projectile == "nita":
        projectiles = "Shaman"
    elif projectile == "dynamike":
        projectiles = "TntDude"
    elif projectile == "el_primo":
        projectiles = "Luchador"
    elif projectile == "mortis":
        projectiles = "Undertaker"
    elif projectile == "crow":
        projectiles = "Crow"
    elif projectile == "poco":
        projectiles = "DeadMariachi"
    elif projectile == "bo":
        projectiles = "BowDude"
    elif projectile == "piper":
        projectiles = "Sniper"
    elif projectile == "pam":
        projectiles = "MinigunDude"
    elif projectile == "tara":
        projectiles = "BlackHole"
    elif projectile == "darryl":
        projectiles = "BarrelBot"
    elif projectile == "penny":
        projectiles = "ArtilleryDude"
    elif projectile == "frank":
        projectiles = "HammerDude"
    elif projectile == "gene":
        projectiles = "HookDude"
    elif projectile == "tick":
        projectiles = "ClusterBombDude"
    elif projectile == "leon":
        projectiles = "Ninja"
    elif projectile == "rosa":
        projectiles = "Rosa"
    elif projectile == "carl":
        projectiles = "Whirlwind"
    elif projectile == "bibi":
        projectiles = "Baseball"
    elif projectile == "eight_bit":
        projectiles = "Arcade"
    elif projectile == "sandy":
        projectiles = "Sandstorm"
    elif projectile == "bea":
        projectiles = "BeeSniper"
    elif projectile == "emz":
        projectiles = "Mummy"
    elif projectile == "mister_p":
        projectiles = "SpawnerDude"
    elif projectile == "max":
        projectiles = "Speedy"
    elif projectile == "jacky":
        projectiles = "Driller"
    elif projectile == "gale":
        projectiles = "Blower"
    elif projectile == "nani":
        projectiles = "Controller"
    elif projectile == "sprout":
        projectiles = "Wally"
    elif projectile == "surge":
        projectiles = "PowerLeveler"
    elif projectile == "colette":
        projectiles = "Percenter"
    global numberofprojectiles
    numberofprojectiles = text_entry5.get()
    global damage
    damage = text_entry6.get()
    global reloadtime
    reloadtime = text_entry7.get()
    global ammonumber
    ammonumber = text_entry8.get()
    global spread
    spread = text_entry9.get()
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
    brawlerSuperRange.place(x=100, y=150)
    brawlerSuperRange.config(command=lambda: hide_button_1(brawlerSuperRange))
    text_entry1.place(x=100, y=100)
    brawlerSuperProjectile.place(x=1000, y=350)
    brawlerSuperProjectile.config(command=lambda: show_attack_or_ulti_buttons_super())
    text_entry2.place(x=1000, y=300)
    brawlerSuperProjectileNumber.place(x=100, y=550)
    brawlerSuperProjectileNumber.config(command=lambda: hide_button_1(brawlerSuperProjectileNumber))
    text_entry5.place(x=100, y=500)
    brawlerSuperDamage.place(x=1000, y=750)
    brawlerSuperDamage.config(command=lambda: hide_button_1(brawlerSuperDamage))
    text_entry6.place(x=1000, y=700)
    brawlerSuperSpread.place(x=100, y=350)
    brawlerSuperSpread.config(command=lambda: hide_button_1(brawlerSuperSpread))
    text_entry9.place(x=100, y=300)


def show_attack_or_ulti_buttons_super():
    brawlerSuperProjectile.place_forget()
    text_entry2.place_forget()
    brawlerSuperProjectileAttackOrUlti_Attack.place(x=1000, y=250)
    brawlerSuperProjectileAttackOrUlti_Attack.config(command=lambda: set_attack_projectile_ulti_or_attack_super(1))
    brawlerSuperProjectileAttackOrUlti_Super.place(x=1000, y=350)
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
    if projectile == "shelly":
        projectiles = "ShotgunGirl"
    elif projectile == "colt":
        projectiles = "Gunslinger"
    elif projectile == "bull":
        projectiles = "BullDude"
    elif projectile == "brock":
        projectiles = "RocketGirl"
    elif projectile == "rico":
        projectiles = "TrickshotDude"
    elif projectile == "spike":
        projectiles = "CactusDude"
    elif projectile == "barley":
        projectiles = "Barkeep"
    elif projectile == "jessie":
        projectiles = "Mechanic"
    elif projectile == "nita":
        projectiles = "Shaman"
    elif projectile == "dynamike":
        projectiles = "TntDude"
    elif projectile == "el_primo":
        projectiles = "Luchador"
    elif projectile == "mortis":
        projectiles = "Undertaker"
    elif projectile == "crow":
        projectiles = "Crow"
    elif projectile == "poco":
        projectiles = "DeadMariachi"
    elif projectile == "bo":
        projectiles = "BowDude"
    elif projectile == "piper":
        projectiles = "Sniper"
    elif projectile == "pam":
        projectiles = "MinigunDude"
    elif projectile == "tara":
        projectiles = "BlackHole"
    elif projectile == "darryl":
        projectiles = "BarrelBot"
    elif projectile == "penny":
        projectiles = "ArtilleryDude"
    elif projectile == "frank":
        projectiles = "HammerDude"
    elif projectile == "gene":
        projectiles = "HookDude"
    elif projectile == "tick":
        projectiles = "ClusterBombDude"
    elif projectile == "leon":
        projectiles = "Ninja"
    elif projectile == "rosa":
        projectiles = "Rosa"
    elif projectile == "carl":
        projectiles = "Whirlwind"
    elif projectile == "bibi":
        projectiles = "Baseball"
    elif projectile == "eight_bit":
        projectiles = "Arcade"
    elif projectile == "sandy":
        projectiles = "Sandstorm"
    elif projectile == "bea":
        projectiles = "BeeSniper"
    elif projectile == "emz":
        projectiles = "Mummy"
    elif projectile == "mister_p":
        projectiles = "SpawnerDude"
    elif projectile == "max":
        projectiles = "Speedy"
    elif projectile == "jacky":
        projectiles = "Driller"
    elif projectile == "gale":
        projectiles = "Blower"
    elif projectile == "nani":
        projectiles = "Controller"
    elif projectile == "sprout":
        projectiles = "Wally"
    elif projectile == "surge":
        projectiles = "PowerLeveler"
    elif projectile == "colette":
        projectiles = "Percenter"
    global numberofprojectiles
    numberofprojectiles = text_entry5.get()
    global damage
    damage = text_entry6.get()
    global reloadtime
    reloadtime = text_entry7.get()
    global ammonumber
    ammonumber = text_entry8.get()
    global spread
    spread = text_entry9.get()
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
        ProgramFinished.place(x=600, y=500)
    elif chosen_option == 2:
        if os.path.exists(os.path.join(current_path, multibrawl_mod_name + " - Brawler Maker")):
            shutil.rmtree(os.path.join(current_path, multibrawl_mod_name + " - Brawler Maker"))
        os.rename(os.path.join(current_path, multibrawl_mod_name), multibrawl_mod_name + " - Brawler Maker")
        if os.path.exists(os.path.join(current_path, multibrawl_mod_name + " - Brawler Maker" + ".zip")):
            os.remove(os.path.join(current_path, multibrawl_mod_name + " - Brawler Maker" + ".zip"))
        if os.path.exists(os.path.join(current_path, multibrawl_mod_name.replace(' ', '-') + "-BrawlerMaker" + ".apk")):
            os.remove(os.path.join(current_path, multibrawl_mod_name.replace(' ', '-') + "-BrawlerMaker" + ".apk"))
        shutil.make_archive(multibrawl_mod_name + " - Brawler Maker", "zip", os.path.join(current_path, multibrawl_mod_name + " - Brawler Maker"))
        os.rename(os.path.join(current_path, multibrawl_mod_name + " - Brawler Maker" + ".zip"), multibrawl_mod_name.replace(' ', '-') + "-BrawlerMaker" + ".apk")
        os.system('java -jar ' + current_path + '/uber-apk-signer.jar -a ' + current_path + "/" + multibrawl_mod_name.replace(' ', '-') + '-BrawlerMaker' + '.apk' + ' --debug')
        ProgramFinished.place(x=600, y=500)
    elif chosen_option == 3:
        if os.path.exists(os.path.join(current_path, multibrawl_classic_name + " - Brawler Maker")):
            shutil.rmtree(os.path.join(current_path, multibrawl_classic_name + " - Brawler Maker"))
        os.rename(os.path.join(current_path, multibrawl_classic_name), multibrawl_classic_name + " - Brawler Maker")
        if os.path.exists(os.path.join(current_path, multibrawl_classic_name + " - Brawler Maker" + ".zip")):
            os.remove(os.path.join(current_path, multibrawl_classic_name + " - Brawler Maker" + ".zip"))
        if os.path.exists(os.path.join(current_path, multibrawl_classic_name.replace(' ', '-') + "-BrawlerMaker" + ".apk")):
            os.remove(os.path.join(current_path, multibrawl_classic_name.replace(' ', '-') + "-BrawlerMaker" + ".apk"))
        shutil.make_archive(multibrawl_classic_name + " - Brawler Maker", "zip", os.path.join(current_path, multibrawl_classic_name + " - Brawler Maker"))
        os.rename(os.path.join(current_path, multibrawl_classic_name + " - Brawler Maker" + ".zip"), multibrawl_classic_name.replace(' ', '-') + "-BrawlerMaker" + ".apk")
        os.system('java -jar ' + current_path + '/uber-apk-signer.jar -a ' + current_path + "/" + multibrawl_classic_name.replace(' ', '-') + '-BrawlerMaker' + '.apk' + " --debug")
        ProgramFinished.place(x=600, y=500)


canvas = tk.Canvas(root, height=1080, width=1920)
canvas.pack()

rebrawlModsWarning = tk.Label(root, text="Apks Provided by MultiBrawl ! Works only for v29 servers !",
                              font=("Times", 20, "bold"), fg="red")
rebrawlModsWarning.pack
rebrawlModsWarning.place(x=0, y=0)

ProgramFinished = tk.Label(root, text="Your Folders are Ready !", font=("Times", 40, "bold"), fg="black")
startButton = tk.Button(root, text="Start", font=("Times", 40, "bold"), fg="black")
startButton.pack
startButton.place(x=960, y=540, anchor=tk.CENTER)
startButton.config(command=lambda: start_button())

ProgramStoppedResponding = tk.Label(root, text="Program may stop responding here and at the end of the script. (Speed depends on your wifi and your computer)", font=("Times", 25, "bold"), fg="black")

apk_or_csv__apk = tk.Button(root, text="Get Csv Automatically", font=("Times", 40, "bold"), fg="black")
apk_or_csv__csv = tk.Button(root, text="Choose Csv Manually", font=("Times", 40, "bold"), fg="black")

normal_brawlers__apk = tk.Button(root, text="Result includes only normal brawlers ?", font=("Times", 30, "bold"), fg="black")
custom_brawlers__apk = tk.Button(root, text="Result includes other modded brawlers ?", font=("Times", 30, "bold"), fg="black")

openFolder = tk.Button(root, text="Open CSV Logic Folder", font=("Times", 40, "bold"), fg="black", command=csv_logic_path_selector)
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

common_rarity_image = tk.PhotoImage(file='images/common_rarity.gif')
rare_rarity_image = tk.PhotoImage(file='images/rare_rarity.gif')
super_rare_rarity_image = tk.PhotoImage(file='images/super_rare_rarity.gif')
epic_rarity_image = tk.PhotoImage(file='images/epic_rarity.gif')
mythic_rarity_image = tk.PhotoImage(file='images/mythic_rarity.gif')
legendary_rarity_image = tk.PhotoImage(file='images/legendary_rarity.gif')

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
                                    text="From what Brawler do you the projectile from \n(brawler name no cap)\n(exeptions : 8bit = eight_bit, primo = el_primo \nand mr.P = mister_p)",
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
                                   text="From what Brawler do you the projectile from \n(brawler name no cap)\n(exeptions : 8bit = eight_bit, primo = el_primo \nand mr.P = mister_p)",
                                   font=("Times", 20, "bold"))
brawlerSuperProjectileAttackOrUlti_Attack = tk.Button(root, text="Do you want his/her main attack projectile)",
                                                      font=("Times", 20, "bold"))
brawlerSuperProjectileAttackOrUlti_Super = tk.Button(root, text="Do  you want his/her super's projectile",
                                                     font=("Times", 20, "bold"))

root.mainloop()
