def parse_input(user_input):
    cmd, *args = user_input.split(' ')
    cmd.strip().lower()
    return cmd, *args