class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            t = (position[i], speed[i])
            cars.append(t)
        cars.sort(key=lambda x: x[0], reverse=True)

        s = []
        for car in cars:
            if s:
                fleetInfront = s[-1]
                timeOfArrival = (target - car[0]) / car[1]
                timeOfArrivalFleet = (target - fleetInfront[0]) / fleetInfront[1]

                if timeOfArrival > timeOfArrivalFleet:
                    s.append(car)

            else:
                s.append(car)  

        return len(s)          

            