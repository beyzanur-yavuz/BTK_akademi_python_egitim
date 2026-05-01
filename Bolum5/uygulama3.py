class Robot:
    toplam_robot_sayisi=0
    def __init__(self,isim):
        self.isim=isim
        Robot.toplam_robot_sayisi+=1
    def selamla(self):
        print(f"merhaba ben {self.isim}")    
    @classmethod
    def robot_sayisini_sorgula(cls):
        print(f"şu an dünyada {cls.toplam_robot_sayisi} robot var.")

robot1=Robot("Chatgbt")
robot2=Robot("siri")
robot1.selamla()
robot2.selamla()
Robot.robot_sayisini_sorgula()