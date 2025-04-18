import find_rated_levels
import time
import os

diff = 1

while True:
    data1 = find_rated_levels.find_rated_levels(diff)
    data2 = find_rated_levels.account_beat_rated_levels()[diff-1]
    data3 = (int(data2)/int(data1)) * 100
    os.system('clear')
    print("Percent of easy rated levels beaten: " + str(data3) + " (" + str(data2) + "/" + str(data1) + ")")
    time.sleep(3)
