import csv
import collections
from collections import Counter

#Where i learned to use the csv https://www.youtube.com/watch?v=q5uM4VKywbA&vl=en
class DataReader():
    def __init__(self,laMax = 39.7589, laMin = 31.1031, loMin = -84.5120, loMax = -84.1916):
        with open('accident.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            self.data = []
            self.time = []
            self.danger = []
            self.deaths = 0
            self.cood = []
            self.loMin = -abs(loMin)-1/56
            self.loMax = -abs(loMax)-1/56
            self.laMax = laMax+1/69
            self.laMin = laMin+1/69
            self.responeTime = []
            self.deathby = {
            1 : 'Overturn',
            2 : 'Fire/Explosion',
            3 : 'Immersion',
            4 : 'Gas Inhalation',
            5 : 'Fell from Vehicle',
            6 : 'Injured in Vehicle (Non-Collision)',
            7 : 'Other Non-Collision',
            8 : 'Pedestrian',
            9 : 'Pedalcycle',
            10 : 'Railway Vehicle',
            11 : 'Live Animal',
            12 : 'Motor Vehicle in Transport',
            13 : 'Motor Vehicle in Transport in Other Roadway',
            14 : 'Parked Motor Vehicle',
            15 : 'Non-Motorist on Personal Conveyance',
            16 : 'Thrown or falling Object',
            17 : 'Boulder',
            18 : 'Other object (Not Fixed)',
            19 : 'Building',
            20 : 'Impact Attenuator/Crash Cushion',
            21 : 'Bridge Pier or Support',
            22 : 'Embankment',
            23 : 'Bridge Rail (Includes Parapet)',
            24 : 'Guardrail Face',
            25 : 'Concrete Traffic Barrier',
            26 : 'Other Traffic Barrier',
            30 : 'Utility Pole/Light Support',
            31 : 'Post, Pole, or Other Supports',
            32 : 'Culvert',
            33 : 'Curb',
            34 : 'Ditch',
            35 : 'Embankment',
            38 : 'Fence',
            39 : 'Wall',
            40 : 'Fire Hydrant',
            41 : 'Shrubbery',
            42 : 'Tree (Standing Only)',
            43 : 'Other Fixed Object',
            44 : 'Pavement Surface Irregularity (Ruts, Potholes, Grates, etc.)',
            45 : 'Working Motor Vehicle',
            46 : 'Traffic Signal Support',
            48 : 'Snow Bank',
            49 : 'Ridden Animal or Animal-Drawn Conveyance (Since 1998)',
            50 : 'Bridge Overhead Structure',
            51 : 'Jackknife (Harmful to This Vehicle)',
            52 : 'Guardrail End',
            53 : 'Mail Box',
            54 : 'Motor Vehicle In-Transport Strikes or is Struck by Cargo, Persons or Objects Set-in-Motion from/by Another MotorVehicle In-Transport',
            55 : '55 Motor Vehicle in Motion Outside the Trafficway',
            57 : 'Cable Barrier (Since 2008)',
            58 : 'Ground',
            59 : 'Traffic Sign Support',
            72 : 'Cargo/Equipment Loss or Shift (Harmful to This Vehicle)',
            73 : 'Object That Had Fallen From Motor Vehicle In-Transport',
            74 : 'Road Vehicle on Rails',
            99 : 'Unknown'
            }
            for line in csv_reader:
                if(float(line['LATITUDE']) >=laMin and float(line['LATITUDE']) <=laMax and float(line['LONGITUD']) >=loMin and float(line['LONGITUD']) <=loMax):
                    self.data += [line]
                    self.time += [int(line['HOUR'])]
                    self.danger += [self.deathby[int(line['HARM_EV'])]]
                    self.responeH = -1
                    self.responeM = -1
                    self.deaths += int(line['FATALS'])
                    if int(line['ARR_HOUR'])<25 and int(line['HOUR'])<25 and int(line['ARR_MIN'])<61 and int(line['MINUTE'])<61:
                        self.responeH = int(line['ARR_HOUR'])-int(line['HOUR'])
                        self.responeM = int(line['ARR_MIN'])-int(line['HOUR'])
                        if self.responeH <0:
                            self.responeH = 24 + self.responeH
                        if  self.responeM < 0:
                            self.responeM = 60 + self.responeM
                        self.responeTime +=[self.responeM+self.responeH*60]
                    dead = self.deathby[int(line['HARM_EV'])]
                    self.cood += [{'LATITUDE':float(line['LATITUDE']),'LONGITUD':abs(float(line['LONGITUD'])),'VE_TOTAL':int(line['VE_TOTAL']),'RESPONSE_HOUR':self.responeH,'RESPONSE_MIN':self.responeM,'FATALS':int(line['FATALS']),'HARM_EV':dead}]

    def locations(self):
        return self.cood
    def totalCrashes(self):
        return len(self.data)
    def totalFatals(self):
        return self.deaths
    def worstDriveTime(self):
        timing = Counter(self.time)
        mostOccur = timing.most_common(1)
        return mostOccur
    def mostOccur(self):
        crash = Counter(self.danger)
        mostOccur = crash.most_common(1)
        return mostOccur
    def helpTime(self):
        avg = 0
        for time in self.responeTime:
            avg +=time
        avg=avg//len(self.responeTime)
        return avg
