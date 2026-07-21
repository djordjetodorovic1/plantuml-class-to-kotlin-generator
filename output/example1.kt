open class Vehicle(var speed: Int) {
    fun start() {
        TODO()
    }
    fun stop() {
        TODO()
    }

}

class Car(
    speed: Int,
    var numDoors: Int
) : Vehicle(speed)

class Bicycle(
    speed: Int,
    var hasBell: Boolean
) : Vehicle(speed)