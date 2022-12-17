from packaging_tut.a_package import AClass


def main(config):
    a_class = AClass(config)
    output = a_class.run()
    print(output)



