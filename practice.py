print("***********CUSTOMER FEEDBACK FORM ***************")
raw_name = input("Enter customer name: ")
raw_feedback = input("Enter feedback message: ")
rating = input("Enter rating (1 to 5): ")



clean_name = raw_name.strip()
clean_feedback = raw_feedback.strip()



formatted_name = clean_name.title()

formatted_feedback = clean_feedback.capitalize()

formatted_feedback = formatted_feedback.replace(" u ", " you ")
formatted_feedback = formatted_feedback.replace(" r ", " are ")

words = formatted_feedback.split()



joined_feedback = " ".join(words)


exclamation_count = formatted_feedback.count("!")


category_positive = "positive".upper()



feedback_lower = formatted_feedback.lower()


if int(rating) >= 4:
    category = category_positive
else:
    category = "needs review".upper()

print("-" * 45)



print(f"{'PROFESSIONAL FEEDBACK REPORT':^45}")

print("-" * 45)


print(f"Customer Name : {formatted_name}")
print(f"Rating        : {rating} / 5 Stars")
print(f"Category      : {category}")
print(f"Excitement    : {exclamation_count} exclamation mark(s)")

print("-" * 45)

print("Formatted Message:")
print(f"{joined_feedback}")

print("-" * 45)

print("\n************STRING METHOD EXAMPLES****************")
print("-" * 45)

print(f"UPPERCASE  : {formatted_feedback.upper()}")
print(f"LOWERCASE  : {formatted_feedback.lower()}")
print(f"TITLE CASE : {formatted_feedback.title()}")
print(f"CAPITALIZE : {formatted_feedback.capitalize()}")
print(f"STRIPPED   : {clean_feedback}")
print(f"REPLACED   : {formatted_feedback}")
print(f"SPLIT      : {words}")
print(f"JOINED     : {joined_feedback}")

print("-" * 45)