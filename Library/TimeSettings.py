from datetime import datetime
from time import sleep



class Time_Config:

    def __init__(self, unit_time='s'):
        """
            @brief Time setting

            @param [unit_time]:    (String) Unit time first letter.\n
               unit_time m = minutes // unit_time h = hours // unit_time s = seconds (default)
        """
        self.unit_time = unit_time.lower()


    def time_out(self, value):
        """
            @brief Time setting

            @param [value]:    (INT) Time sleep.\n
        """
        if self.unit_time == 'm':
            sleep(60*value)

        elif self.unit_time == 'h':
            sleep(3600*value)

        else:
            sleep(value)


    def time_hour(self, hours,  kind='%H:%M'):
        """
            @brief Scheduler

            @param [hours]:    (STR) Date value.\n
            @param [kind]:     (STR) Date type.\n
                kind %H = Hour(s) // kind %M = minute(s) // kind %H:%M = Hour(s) and minute(s) (default)
        """
        while True:
            now = datetime.now()
            if kind.upper() == "%H:%M" and hours == now.strftime("%H:%M"):
                return 1
            elif kind.upper() == "%H" and hours == now.strftime("%H"):
                return 1
            elif kind.upper() == "%M" and hours == now.strftime("%M"):
                return 1
