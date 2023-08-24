import wikipedia

# Source : https://wikipedia.readthedocs.io/en/latest/code.html#api
print(wikipedia.random(pages=2))
print(wikipedia.summary(wikipedia.random()))
print(wikipedia.WikipediaPage(title=wikipedia.random()).html()) # Bisa pake flask hasil html nya