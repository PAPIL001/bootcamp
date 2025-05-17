def show_settings(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

show_settings(mode="dark", volume=70)
