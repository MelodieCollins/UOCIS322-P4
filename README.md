# UOCIS322 - Project 4 #

## Brevet Controle Time Calculation Rules

Acording to rusa.org:

Overall time limits vary for each brevet according to the distance. 
These are: (in hours and minutes, HH:MM) 13:30 for 200 KM, 20:00 for 300 KM, 
27:00 for 400 KM, 40:00 for 600 KM, and 75:00 for 1000 KM. A rider’s total elapsed 
time is calculated from the opening time of the start control (regardless of the rider’s
actual start time) to the rider’s arrival time at the finish control. Additionally, 
riders must arrive at each checkpoint between the opening and closing time for the 
checkpoint. These times are noted on the brevet card with the information for the 
checkpoints.

The table below gives the minimum and maximum speeds for ACP brevets.

Control location (km): 0-200, 200-400, 400-600, 600-1000, 1000-1300	
Minimum Speed (km/hr): 15,    15,      15,      11.428,   13.333
Maximum Speed (km/hr): 34,    32,      30,      28,       26

The calculation of a control's opening time is based on the maximum speed. Calculation of a control's closing time is based on the minimum speed.


Distance, Speed, and Time Calculation:
When a distance in kilometers is divided by a speed in kilometers per hour, the result is a time measured in hours. For example, a distance of 100 km divided by a speed of 15 km per hour results in a time of 6.666666... hours. To convert that figure into hours and minutes, subtract the whole number of hours (6) and multiply the resulting fractional part by 60. The result is 6 hours, 40 minutes, expressed here as 6H40.

If the control distance in kilometers is greater than the nominal distance of the brevet and if the control distance in kilometers is smaller than or equal to 120% of the nominal distance of the brevet, then the control distance in kilometers is equal to the nominal distance of the brevet. Otherwise, the control distance is too big.
      
If the control distance in kilometers is equal to the nominal distance of the brevet then:
200 kilometres (120 mi) – 13.5 hours (15 km/h)
300 kilometres (190 mi) – 20 hours (15 km/h)
400 kilometres (250 mi) – 27 hours (15 km/h)
600 kilometres (370 mi) – 40 hours (15 km/h)
1,000 kilometres (620 mi) – 75 hours (13.3 km/h)

For controls beyond the first 200km, the maximum speed decreases. Here the calculation is more difficult. Consider a control at 350km. We have 200/34 + 150/32 = 5H53 + 4H41 = 10H34. The 200/34 gives us the minimum time to complete the first 200km while the 150/32 gives us the minimum time to complete the next 150km. The sum gives us the control's opening time.


Some Oddities include: 
The maximum time limit for a control within the first 60km is based on 20 km/hr, plus 1 hour.


## Author

Melodie Collins, mcolli11@uoregon.edu

## Date

May 16, 2021


## Credits

Michal Young, Ram Durairajan, Steven Walton, Joe Istas.
