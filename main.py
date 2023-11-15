from pandas import read_excel
from matplotlib import pyplot


def draw_graph(url):
    file = read_excel(url)

    first_type = [[], []]
    second_type = [[], []]
    third_type = [[], []]

    classes = list(file["class"])
    nodes = list(file["node"])
    ends = list(file["end"])

    iterator = 0
    for class_type in classes:
        if class_type == "first":
            first_type[0].append(nodes[iterator])
            first_type[1].append(ends[iterator])
        elif class_type == "second":
            second_type[0].append(nodes[iterator])
            second_type[1].append(ends[iterator])
        else:
            third_type[0].append(nodes[iterator])
            third_type[1].append(ends[iterator])
        iterator += 1
    print("first class:\n")
    print(first_type[0])
    print(first_type[1])
    print("\nsecond class:\n")
    print(second_type[0])
    print(second_type[1])
    print("\nthird class:\n")
    print(third_type[0])
    print(third_type[1])

    pyplot.plot(first_type[1], first_type[0], "ro")
    pyplot.plot(second_type[1], second_type[0], "bo")
    pyplot.plot(third_type[1], third_type[0], "go")
    pyplot.xlabel("Ne")
    pyplot.ylabel("Nnd")
    pyplot.show()


if __name__ == '__main__':
    draw_graph("data.xlsx")