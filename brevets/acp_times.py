"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#
def calc(control_dist_km, speed):
  hours = control_dist_km // speed;
  mins = round((control_dist_km / speed) - hours) * 60;
  arrow.shift(hours = hours, minutes = mins);


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    
    # For controls beyond the first 200km, the maximum speed decreases. 
    # Here the calculation is more difficult. Consider a control at 350km. 
    # We have 200/34 + 150/32 = 5H53 + 4H41 = 10H34. The 200/34 gives us the
    # minimum time to complete the first 200km while the 150/32 gives us the
    # minimum time to complete the next 150km. The sum gives us the control's
    # opening time.

    # open_time = max_time * distance
    hours = 0.0
    intervals = {
      200: 34,
      400-200: 32,
      600-400: 30,
      1000-600: 28,
      1300-1000: 26,
    }

    if control_dist_km > brevet_dist_km:
      if control_dist_km <= (brevet_dist_km + (brevet_dist_km*0.2)):
        control_dist_km = brevet_dist_km
      else
        return -1

    for interval, max_speed in intervals:
      if control_dist_km <= 0:
        break
      dist = min(control_dist_km, interval) 
      hours += dist / max_speed
      control_dist_km -= interval

    mins = (hours - int(hours)) * 60
    result = brevet_start_time.shift(hours = int(hours), minutes = mins)
    return result


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    
    # close_time = min_speed * distance
    hours = 0.0 

    if control_dist_km > brevet_dist_km:
      if control_dist_km <= (brevet_dist_km + (brevet_dist_km*0.2)):
        control_dist_km = brevet_dist_km
      else
        return -1

    if control_dist_km == brevet_dist_km:
      if control_dist_km == 200:
        hours = 13
        mins = 30
        return brevet_start_time.shift(hours = hours, minutes = mins)
      elif control_dist_km == 300:
        hours = 20
        mins = 0
        return brevet_start_time.shift(hours = hours, minutes = mins)
      elif control_dist_km == 400:
        hours = 27
        mins = 0
        return brevet_start_time.shift(hours = hours, minutes = mins)
      elif control_dist_km == 600:
        hours = 40
        mins = 0
        return brevet_start_time.shift(hours = hours, minutes = mins)
      elif control_dist_km == 1000:
        hours = 75
        mins = 0
        return brevet_start_time.shift(hours = hours, minutes = mins)

    if control_dist_km <= 60:
      dist = min(control_dist_km, 60)
      min_speed = 20; #in km/h
      # the maximum time limit for a control within the first 60km
      # is based on 20 km/hr, plus 1 hour.
      hours += (dist / min_speed) + 1
      control_dist_km -= 60

    else:

      intervals = {
        200: 15,
        400-200: 15,
        600-400: 15,
        1000-600: 11.428,
        1300-1000: 13.333,
      }
      for interval, min_speed in intervals:
        if control_dist_km <= 0:
          break
        dist = min(control_dist_km, interval)
        hours += dist / min_speed
        control_dist_km -= interval

    mins = (hours - int(hours)) * 60
    result = brevet_start_time.shift(hours = int(hours), minutes = mins)
    return result
