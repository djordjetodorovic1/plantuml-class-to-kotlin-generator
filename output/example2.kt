open class Person(
    var id: Int,
    var fullName: String
)

class User(
    id: Int,
    fullName: String,
    var username: String,
    var email: String
) : Person(id, fullName) {
    var orders: List<Order> = mutableListOf()

}

class Order(
    var totalAmount: Double,
    var status: String
)