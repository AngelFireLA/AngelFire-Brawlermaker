import csv


def update_csv_file():
    csv_writer = csv.writer(open('skills.csv', 'a'), delimiter=',')
    version = int(input("Wich BS d you use ?(input only the number)(1-Real_BS 2-Rebrawl) ? : "))
    if version == 2:
        attacktype = int(input("What type of attack do you want ? (1-Normal 2-Charge 3-Spawnable)"))
        ammo_or_super = int(input("Is it an ammo or a super (1-Ammo 2-Super) ? : "))
        if attacktype == 1:
            nombrawler  = str(input("Name of the Brawler : "))
            attackduration = int(input("Duration of the attack (in miliseconds) (rosa's duration let 3 punches for example and default is 150) : "))
            range = int(input("Range of the attack (primo is 9 and rico is 29) : "))
            if ammo_or_super ==1:
                reloadtime = int(input("How long for a brawler to reload an ammo (in miliseconds) : "))
                ammonumber = int(input("How many ammo (1-4) : "))
            else:
                reloadtime = ''
                ammonumber = ''
                weapon_or_ulti = "Ulti"
            damage = int(input("How much damage for each projectile ? : "))
            timebetweenattacks= int(input("How much time between each attacks ? (in milliseconds)(colonel ruff have a small one and default is 100) ? : "))
            spread = str(input("How much spread ? (shelly is 60 and poco is 130 and nita 0) ? : "))
            attackpatern = int(input("What attack patern (1 is by default but you can search for more information of the others) ? : "))
            numberofprojectiles = int(input("How much projectiles do you want in one ammo ? : "))
            projectile = str(input("Wich projectile do you want ? (from projectiles.csv) ? :"))
            csv_writer.writerow([nombrawler + weapon_or_ulti, 'Attack', 'true', 'true', 'true', '', '50', attackduration, '', range, '', '', '', '', reloadtime, ammonumber, damage, '', timebetweenattacks, spread, attackpatern, numberofprojectiles, '', 'true', '', '', '', '', '', '', '', '', projectile, '', '', '', '', '', '', '', '', 'sc/ui.sc', 'rapid_fire_button', 'rico_def_atk', '', '', '', '', '', '', '', '', '', '', '', ''])
        elif attacktype == 2:
            nombrawler = str(input("Name of the Brawler : "))
            range = int(input("Range of the attack (primo is 9 and rico is 29) : "))
            if ammo_or_super ==1:
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
            if ammo_or_super ==1:
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


if __name__  == "__main__" :
    update_csv_file()
    print(" ")
    print("Done adding the skill")
