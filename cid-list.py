input_strings = ["", "", ""]

for input_string in input_strings:
    bot_name, password = input_string.split(":")
    output_string = f'{{BotName = "{bot_name}", Password = "{password}"}}'
    print(output_string)
