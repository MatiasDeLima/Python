## == upper case and lower case == ##

# a = "asdfasdgf";
# b = "LUCAS MATIAS";

# print(a.upper());
# print(b.lower());

## == Get string in uppercase and lowercase and order == ##

# a = "Hey There How Are Your";
# b = '';

# for i in a:
#     if i.islower():
#         b = b + i

# for i in a:
#     if i.isupper():
#         b = b + i;

# print(b); # eyhereowreourHTAY

## == split method

# a = "Lucas Matias de Lima";
# b = a.split();

# print(b); # ['Lucas', 'Matias', 'de', 'Lima']

## == Count string
str = "P@#yn26at^&i5ve";

chr = 0;
dig = 0;
spchr = 0;

for i in str:
    if i.isdigit():
        dig = dig + 1;
    elif i.isalpha():
        chr = chr + 1;
    else:
        spchr = spchr + 1;

print(chr);
print(dig);
print(spchr);