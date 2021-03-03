class foo:
    mylt = []
    def print_in_reverse(self):
        for x in self.mylt:
            print(x)

my_foo = foo()

my_foo.mylt.append(1);
my_foo.mylt.append(4);
my_foo.mylt.append(13);

my_foo.print_in_reverse()

