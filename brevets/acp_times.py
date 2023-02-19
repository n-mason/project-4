"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_acp.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
   """
   Args:
      control_dist_km:  number, control distance in kilometers
      brevet_dist_km: number, nominal distance of the brevet
         in kilometers, which must be one of 200, 300, 400, 600,
         or 1000 (the only official ACP brevet distances)
      brevet_start_time:  An arrow object
   Returns:
      An arrow object indicating the control open time.
      This will be in the same time zone as the brevet start time.
   """
   # To calculate opening times, use the maximum speed from table
   # Based on the brevet_dist, will determine max speed
   # Then, once have that speed, use the control_dist and speed to calculate hours and mins
   # Then shift the brevet start time with those hour and min values
   max_speed = 0
   
   if brevet_dist_km <= 200:
      max_speed = 34
   elif 200 < brevet_dist_km <= 400:
      max_speed = 32
   elif 400 < brevet_dist_km <= 600:
      max_speed = 30
   elif 600 < brevet_dist_km <= 1000:
      max_speed = 28
   elif 1000 < brevet_dist_km <= 1300:
      max_speed = 26

   hours_value = control_dist_km // max_speed # Floor division to get only the hours amount
   # Now, separate into hours and mins
   mins_value = ((control_dist_km / max_speed) - hours_value) * 60 # Multiplying resulting fractional part by 60

   return brevet_start_time.shift(hours=hours_value, minutes=mins_value)


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
   """
   Args:
      control_dist_km:  number, control distance in kilometers
         brevet_dist_km: number, nominal distance of the brevet
         in kilometers, which must be one of 200, 300, 400, 600, or 1000
         (the only official ACP brevet distances)
      brevet_start_time:  An arrow object
   Returns:
      An arrow object indicating the control close time.
      This will be in the same time zone as the brevet start time.
   """
   # To calculate closing times, use the minimum speed
   # Based on the brevet_dist, will determine min speed
   # Then, once have that speed, use the control_dist and speed to calculate hours and mins
   # Then shift the brevet start time with those hour and min values
   min_speed = 0
   
   if brevet_dist_km <= 200:
      min_speed = 15
   elif 200 < brevet_dist_km <= 400:
      min_speed = 15
   elif 400 < brevet_dist_km <= 600:
      min_speed = 15
   elif 600 < brevet_dist_km <= 1000:
      min_speed = 11.428
   elif 1000 < brevet_dist_km <= 1300:
      min_speed = 13.333

   hours_value = control_dist_km // min_speed # Floor division to get only the hours amount
   # Now, separate into hours and mins
   mins_value = ((control_dist_km / min_speed) - hours_value) * 60 # Multiplying resulting fractional part by 60

   return brevet_start_time.shift(hours=hours_value, minutes=mins_value)
