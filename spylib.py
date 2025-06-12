# Dummy SpyLib module placeholder


def parse_t_me_c_link(link: str):
    # Example: https://t.me/c/2535013502/1610
    import re
    match = re.search(r't\.me/c/(\d+)/(\d+)', link)
    if match:
        chat_id = -100 * 10**(len(match.group(1)) - 1) + int(match.group(1))
        message_id = int(match.group(2))
        return chat_id, message_id
    raise ValueError("Invalid t.me/c/ link format.")
