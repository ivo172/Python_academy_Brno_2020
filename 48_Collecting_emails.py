# The main function should be named main(), it should call all the other
# needed function and return the result. As you can see from the example
# above, The result should be a dictionary with keys domains and
# emails_with_nums, containing values - lists with relevant emails.

my_str = '''Lorem ipsum dolor sit amet, consectetur adipiscing
        elit. Mauris vulputate lacus id eros consequat tempus.
        Nam viverra velit sit amet lorem lobortis, at tincidunt
        nunc ultricies. Duis facilisis ultrices lacus, id
        tiger123@email.cz auctor massa molestie at. Nunc tristique
        fringilla congue. Donec ante diam cnn@info.com, dapibus
        lacinia vulputate vitae, ullamcorper in justo. Maecenas
        massa purus, ultricies a dictum ut, dapibus vitae massa.
        Cras abc@gmail.com vel libero felis. In augue elit, porttitor
        nec molestie quis, auctor a quam. Quisque b2b@money.fr
        pretium dolor et tempor feugiat. Morbi libero lectus,
        porttitor eu mi sed, luctus lacinia risus. Maecenas posuere
        leo sit amet spam@info.cz. elit tincidunt maximus. Aliquam
        erat volutpat. Donec eleifend felis at leo ullamcorper cursus.
        Pellentesque id dui viverra, auctor enim ut, fringilla est.
        Maecenas gravida turpis nec ultrices aliquet.'''


def main(words):    #main function
    e_mails = separator_email(words)
    e_mails = e_mails.split()
    domains_ = domains(e_mails)
    domains_with_nums = with_nums(e_mails)
    result = {'domains' : [domains_], 'emails_with_nums' : [domains_with_nums]}
    return result


def separator_email(text):  # function separate emails from text
    text = text.replace(',', '').split()
    email_adr = ''
    for word in text:
        for char in word:
            if char == '@':
                email_adr = email_adr + ' ' + word
            else:
                continue
    return email_adr


def domains(e_adress):  # slice domains from email adress
    domains = ''
    for adress in e_adress:
        domains = domains + ' ' + adress[int(adress.index('@')):
                                         int(str(len(adress)))]
    return domains


def with_nums(text): # returns email adress with number
    word_with_nums = ''
    for word in text:
        word_x = word.replace('@','').replace('.','')
        if not word_x.isalpha():
            word_with_nums = word_with_nums + ' ' + word
        else:
            continue
    return word_with_nums


print(main(my_str)) # call main function an print
