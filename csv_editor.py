import csv
import random

brawlername = str(input("What is the name of you Brawler ? : "))
version = int(input('Which BS do you use ?(input only the number)(1-Real_BS 2-Rebrawl) ? : '))
def update_skills_csv_file():
    csv_writer = csv.writer(open('skills.csv', 'a'), delimiter=',')
    if version == 2:
        attacktype = int(input("What type of attack do you want ? (1-Normal 2-Charge 3-Spawnable) ? : "))
        ammo_or_super = int(input("Is it an ammo or a super (1-Ammo 2-Super) ? : "))
        if attacktype == 1:
            attackduration = int(input("Duration of the attack (in miliseconds) (rosa's duration let 3 punches for example and default is 150) : "))
            range = int(input("Range of the attack (primo is 9 and rico is 29) : "))
            if ammo_or_super == 1:
                reloadtime = int(input("How long for a brawler to reload an ammo (in miliseconds) : "))
                ammonumber = int(input("How many ammo (1-4) : "))
                weapon_or_ulti = "Weapon"
            else:
                reloadtime = ''
                ammonumber = ''
                weapon_or_ulti = "Ulti"
            damage = int(input("How much damage for each projectile ? : "))
            timebetweenattacks = int(input("How much time between each attacks ? (in milliseconds)(colonel ruff have a small one and default is 100) ? : "))
            spread = str(input("How much spread ? (shelly is 60 and poco is 130 and nita 0) ? : "))
            attackpatern = int(input("What attack patern (1 is by default but you can search for more information of the others) ? : "))
            numberofprojectiles = int(input("How much projectiles do you want in one ammo ? : "))
            projectile = str(input("Wich projectile do you want ? (from projectiles.csv) ? : "))
            csv_writer.writerow([brawlername + weapon_or_ulti, 'Attack', 'true', 'true', 'true', '', '50', attackduration, '', range, '', '', '', '', reloadtime, ammonumber, damage, '', timebetweenattacks, spread, attackpatern, numberofprojectiles, '', 'true', '', '', '', '', '', '', '', '', projectile, '', '', '', '', '', '', '', '', 'sc/ui.sc', 'rapid_fire_button', 'rico_def_atk', '', '', '', '', '', '', '', '', '', '', '', ''])
        elif attacktype == 2:
            nombrawler = str(input("Name of the Brawler : "))
            range = int(input("Range of the attack (primo is 9 and rico is 29) : "))
            if ammo_or_super == 1:
                reloadtime = int(input("How long for a brawler to reload an ammo (in miliseconds) : "))
                ammonumber = int(input("How many ammo (1-4) : "))
            else:
                reloadtime = ''
                ammonumber = ''
                weapon_or_ulti = "Ulti"
            damage = int(input("How much damage for each projectile ? : "))
            chargepushback = int(input("How much knockback for the charge (primo is 130) ? : "))
            chargespeed = int(input("How much speed for the charge ? (primo is 1600 and mortis 2700) ? : "))
            chargetype = int(input("Which charge type do you want (search yourself for more info) ? : "))
            csv_writer.writerow([nombrawler + weapon_or_ulti, 'Charge', '', 'true', 'true', '', '50', '', '', range, '', '', '', '', reloadtime, ammonumber, damage, '', '', '', '', '', '', '', chargepushback, chargespeed, chargetype, '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'sc/ui.sc', 'charge_button', 'luchador_ulti', '', '', '', '', '', '', '', '', '', '', '', ''])
        elif attacktype == 3:
            nombrawler = str(input("Name of the Brawler : "))
            attackduration = int(input("Duration of the attack (in miliseconds) (rosa's duration let 3 punches for example and default is 150) : "))
            range = int(input("Range of the attack (primo is 9 and rico is 29) : "))
            if ammo_or_super == 1:
                reloadtime = int(input("How long for a brawler to reload an ammo (in miliseconds) : "))
                ammonumber = int(input("How many ammo (1-4) : "))
                weapon_or_ulti = "Weapon"
            else:
                reloadtime = ''
                ammonumber = ''
                weapon_or_ulti = "Ulti"
            numberofprojectiles = int(input("How much spawnables do you want in one ammo ? : "))
            timebetweenattacks = int(input("How much time between each attacks ? (in milliseconds)(colonel ruff have a small one and default is 100) ? : "))
            maxspawnables = int(input("What is the max number of spawnables that can you have at the same times ? : "))
            projectile = str(input("Wich projectile do you want ? (from projectiles.csv) ? :"))
            petname = str(input("What is the name of the spawnable (from characters.csv) ? : "))
            csv_writer.writerow([nombrawler + weapon_or_ulti, 'Attack', 'true', 'true', 'true', '', '50', attackduration, '', range, '', '', '', '', reloadtime, ammonumber, '', '', timebetweenattacks, '', '', '', '', 'true', '', '', '', numberofprojectiles, maxspawnables, '', '', '', projectile, petname, '', '', '', '', '', '', '', 'sc/ui.sc', 'turret_button', 'rico_def_atk', '', '', '', '', '', '', '', '', '', '', '', ''])


def update_cards_csv_file():
    if version == 2:
        csv_writer = csv.writer(open('cards.csv', 'a'), delimiter=',')
        rarity = str(input("What is the rarity of you brawler (common or rare or super_rare or epic or mega_epic or legendary) (mega_epic is mythic) ? : "))
        brawlernumber = random.randint(1500, 9999)
        csv_writer.writerow([brawlername + '_unlock', 'sc/ui.sc', '', brawlername, '', '', '0', '', 'unlock', '', '', '', '', rarity, '', '', '', '', '', '', brawlernumber, '', ''])
        csv_writer.writerow([brawlername + '_hp', 'sc/ui.sc', 'health_icon', brawlername, '', '', '1', '', 'hp', '', '', '', '', 'common', 'TID_ARMOR', 'TID_ARMOR', '', '', 'genicon_health', '', '', '', ''])
        csv_writer.writerow([brawlername + '_abi', 'sc/ui.sc', 'attack_icon', brawlername, '', '', '2', '', 'abi', '', '', '', '', 'common', 'TID_ARMOR', 'TID_ARMOR', '', '', 'genicon_damage', '', '', '', ''])
        csv_writer.writerow([brawlername + '_ulti', 'sc/ui.sc', 'ulti_icon', brawlername, '', '', '3', '', 'ulti', '', '', '', '', 'common', 'TID_ARMOR', 'TID_ARMOR', '', '', 'genicon_damage', '', '', '', ''])
        csv_writer.writerow([brawlername + '_unique', 'sc/ui.sc', '', brawlername, '', '', '4', '', 'freeze', '', '60', '350', '', 'common', 'TID_ARMOR', '', '', '', 'genicon_health', '', '', '', ''])
        csv_writer.writerow([brawlername + 'Gadget', 'sc/ui.sc', 'icon_item_8bit_1', brawlername, '', '', '5', '', 'accessory', 'Crow_Shield', '0', '', '', 'common', 'TID_ARMOR', '', '', '', 'genicon_health', '', '', '', ''])


def update_characters_csv_file():
    if version == 2:
        csv_writer = csv.writer(open('characters.csv', 'a'), delimiter=',')
        pet = str(input("If you had a pet please re-enter it's name, if you don't just press enter key : "))
        speed = int(input("Please enter you brawler's speed (normal is 720, tank is 770 and speed is 820) ? : "))
        hp = int(input("How much hp do you want ? : "))
        ultichargemul = random.randint(80, 135)
        ultichargeultimul = random.randint(85, 150)
        scale = int(input("Wich scale do you want your brawler to be at (default is 116) ? : "))
        doesautoultcharge = int(input("Do you want your super to auto charge ? (1 = Yes and 2 = No) ? : "))
        if doesautoultcharge == 1:
            autoultcharge = int(input("At what speed (darryl is 33) ? : "))
        else:
            autoultcharge = ""
        csv_writer.writerow([brawlername, '', '', 'bull', brawlername + 'Weapon', brawlername + 'Ulti', pet, speed, hp, '', '', '', '', '', '', '', '12', '', ultichargemul, ultichargeultimul, "Hero", '', brawlername + 'Default', '', '', '', '', '', '', 'takedamage_gen', 'death_shotgun_girl', 'Gen_move_fx', 'reload_shotgun_girl', 'No_ammo_shotgungirl', 'Dry_fire_shotgungirl', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '30', '', '80', '80', '', '', '35', scale, '210', '284', '90', '175', '260', '', '', '', '-25', '40', '120', 'Medium', '-48', '', '450', '', '', 'TID_SHOTGUN_GIRL_BUFF', '', 'sc/ui.sc', 'hero_icon_shelly', '0', 'human', 'footstep', '25', '250', '200', '', '', '1', '3', '2', '', '', '', '', '', '', '', '', autoultcharge, '', '', '', '', '', '', '3', '3', '3'])

def update_skins_csv_file():
    if version == 2:
        csv_writer = csv.writer(open('skins.csv', 'a'), delimiter=',')
        csv_writer.writerow([brawlername + 'Default', brawlername + 'Default', '', '', '', '', '', '', '', '', '', '', '', '', '', 'shelly_v2_01.pvr', 'shelly_v2_01.pvr', 'shelly_v2_01.pvr', 'shelly_v2_01.pvr'])
        csv_writer = csv.writer(open('skin_confs.csv', 'a'), delimiter=',')
        csv_writer.writerow([brawlername + 'Default',brawlername,'shelly_geo.scw', '', '','shelly_base_cam.scw','shelly_intro_pose.scw', '','ShellyIdle','ShellyWalk','ShellyPrimary','ShellySecondary','ShellyRecoil', '','ShellyRecoil', '','ShellyReload','ShellyPushback','ShellyWin','ShellyWinloop','ShellyLose','ShellyLoseloop','ShellyIdle','ShellyWin','ShellyWinloop','ShellyWin','ShellyIdle','ShellyIdle','ShellyProfile','ShellyIntro', '', '', '', '','ShellyFace','ShellyFace','ShellyHappy','ShellyFace','ShellySad','ShellySadLoop','ShellyFace','ShellyHappy','ShellyFace','ShellyHappy','ShellyStill','ShellyStill', '', '', '','true','true', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ', '', ', '', '', '', ''])
if __name__ == "__main__":
    creationtype = int(input("What do you want to create (1-attack/super 2-Brawler) ? : "))
    if creationtype == 1:
        update_skills_csv_file()
        print("Done adding the skill")
    elif creationtype == 2:
        update_cards_csv_file()
        update_characters_csv_file()
        update_skins_csv_file()
        print("Done creating Brawler")
    print(" ")
