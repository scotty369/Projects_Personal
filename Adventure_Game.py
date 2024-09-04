''
# You will be given an answer choice as the story progresses, and each choice will lead to more choices resulting in something terrifying or good. Please select the choice of which you would like and attempt to get out of the forest. Not all choices will lead to a resolution. Play at your own risk, and good luck finding your way out of the dark and dreary forest!
print("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you pick up?")
choice = input().lower()

if choice == "match":
    print("You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large wolf, and then the match burns out. Do you want to RUN or HIDE behind a tree?")
    choice = input().lower()
    if choice == "run":
        print("You start to run through the dark forest. All around you is nothing but black, but you start to see the faint outline of trees. You come to a for in the road and can choose between LEFT, RIGHT, or MIDDLE.")
        choice = input().lower()
        if choice == "left":
            print("You run left and suddenly find yourself at the edge of a cliff. The only way is back.")
        elif choice == "right":
            print("You run right and see a light in the distance. It's a ranger's station! You're safe.")
        elif choice == "middle":
            print("You run to the middle of the fork and enter a maze of trees and shrubbery. You're not sure what to do. So you break down in terror realizing you are completely lost.")
        else:
            print("Invalid choice. Please choose between LEFT, RIGHT, MIDDLE.")


    elif choice == "hide":
        print("After seeing the large wolf, you decide to hide behind a mess of shrubs. While hiding and waiting for the wolf to leave, you hear some rustling in the leaves. Do you want to GO or STAY?")
        choice = input().lower()
        if choice == "go":
            print("You decide to go and find yourself face to face with a friendly dog. It leads you out of the forest.")
        elif choice == "stay":
            print("You stay hidden, and eventually, the wolf leaves. You find your way out once it is the morning and you can see clearly.")
        else:
            print("Invalid choice. Please choose between GO and STAY.")

elif choice == "flashlight":
    print("You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees to see what made the noise?")
    choice = input().lower()
    if choice == "follow":
        print("You follow the path and it leads you to a cozy cabin. You knock on the door, and the owner lets you stay for the night.")
    elif choice == "look":
        print("You look in the trees and find an owl. It hoots, and you start to get scared that there's no way out of this forest.")
    else:
        print("Invalid choice. Please choose between FOLLOW or LOOK.")
#That concludes the adventure game! Hopefully you made it out, if not, then you can try again and choose different answers to escape. Do it at your own risk!