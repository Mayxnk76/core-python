# Q-1 Write a Python program to input a sentence and a positive integer from the user. Perform the following tasks:
# 1.	Display all words having more consonants than vowels.
st = input("enter string here:")
num = input("enter a positive number:")
words = st.split()

print("word having more consonants than vowels:")

for word in words:
    vowel = 0
    cons = 0
    for ch in word.lower():
        if ch.isalpha():
            if ch in "aeiou":
                vowel += 1
            else:
                cons += 1
    if cons > vowel:
        print(word)
# 2.	Count the number of words containing at least one repeated character.
rep = 0
for word in words:
    word = word.lower()

    found_rep = False

    for ch in word:
        if word.count(ch) > 1:
            found_rep = True
            break

    if found_rep:
        rep += 1

print("Words containing repeated Characters:",rep)

# 3.	Find how many times the largest digit occurs in the given number.
ld = max(num)
lc = num.count(ld)

print("largest digit:",ld)
print("largest digit occurs:",lc,"time")
# 4.	Create a new number by removing all odd digits from the given number.
new_num = ""

for digit in num:
    if int(digit) % 2 == 0:
        new_num += digit

print("new number after removing odd digits:",new_num)


# Q-2 Write a Python program to input n words from the user and store them in a list. Perform the following tasks:
n = int(input("Enter number of words: "))

words = []

for i in range(n):
    word = input("Enter word: ")
    words.append(word)
# 1.Create a dictionary where:
# o	Key → Word
# o	Value → Number of distinct characters in the word
word_dict = {}

for word in words:
    distinct_count = len(set(word.lower()))
    word_dict[word] = distinct_count

print("\nDictionary:")
print(word_dict)
# 2.	Create a tuple containing all words having vowels as the first and last character.
vowel_words = []

for word in words:
    word_lower = word.lower()

    if word_lower[0] in "aeiou" and word_lower[-1] in "aeiou":
        vowel_words.append(word)

vowel_tuple = tuple(vowel_words)

print("\nTuple of words starting and ending with vowels:")
print(vowel_tuple)

# 3.	Create a set containing the last character of each word.
last_characters = set()

for word in words:
    last_characters.add(word[-1].lower())

print("\nSet of last characters:")
print(last_characters)
# 4.	Display the words in which the first character occurs again anywhere else in the same word.
print("\nWords where first character occurs again:")

for word in words:
    word_lower = word.lower()
    first_character = word_lower[0]

    if word_lower[1:].count(first_character) > 0:
        print(word)

# Q-3 Write a Python program to accept details of n movies and create a dictionary in the following format:
movies = {
    201: ["Sky Force", "Action", 250, 40],
    202: ["Dream Story", "Drama", 180, 25],
    203: ["Fast Track", "Action", 300, 50],
    204: ["Happy Days", "Comedy", 200, 30]
}
# Where:
# Key → Movie ID
# Value → [Movie Name, Genre, Ticket Price, Tickets Sold]
# Perform the following tasks:
n = int(input("Enter number of movies: "))

movies = {}
for i in range(n):
    movie_id = int(input("\nEnter movie ID: "))
    movie_name = input("Enter movie name: ")
    genre = input("Enter genre: ")
    ticket_price = int(input("Enter ticket price: "))
    tickets_sold = int(input("Enter tickets sold: "))

    movies[movie_id] = [
        movie_name,
        genre,
        ticket_price,
        tickets_sold
    ]
# 1.	Create a new dictionary where Movie ID is the key and value is a tuple containing:
# (Movie Name, Total Collection)
# where:
collection_dict = {}

for movie_id, details in movies.items():
    movie_name = details[0]
    ticket_price = details[2]
    tickets_sold = details[3]

    total_collection = ticket_price * tickets_sold

    collection_dict[movie_id] = (
        movie_name,
        total_collection
    )

print("\nCollection Dictionary:")
print(collection_dict)
# Total Collection = Ticket Price × Tickets Sold
# 2.	Create a set containing all the different genres.
genres = set()

for details in movies.values():
    genre = details[1]
    genres.add(genre)

print("\nDifferent Genres:")
print(genres)
# 3.	Display all movies which have sold more than 30 tickets.
print("\nMovies with more than 30 tickets sold:")

for movie_id, details in movies.items():
    movie_name = details[0]
    tickets_sold = details[3]

    if tickets_sold > 30:
        print(movie_id, movie_name)
# 4.	Find and display the movie having the highest total collection.
highest_collection = 0
highest_movie = ""

for movie_id, details in movies.items():
    movie_name = details[0]
    ticket_price = details[2]
    tickets_sold = details[3]

    total_collection = ticket_price * tickets_sold

    if total_collection > highest_collection:
        highest_collection = total_collection
        highest_movie = movie_name

print("\nMovie with highest collection:")
print(highest_movie, highest_collection)
# 5.	Display all movies whose ticket price is less than the average ticket price of all movies.
total_price = 0

for details in movies.values():
    total_price += details[2]

average_price = total_price / len(movies)

print("\nAverage Ticket Price:", average_price)

print("Movies with ticket price less than average:")

for movie_id, details in movies.items():
    movie_name = details[0]
    ticket_price = details[2]

    if ticket_price < average_price:
        print(movie_id, movie_name, ticket_price)