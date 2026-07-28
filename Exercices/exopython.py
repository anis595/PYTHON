bobine = int(input(" quel est le nombre de bobine souhaité? "))
fdp = 15


if bobine <= 10:
    prix = bobine * 24
elif (bobine > 10) and (bobine <= 25):
    prix = bobine * 21
else:
    prix = bobine * 18

if prix > 400:
    fdp = 0
    print("frais de port offer !")

print(f" Le total est de :{prix + fdp} €")
