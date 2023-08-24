from fuzzywuzzy import fuzz, process

result = fuzz.ratio("this is a test", "this is a test!")
print(result)

result = fuzz.ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear")
print(result)
result = fuzz.token_sort_ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear")
print(result)

choices = ["Atlanta Falcons", "New York Jets", "Dallas Cowboys"]
result = process.extract("new york jets", choices, limit=2)
print(result)

result = process.extractOne("cowboys", choices)
print(result)