def my_print(txt):
    print(txt)

# """" are like pre> in HTML thye presrerve the format
# """

# Hva to do pyhton -i main.py for this pne

msg_template = """Hello {name},
Thank you for joining {website}. We are very
happy to have you with us.
""" .format(name="Justin", website='cfe.sh')

my_print("Hello World")