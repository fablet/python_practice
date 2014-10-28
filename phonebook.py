class Contact():
    def __init__(self, name, number, address):
        self.name = name
        self.number = number
        self.address = address


class PhoneBook():
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        # self.contacts.append(contact)

    def find_contact(self, search_name):
        for person in self.contacts:
            if person.name.lower == search_name:
                return person
            else:
                print("Not found")
                return "error"

    def remove_contact(self, search_name):
        to_remove = self.find_contact(search_name)
        if not to_remove == "error":
            self.contacts.remove(to_remove)

    def print_info(self, contact):
        print("{}: \n\t--{}\n\t--{}".format(contact.name, contact.number, contact.address))

    def print_all(self):
        for person in self.contacts:
            self.print_info(person)

def main():
    pb = PhoneBook()
    while True:
        cmd = raw_input('Command?: ')
        if cmd == 'exit' or cmd == 'q' or cmd == 'quit':
            exit(1)
        elif cmd == 'add':
            name = raw_input('Name?:\t')
            num = raw_input('Number?:\t')
            addr = raw_input('Address?:\t')
            pb.add_contact(Contact(name, num, addr))
        elif cmd == 'remove' or cmd == 'delete':
            name = raw_input('Who to remove?:\t')
            pb.remove_contact(name)
        elif cmd == 'find' or cmd == 'print':
            search = pb.find_contact(raw_input('Who?'))
            search = search.lower()
            pb.print_info(search)
        elif cmd == 'print all' or cmd == 'printall':
            pb.print_all()
        elif cmd == 'help' or cmd == 'h' or cmd == '?':
            print("exit:\texits command\n"
                  "add:\tadds new contact\n"
                  "remove:\tremove contact\n"
                  "find:\tfind contact by name\n"
                  "print all:\tprint all contacts")
        else:
            print('Sorry, I don\'t recognize that command. Try again.')

if __name__ == '__main__':
    main()