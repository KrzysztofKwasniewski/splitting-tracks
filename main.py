from pydub import AudioSegment
from math import floor
import os

class Katalog:

    def __init__(self):
        self.lista = []
        self.file_format = ('mp3','ogg','flv','mp4', 'wma','aac')

    def katolog(self,path, format):
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                name=name.split('.')
                if name[-1] in self.file_format and format == name[-1]:
                    # dodaje liste z name_track pliku i location
                    self.lista.append([root, '.'.join(name)])
                    
class Muzyka:

    def question_how_many_minutes(self,how_many_minutes):
        self.quantity = floor(self.minutes_milliseconds/60)
        self.how_much = floor(self.quantity/how_many_minutes)
        return self.how_much

    def zapis(self,question_of_the_minute:int,lista:list, format:str):
        track_list = [_ for _ in lista]
        one_minute = 60 * 1000

        print(f"{len(track_list)} tracks found.")
        
        if len(track_list) == 0:
            quit()
        
        for track in track_list:
            self.name_track = track[1].split('.')
            self.name_track = self.name_track[0]
            location_and_name_of_the_file = "/".join(track)
            track = location_and_name_of_the_file
            try:
                self.sound = AudioSegment.from_file(track, format=format)
                self.track_lenght = self.sound.duration_seconds # float
                if self.track_lenght/60 > float(question_of_the_minute):
                # rozdzielenie
                    division = str(self.track_lenght).split(".")
                    minutes = division[0]
                    self.minutes_milliseconds = int(minutes)
                    #######################################
                    quantity = self.question_how_many_minutes(question_of_the_minute)
                    a = 1
                    b = 2
                    nr = 1
                    
                    variable = self.sound[:one_minute*question_of_the_minute]
                    variable.export(f"{self.name_track}_{nr}.{format}", format=format)
                    print(f"Done {self.name_track} No. {nr}")
                    for _ in range(1,quantity+1):
                        variable = self.sound[one_minute*a*question_of_the_minute:one_minute*b*question_of_the_minute]
                        nr += 1
                        variable.export(f"{self.name_track}_{nr}.{format}", format=format)
                        print(f"Done {self.name_track} No. {nr}")
                        a += 1
                        b += 1        
                print(f'Track too short: {self.name_track}')
            
            except Exception as e:
                print('---'*10)
                print(f'Error: {str(e)}, file: {track}')
                print('---'*10)

if __name__=="__main__":
    katalog = Katalog()
    formaty = str(katalog.file_format).replace('(','').replace(')','').replace("'","")
    muzyka = Muzyka()

    print("Location e.g. in linux: /home/home/Music/music /n in Windows: C:\\Music")
    location = input('Enter the song locations: ')
    #location = '/home/home/Muzyka/muzyka'
    print(f"Obslugiwane formaty: {formaty}")

    petla = True
    while petla:
        format = input("Enter the format of the files you are looking for, e.g. mp3: ")
        if format not in katalog.file_format:
            print('---'*10)
            print(f"wrong format {format} entered, please try again!")
            print(f"Supported Formats: {formaty}")
            print('---'*10)
            format = input("Enter the format of the files you are looking for, e.g. mp3: ")
        petla = False

    minutes = int(input('Enter every how_much minutes files are to be split, e.g. 4:'))
    katalog.katolog(location,format)
    lista = katalog.lista
    muzyka.zapis(minutes,lista, format)

    print('finished!')
