import csv

'''def read_csv_file():
    for row in csv.reader(open('skills.csv' , 'r'), delimiter=','):
        if len(row) > 0:
            a = 0
            for i in range (56):
                print(row[a+1]+ ' ')'''

def update_csv_file():
    csv_writer = csv.writer(open('skills.csv', 'a'), delimiter=',')
    nombrawler  = str(input("Name of the Brawler : "))
    attackduration = int(input("Duration of the attack (in miliseconds) (rosa's duration let 3 punches for example and default is 150) : "))
    range = int(input("Range of the attack (primo is 9 and rico is 29) : "))
    reloadtime = int(input("How long for a brawler to reload an ammo (in miliseconds) : "))
    ammonumber = int(input("How many ammo (1-4) : "))
    damage = int(input("How much damage for each projectile ? : "))
    timebetweenattacks= int(input("How much time between each attacks ? (in milliseconds)(colonel ruff have a small one and default is 100) ? : "))
    spread = str(input("How much spread ? (shelly is 60 and poco is 130 and nita 0) ? : "))
    attackpatern = int(input("What attack patern (1 is by default but you can search for more information of the others) ? : "))
    numberofprojectiles = int(input("How much projectiles do you want in one ammo ? : "))
    projectile = str(input("Wich projectile do you want ? (from projectiles.csv) ? :"))


    csv_writer.writerow([nombrawler + 'Weapon', 'Attack', 'true', 'true', 'true', '', '50', attackduration, '', range, '', '', '', '', reloadtime, ammonumber, damage, '', timebetweenattacks, spread, attackpatern, numberofprojectiles, '', 'true', '', '', '', '', '', '', '', '', projectile, '', '', '', '', '', '', '', '', 'sc/ui.sc', 'rapid_fire_button', 'rico_def_atk', '', '', '', '', '', '', '', '', '', '', '', ''])

if __name__  == "__main__" :
    update_csv_file()
    print(" ")
    print("Done adding the skill")
