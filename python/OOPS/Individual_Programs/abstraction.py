from abc import ABC,abstractmethod

class Mobile(ABC):
    def __init__(self):
        super().__init__()
        self.company1 = "Samsung"
        self.company2 = "Apple"

    @abstractmethod
    def wifi(self):
        pass

    @abstractmethod    
    def bluetooth(self):
        pass

    @abstractmethod
    def hotspot(self):
        pass

    @abstractmethod
    def screen(self):
        pass

class Samsung(Mobile):
    def __init__(self):
        super().__init__()

    def android_version(self):
        print(f"{self.company1} has latest android version 15")

    def reverse_charging(self):
        print(f"{self.company1} has reverse charging feature")

    def wifi(self):
        print(f"{self.company1} has wifi-802.11 a/b/g/n/ac")

    def bluetooth(self):
        print(f"{self.company1} has Bluetooth version 5.0")

    def hotspot(self):
        print(f"{self.company1} supports 2.4 & 5ghz")    

    def screen(self):
        print(f"{self.company1} has Super Amoled Display")

class Apple(Mobile):
    def __init__(self):
        super().__init__()

    def os_version(self):
        print(f"{self.company2} has latest 18.4.1 version")

    def facetime(self):
        print(f"{self.company2} has facetime")

    def airdrop(self):
        print(f"{self.company2} has Airdrop feature")

    def wifi(self):
        print(f"{self.company2} has 802.11ax wifi")

    def bluetooth(self):
        print(f"{self.company2} has bluetooth 5.3")

    def hotspot(self):
        print(f"{self.company2} has all bands hotspot support ")

    def screen(self):
        print(f"{self.company2} has Super retina XDR Display")

state_obj= [Samsung(),Apple()] 

for state in state_obj:
    state.wifi()
    state.bluetooth()
    state.screen()
    state.hotspot()
    print()
