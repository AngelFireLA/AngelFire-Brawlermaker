import csv
import random


brawlername = str(input("What is the name of you Brawler ? : "))
version = int(input('Which BS do you use ?(input only the number)(1-Not Avaible 2-Rebrawl) ? : '))
def update_skills_csv_file_1():
    csv_writer = csv.writer(open('csv_logic/skills.csv', 'a'), delimiter=',')
    if version == 2:
        print("Creating main attack")
        attacktype = int(input("What type of attack do you want ? (1-Normal 2-Charge 3-Spawnable) ? : "))
        if attacktype == 1:
            attackduration = int(input("Duration of the attack (in miliseconds) (rosa's duration let 3 punches for example and default is 150) : "))
            range = int(input("Range of the attack (primo is 9 and rico is 29) : "))
            reloadtime = int(input("How long for a brawler to reload an ammo (in miliseconds) : "))
            ammonumber = int(input("How many ammo (1-4) : "))
            weapon_or_ulti = "Weapon"
            damage = int(input("How much damage for each projectile ? : "))
            timebetweenattacks = int(input("How much time between each attacks ? (in milliseconds)(colonel ruff have a small one and default is 100) ? : "))
            spread = str(input("How much spread ? (shelly is 60 and poco is 130 and nita 0) ? : "))
            attackpatern = int(input("What attack patern (1 is by default but you can search for more information of the others) ? : "))
            numberofprojectiles = int(input("How much projectiles do you want in one ammo ? : "))
            projectile = str(input("Projectile : Enter name of brawler that you want the projctile off (exeptions : 8bit = eight_bit, primo = el_primo and mr.P = mister_p)? : "))
            if projectile == "shelly":
                projectiles = "ShotGunGirl"
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
            superorattackprojectile = input("Projectile for attack or super ?")
            if superorattackprojectile == 1 or superorattackprojectile == "attack":
                projectiletype = "Projectile"
            elif superorattackprojectile == 2 or superorattackprojectile == "super":
                projectiletype = "UltiProjectile"
            csv_writer.writerow([brawlername + weapon_or_ulti, 'Attack', 'true', 'true', 'true', '', '50', attackduration, '', range, '', '', '', '', reloadtime, ammonumber, damage, '', timebetweenattacks, spread, attackpatern, numberofprojectiles, '', 'true', '', '', '', '', '', '', '', '', projectiles + projectiletype, '', '', '', '', '', '', '', '', 'sc/ui.sc', 'rapid_fire_button', 'rico_def_atk', '', '', '', '', '', '', '', '', '', '', '', ''])
        elif attacktype == 2:
            nombrawler = str(input("Name of the Brawler : "))
            range = int(input("Range of the attack (primo is 9 and rico is 29) : "))
            reloadtime = int(input("How long for a brawler to reload an ammo (in miliseconds) : "))
            ammonumber = int(input("How many ammo (1-4) : "))
            weapon_or_ulti = "Weapon"
            damage = int(input("How much damage for each projectile ? : "))
            chargepushback = int(input("How much knockback for the charge (primo is 130) ? : "))
            chargespeed = int(input("How much speed for the charge ? (primo is 1600 and mortis 2700) ? : "))
            chargetype = int(input("Which charge type do you want (search yourself for more info) ? : "))
            csv_writer.writerow([nombrawler + weapon_or_ulti, 'Charge', '', 'true', 'true', '', '50', '', '', range, '', '', '', '', reloadtime, ammonumber, damage, '', '', '', '', '', '', '', chargepushback, chargespeed, chargetype, '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'sc/ui.sc', 'charge_button', 'luchador_ulti', '', '', '', '', '', '', '', '', '', '', '', ''])
        elif attacktype == 3:
            nombrawler = str(input("Name of the Brawler : "))
            attackduration = int(input("Duration of the attack (in miliseconds) (rosa's duration let 3 punches for example and default is 150) : "))
            range = int(input("Range of the attack (primo is 9 and rico is 29) : "))
            reloadtime = int(input("How long for a brawler to reload an ammo (in miliseconds) : "))
            ammonumber = int(input("How many ammo (1-4) : "))
            weapon_or_ulti = "Weapon"
            numberofprojectiles = int(input("How much spawnables do you want in one ammo ? : "))
            timebetweenattacks = int(input("How much time between each attacks ? (in milliseconds)(colonel ruff have a small one and default is 100) ? : "))
            maxspawnables = int(input("What is the max number of spawnables that can you have at the same times ? : "))
            projectile = str(input("Projectile : Enter name of brawler that you want the projctile off (exeptions : 8bit = eight_bit, primo = el_primo and mr.P = mister_p)? : "))
            if projectile == "shelly":
                projectiles = "ShotGunGirl"
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
            superorattackprojectile = int(input("Projectile for attack or super ?"))
            if superorattackprojectile == 1:
                projectiletype = "Projectile"
            elif superorattackprojectile == 2:
                projectiletype = "UltiProjectile"
            petname = str(input("What is the name of the spawnable (from characters.csv) ? : "))
            csv_writer.writerow([nombrawler + weapon_or_ulti, 'Attack', 'true', 'true', 'true', '', '50', attackduration, '', range, '', '', '', '', reloadtime, ammonumber, '', '', timebetweenattacks, '', '', '', '', 'true', '', '', '', numberofprojectiles, maxspawnables, '', '', '', projectiles + projectiletype, petname, '', '', '', '', '', '', '', 'sc/ui.sc', 'turret_button', 'rico_def_atk', '', '', '', '', '', '', '', '', '', '', '', ''])


def update_skills_csv_file_2():
    csv_writer = csv.writer(open('csv_logic/skills.csv', 'a'), delimiter=',')
    if version == 2:
        print("Creating Super")
        attacktype = int(input("What type of attack do you want ? (1-Normal 2-Charge 3-Spawnable) ? : "))
        if attacktype == 1:
            attackduration = int(input("Duration of the attack (in miliseconds) (rosa's duration let 3 punches for example and default is 150) : "))
            range = int(input("Range of the attack (primo is 9 and rico is 29) : "))
            reloadtime = ''
            ammonumber = ''
            weapon_or_ulti = "Ulti"
            damage = int(input("How much damage for each projectile ? : "))
            timebetweenattacks = int(input("How much time between each attacks ? (in milliseconds)(colonel ruff have a small one and default is 100) ? : "))
            spread = str(input("How much spread ? (shelly is 60 and poco is 130 and nita 0) ? : "))
            attackpatern = int(input("What attack patern (1 is by default but you can search for more information of the others) ? : "))
            numberofprojectiles = int(input("How much projectiles do you want in one ammo ? : "))
            projectile = str(input("Projectile : Enter name of brawler that you want the projctile off (exeptions : 8bit = eight_bit, primo = el_primo and mr.P = mister_p)? : "))
            if projectile == "shelly":
                projectiles = "ShotGunGirl"
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
            superorattackprojectile = int(input("Projectile for 1-attack or 2-super ?"))
            if superorattackprojectile == 1:
                projectiletype = "Projectile"
            elif superorattackprojectile == 2:
                projectiletype = "UltiProjectile"
            csv_writer.writerow([brawlername + weapon_or_ulti, 'Attack', 'true', 'true', 'true', '', '50', attackduration, '', range, '', '', '', '', reloadtime, ammonumber, damage, '', timebetweenattacks, spread, attackpatern, numberofprojectiles, '', 'true', '', '', '', '', '', '', '', '', projectiles + projectiletype, '', '', '', '', '', '', '', '', 'sc/ui.sc', 'rapid_fire_button', 'rico_def_atk', '', '', '', '', '', '', '', '', '', '', '', ''])
        elif attacktype == 2:
            nombrawler = str(input("Name of the Brawler : "))
            range = int(input("Range of the attack (primo is 9 and rico is 29) : "))
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
            reloadtime = ''
            ammonumber = ''
            weapon_or_ulti = "Ulti"
            numberofprojectiles = int(input("How much spawnables do you want in one ammo ? : "))
            timebetweenattacks = int(input("How much time between each attacks ? (in milliseconds)(colonel ruff have a small one and default is 100) ? : "))
            maxspawnables = int(input("What is the max number of spawnables that can you have at the same times ? : "))

            projectile = str(input("Projectile : Enter name of brawler that you want the projectile off (exeptions : 8bit = eight_bit, primo = el_primo and mr.P = mister_p)? : "))
            if projectile == "shelly":
                projectiles = "ShotGunGirl"
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
            superorattackprojectile = int(input("Projectile for 1-attack or 2-super ?"))
            if superorattackprojectile == 1:
                projectiletype = "Projectile"
            elif superorattackprojectile == 2:
                projectiletype = "UltiProjectile"
            petname = str(input("What is the name of the spawnable (from characters.csv) ? : "))
            csv_writer.writerow([nombrawler + weapon_or_ulti, 'Attack', 'true', 'true', 'true', '', '50', attackduration, '', range, '', '', '', '', reloadtime, ammonumber, '', '', timebetweenattacks, '', '', '', '', 'true', '', '', '', numberofprojectiles, maxspawnables, '', '', '', projectiles + projectiletype, petname, '', '', '', '', '', '', '', 'sc/ui.sc', 'turret_button', 'rico_def_atk', '', '', '', '', '', '', '', '', '', '', '', ''])

def update_cards_csv_file():
    if version == 2:
        csv_writer = csv.writer(open('csv_logic/cards.csv', 'a'), delimiter=',')
        rarity = str(input("What is the rarity of you brawler (common or rare or super_rare or epic or mega_epic or legendary) (mega_epic is mythic) ? : "))
        capbrawlername = brawlername.upper()
        brawlernumber = random.randint(1500, 9999)
        csv_writer.writerow([brawlername + '_unlock', 'sc/ui.sc', '', brawlername, '', '', '0', '', 'unlock', '', '', '', '', rarity, '', '', '', '', '', '', brawlernumber, '', ''])
        csv_writer.writerow([brawlername + '_hp', 'sc/ui.sc', 'health_icon', brawlername, '', '', '1', '', 'hp', '', '', '', '', 'common', 'TID_ARMOR', 'TID_ARMOR', '', '', 'genicon_health', '', '', '', ''])
        csv_writer.writerow([brawlername + '_abi', 'sc/ui.sc', 'attack_icon', brawlername, '', '', '2', '', 'skill', brawlername + 'Weapon', '', '', '', 'common', 'TID_' + capbrawlername + '_WEAPON', 'TID_STAT_DAMAGE', '', '', 'genicon_damage', '', '', '', ''])
        csv_writer.writerow([brawlername + '_ulti', 'sc/ui.sc', 'ulti_icon', brawlername, '', '', '3', '', 'skill', brawlername + 'Ulti', '', '', '', 'common', 'TID_' + capbrawlername + '_ULTI', 'TID_STAT_DAMAGE', '', '', 'genicon_damage', '', '', '', ''])
        csv_writer.writerow([brawlername + '_unique', 'sc/ui.sc', '', brawlername, '', '', '4', '', 'speed_low_health', '', '350', '1', '', 'common', 'TID_ARMOR', '', '', '', 'genicon_health', '', '', '', ''])
        csv_writer.writerow([brawlername + '_Gadget', 'sc/ui.sc', 'icon_item_8bit_1', brawlername, '', '', '5', '', 'accessory', 'Crow_Shield', '2', '', '', 'common', 'TID_ARMOR', '', '', '', 'genicon_health', '', '', '', ''])


def update_characters_csv_file():
    if version == 2:
        csv_writer = csv.writer(open('csv_logic/characters.csv', 'a'), delimiter=',')
        pet = str(input("If you had a pet please re-enter it's name, if you don't just press enter key : "))
        speed = int(input("Please enter you brawler's speed (normal is 720, tank is 770 and speed is 820) ? : "))
        hp = int(input("How much hp do you want ? : "))
        ultichargemul = random.randint(80, 135)
        ultichargeultimul = random.randint(85, 150)
        capbrawlername = brawlername.upper()
        icon = str(input("What brawler icon do you want (exeptions : 8bit = eight_bit, primo = el_primo and mr.P = mister_p) ? : "))
        scale = int(input("Wich scale do you want your brawler to be at (default is 116) ? : "))
        doesautoultcharge = input("Do you want your super to auto charge ? (1 = Yes and 2 = No) ? : ")
        if doesautoultcharge == 1 or doesautoultcharge == "Yes":
            autoultcharge = int(input("At what speed (darryl is 33) ? : "))
        else:
            autoultcharge = ""
        csv_writer.writerow([brawlername, '', '', 'bull', brawlername + 'Weapon', brawlername + 'Ulti', pet, speed, hp, '', '', '', '', '', '', '', '12', '', ultichargemul, ultichargeultimul, "Hero", '', brawlername + 'Default', '', '', '', '', '', '', 'takedamage_gen', 'death_shotgun_girl', 'Gen_move_fx', 'reload_shotgun_girl', 'No_ammo_shotgungirl', 'Dry_fire_shotgungirl', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '30', '', '80', '80', '', '', '35', scale, '210', '284', '90', '175', '260', '', '', '', '-25', '40', '120', 'Medium', '-48', '', '450', '', '', 'TID_' + capbrawlername, '', 'sc/ui.sc', 'hero_icon_' + icon, '0', 'human', 'footstep', '25', '250', '200', '', '', '1', '3', '2', '', '', '', '', '', '', '', '', autoultcharge, 'ShellyTutorial', '', '', '', '', '', '3', '3', '3'])

def update_skins_csv_file():
    if version == 2:
        csv_writer = csv.writer(open('csv_logic/skins.csv', 'a'), delimiter=',')
        csv_writer.writerow([brawlername + 'Default', brawlername + 'Default', '', '', '', '', '', '', '', '', '', '', '', '', '', 'shelly_v2_01.pvr', 'shelly_v2_01.pvr', 'shelly_v2_01.pvr', 'shelly_v2_01.pvr'])

def update_skin_conf_csv():
        csv_writer = csv.writer(open('csv_logic/skin_confs.csv', 'a'), delimiter=',')
        csv_writer.writerow([brawlername + 'Default', brawlername, 'shelly_geo.scw', '', '', 'shelly_base_cam.scw','shelly_intro_pose.scw', '','ShellyIdle','ShellyWalk','ShellyPrimary','ShellySecondary','ShellyRecoil', '','ShellyRecoil', '','ShellyReload','ShellyPushback','ShellyWin','ShellyWinloop','ShellyLose','ShellyLoseloop','ShellyIdle','ShellyWin','ShellyWinloop','ShellyWin','ShellyIdle','ShellyIdle','ShellyProfile','ShellyIntro', '', '', '', '', '','ShellyFace','ShellyFace','ShellyHappy','ShellyFace','ShellySad','ShellySadLoop','ShellyFace','ShellyHappy','ShellyFace','ShellyHappy','ShellyStill','ShellyStill', '', '', '','true','true', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ', '', ', '', '', '', ''])

def update_texts_csv():
    csv_writer = csv.writer(open('localization/texts.csv', 'a'), delimiter=',')
    capbrawlername = brawlername.upper()
    description = str(input("Enter your brawler's description : "))
    attack_name = str(input("Enter the Name of the Attack of your brawler : "))
    attack_description = str(input("Enter the Description of the Attack of your brawler : "))
    ulti_name = str(input("Enter the Name of the Super of your brawler : "))
    ulti_description = str(input("Enter the Description of the Super of your brawler : "))
    csv_writer.writerow(['TID_' + capbrawlername, brawlername])
    csv_writer.writerow(['TID_' + capbrawlername + '_DESC', description])
    csv_writer.writerow(['TID_' + capbrawlername + '_WEAPON', attack_name])
    csv_writer.writerow(['TID_' + capbrawlername+ '_WEAPON_DESC', attack_description])
    csv_writer.writerow(['TID_' + capbrawlername + '_ULTI', ulti_name])
    csv_writer.writerow(['TID_' + capbrawlername + '_ULTI_DESC', ulti_description])


if __name__ == "__main__":
    update_cards_csv_file()
    update_characters_csv_file()
    update_skins_csv_file()
    update_skin_conf_csv()
    update_skills_csv_file_1()
    update_skills_csv_file_2()
    update_texts_csv()
    print("Done creating Brawler")
    print(" ")
