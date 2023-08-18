from faker import Faker
fake = Faker()
print(fake.name())
print(fake.address())
print(fake.text())
print(fake.email())
print(fake.country())
print(fake.latitude(), fake.longitude())
print(fake.url())
for i in range(10):
    print(fake.name())

