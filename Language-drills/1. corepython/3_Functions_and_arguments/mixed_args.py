def config(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

config(1, 2, theme="light", size=10)
