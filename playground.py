with open("exercise_files/10_04_challenge_art.txt", "r") as file:
    lines = file.readlines()

with open("playground.txt", "w") as file:
    line = lines[4]
    prev_char = lines[4][0]
    count = 0
    for character in line:
        if character == prev_char:
            count += 1
        else:
            input = "S" if prev_char == " " else "N" if prev_char == "\n" else prev_char
            file.write(f"{input}{count}")
            prev_char = character
            count = 1

with open("playground.txt", "r") as file:
    encoding = file.readline()

    decoded_string = ""
    curr_char = encoding[0]
    count = "0"
    for character in encoding[1:]:
        if character.isdigit():
            count += f"{character}"
        else:
            print(curr_char, int(count))
            curr_char = character
            count = "0"
    print(curr_char, int(count))

    # while curr_char:
    #     i = 0
    #     while curr_char.isdigit():
    #         curr_char = encoding[i]
    #         count += int(curr_char)
    #     decoded_string += curr_char * count
    #     curr_char = encoding[i]

print(decoded_string)
