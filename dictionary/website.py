webpage = {'name': 'Webpage', 'URL': 'www.webpage.com', 'size': 20}
print(webpage)
web = {}
web['name'] = 'csit'
web['URL'] = 'www.csit.com'
web['size'] = 30
print(web)
print(webpage)


for name, url in webpage.items():
    print('{} is {}'.format(name, url))

for x in webpage.keys():
    print(x)
print("_______________________")
for x in webpage.values():
    print(x)
