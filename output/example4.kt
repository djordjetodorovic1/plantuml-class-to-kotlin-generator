interface IBorrowable {
    fun borrowItem(memberId: Int): Boolean
    fun returnItem(memberId: Int): Boolean
}

abstract class Document(
    var id: Int,
    var title: String
) {
    abstract fun getDetails(): String

}

class Book(
    id: Int,
    title: String,
    var author: String,
    var status: BookStatus
) : Document(id, title), IBorrowable {
    override fun getDetails(): String {
        TODO()
    }
    override fun borrowItem(memberId: Int): Boolean {
        TODO()
    }
    override fun returnItem(memberId: Int): Boolean {
        TODO()
    }

}

class Magazine(
    id: Int,
    title: String,
    var issueNumber: Int
) : Document(id, title) {
    override fun getDetails(): String {
        TODO()
    }

}

class LibraryMember(
    var memberId: Int,
    var fullName: String
)

class Library(var name: String) {
    var catalogue: List<Document> = mutableListOf()
    var members: List<LibraryMember> = mutableListOf()

}

enum class BookStatus {
    AVAILABLE,
    BORROWED,
    RESERVED,
    LOST
}