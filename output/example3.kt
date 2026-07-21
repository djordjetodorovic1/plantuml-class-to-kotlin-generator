interface Drawable {
    fun draw()
}

abstract class Shape(protected var color: Color) {
    abstract fun calculateArea(): Double

}

class Circle(
    color: Color,
    var radius: Double
) : Shape(color), Drawable {
    override fun calculateArea(): Double {
        TODO()
    }
    override fun draw() {
        TODO()
    }

}

class Rectangle(
    color: Color,
    var width: Double,
    var height: Double
) : Shape(color), Drawable {
    override fun calculateArea(): Double {
        TODO()
    }
    override fun draw() {
        TODO()
    }

}

class Canvas(var name: String) {
    var shapes: List<Shape> = mutableListOf()
    fun refresh() {
        TODO()
    }

}

enum class Color {
    RED,
    GREEN,
    BLUE,
    YELLOW
}