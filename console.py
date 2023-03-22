from models.author import Author
from models.book import Book

import repositories.author_repo as author_repo
import repositories.book_repo as book_repo


author_repo.delete_all()
book_repo.delete_all()


author1 = Author("William Corlett")
author_repo.save(author1)

author2 = Author("Claire Keegan")
author_repo.save(author2)

author3 = Author("Stanley Tucci")
author_repo.save(author3)

author4 = Author("Sheena Patel")
author_repo.save(author4)

author5 = Author("Jane Harper")
author_repo.save(author5)

author6 = Author("Dr Gwen Adshead")
author_repo.save(author6)


author_repo.select_all()


book1 = Book("Now and Then", author1, "https://app.thestorygraph.com/books/a5277205-54b5-4fbe-a359-dcd8004ea0a9", "https://cdn.thestorygraph.com/p8yv2v9202eipojiu02pzprx6bd9")
book_repo.save(book1)

book2 = Book("Small Things Like These", author2, "https://app.thestorygraph.com/books/a49523ae-4893-4a00-892f-876543ddf423", "https://cdn.thestorygraph.com/ax6l7ekdmah961c7lthkv5ahvhjh")
book_repo.save(book2)

book3 = Book("Taste", author3, "https://app.thestorygraph.com/books/9de3288b-b28f-4af2-9fcb-788670336e37", "https://cdn.thestorygraph.com/o9u4erbafu8srluwvferpv561egl")
book_repo.save(book3)


book4 = Book("I'm a Fan", author4, "https://app.thestorygraph.com/books/446ae4fa-df63-4e98-9333-edacd8592ca6", "https://cdn.thestorygraph.com/d5qtzy4ad6rg2fcd1wvrdbcduix1")
book_repo.save(book4)


book5 = Book("The Dry", author5, "https://app.thestorygraph.com/books/333650e7-b9ee-433a-a765-ffaaf2673e0f", "https://cdn.thestorygraph.com/vnvwdz2cjdqomz022w1u48x1vwfn")
book_repo.save(book5)


book6 = Book("The Devil You Know", author6, "https://app.thestorygraph.com/books/ea9f0822-0941-49dc-aa2a-ca3e0de7b161", "https://cdn.thestorygraph.com/rf8qvil0eqyycjknh0o6qwgrzlda")
book_repo.save(book6)

print(book_repo.find_book_by_title_author('The Dry', 'Jane Harper'))
print(book_repo.find_book_by_title_author('Hello', 'Aneeqa'))

