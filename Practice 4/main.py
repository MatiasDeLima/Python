


# a = "asdfasdgf";
# b = "LUCAS MATIAS";

# print(a.upper());
# print(b.lower());


a = "Hey There How Are Your";
b = '';

for i in a:
    if i.islower():
        b = b + i

for i in a:
    if i.isupper():
        b = b + i;

print(b);