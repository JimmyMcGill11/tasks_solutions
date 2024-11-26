def library_book_analysis(records):
  
  borrowed_books = {}
  
  for record in records:
    title, days = record.split(" - ")
    days = int(days)
    
    if title in borrowed_books:
      borrowed_books[title] += days
    else:
      borrowed_books[title] = days

  most_borrowed = max(borrowed_books.items(), key=lambda x: x[1])
  least_borrowed = min(borrowed_books.items(), key=lambda x: x[1])

  total_days = sum(borrowed_books.values())
  total_books = len(borrowed_books)
  average_days = total_days / total_books if total_books > 0 else 0

  unique_titles = set(borrowed_books.keys())

  sorted_books = sorted(borrowed_books.items(), key=lambda x: x[1], reverse=True)

  return {
    "Most Borrowed": most_borrowed,
    "Least Borrowed": least_borrowed,
    "Average Days": average_days,
    "Unique Titles": unique_titles,
    "Sorted Books": sorted_books,
  }

records = [
  "Book I - 10",
  "Book II - 5",
  "Book X - 15",
  "Book IV - 3",
  "Book I - 7",
  "Book II - 2",
  "Book X - 7"
]

result = library_book_analysis(records)

print("Most Borrowed:", result["Most Borrowed"])
print("Least Borrowed:", result["Least Borrowed"])
print("Average Days:", result["Average Days"])
print("Unique Titles:", result["Unique Titles"])
print("Sorted Books:", result["Sorted Books"])
