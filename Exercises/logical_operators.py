is_magician = True
is_expert = True

#Check if magician AND expert
# if true "you are master magician"

#Check if magician but not expert
# at least you're getting there

#Check if not magician
# you need magic powers

if is_magician and is_expert:
    print("You are a master magician")
elif is_magician and not is_expert:
    print("You're getting there")
elif not is_magician:
    print("You need magic powers")
else:
    print("What are you")