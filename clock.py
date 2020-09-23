import os, time

def notify(text):
    os.system(f"""
              osascript -e 'display notification "{text}"'""")

start = 0

while (True):
    countdown = int(input("Ingrese un número mayor a cero: "))
    if (countdown<=0):
        continue
    else: 
        while start < countdown:
            m, s = divmod(start, 60)
            clock = str(m).zfill(2) + ":" + str(s).zfill(2)
            print(clock, end ="\r")
            time.sleep(1)
            start += 1
            if (start == countdown):
                text = 'El reloj se ha parado'
                notify(text)
                print(f"Los {countdown} segs terminaron")
                break
    break





        