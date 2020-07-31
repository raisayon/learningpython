first_name = 'sayon'
last_name = 'rai'
note = 'award: Nobel Peace Prize'
first_name_cap = first_name.capitalize()
last_name_cap = last_name.isupper() #checking uppercase
print(first_name_cap)
print(last_name_cap)
award_location = note.find('award: ')
print(award_location)
award_text = note[7:]
print(award_text)
