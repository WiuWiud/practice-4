def check_disk(value):
    if value >= 80:
        return "warning"
    return "ok"