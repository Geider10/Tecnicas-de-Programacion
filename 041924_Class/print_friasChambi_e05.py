#exercise 05
hourPair = int(input("start time: "))
minutePair = int(input("minute of time:"))
duration = int(input("duration the event: "))

totalMinutes = duration + minutePair
newHora = totalMinutes / 60
restoMinutes = totalMinutes % 60
totalHours = hourPair + newHora

if (totalHours >= 24):
    dia = totalHours % 24
    print("El evento empieza a las ", hourPair, ":",minutePair," y dura ",duration,"m terminara a las ",int(dia),":",restoMinutes)
else:
    print("El evento empieza a las ", hourPair, ":",minutePair," y dura ",duration,"m terminara a las ",int(totalHours),":",restoMinutes)
