import time

class Taxi:
    def __init__(self,id):
        self.id = id
        self.taxi_loaction = 'A'
        self.earning = 0
        self.availablity = True
        self.time_to_free = 0
    
    def bookTaxi(self,pickup,drop):
        self.availablity = False
        travel_time = abs(ord(pickup) - ord(drop)) * 60
        self.time_to_free = time.time() + travel_time
        fare = self.calculateFare(pickup,drop)
        self.earning += fare
        self.taxi_loaction = drop
        return fare,travel_time

    def calculateFare(self,pickup,drop):
        distance = abs(ord(drop) - ord(pickup)) * 15
        return 100 if distance <= 5 else 100 + ((distance - 5) * 10)
    
    def updateAvailability(self):
        if time.time() >= self.time_to_free:
            self.availablity = True

class BookingSystem:
    def __init__(self,num_taxi):
        self.taxies = [Taxi(i) for i in range(1,num_taxi+1)]
        self.locations = ['A','B','C','D','E','F']
    
    def findNearest(self,pickup):
        nearest_taxi = None
        min_distance = float('inf')

        for taxi in self.taxies:
            taxi.updateAvailability()
            if taxi.availablity:
                distance = abs(ord(taxi.taxi_loaction) - ord(pickup)) * 15

                if distance < min_distance or (distance == min_distance and taxi.earning < nearest_taxi.earning):
                    nearest_taxi = taxi
                    min_distance = distance
        return nearest_taxi,min_distance
    
    def bookingDetails(self,pickup,drop):
        if pickup not in self.locations or drop not in self.locations:
            return 'Invalid Pickup or Drop location'
        
        taxi,min_dis = self.findNearest(pickup)

        if taxi:
            fare,travel_time = taxi.bookTaxi(pickup,drop)
            
            # To check the availability 1 Hr of travel time is converted into 1 min
            return f"Taxi{taxi.id} is booked. Fare Rs.{fare}. Travelling time {travel_time//60} mins. Your taxi is {min_dis} kms away from your Pick up"
        else:
            return 'No taxi is available right now. Please try again later'
    

def main():
    system = BookingSystem(num_taxi=4)
    while True:
        print(f'\nTaxi Booking')
        pickup = input('Select pickup (A,B,C,D,E,F): ').strip().upper()
        drop = input('Select Drop (A,B,C,D,E,F): ').strip().upper()

        result = system.bookingDetails(pickup,drop)
        print(result)

if __name__ == '__main__':
    main()