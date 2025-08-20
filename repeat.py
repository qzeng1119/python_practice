def repeat(x):
    return make_detector(lambda i: False)(x)

def make_detector(have_seen):
    def detector(x):
        if have_seen(x):
            print(x)
            return make_detector(have_seen)
        else:
            return make_detector(lambda i: i == x or have_seen(i))
    return detector

repeat(3)(4)(3)(9)(7)(4)(5)(7)(5)
