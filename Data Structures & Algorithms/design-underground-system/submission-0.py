class UndergroundSystem:
    def __init__(self):
        self.check_ins={}
        self.journeys={}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id]=(stationName,t)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start,time = self.check_ins[id]
        self.check_ins[id]={}
        total,count = self.journeys.get((start,stationName),(0,0))
        self.journeys[(start,stationName)]=(total+t-time,count+1)
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total,count = self.journeys[(startStation,endStation)]
        return total/count
