import matplotlib.pyplot as plt

option_votes = [63, 28, 8]
option_names = [
    "Flask",
    "Django",
    "It depends"
]

figure = plt.figure()
axes = figure.add_subplot()

axes.pie(
    option_votes,
    labels=option_names,
    explode=[0.1, 0, 0],
    autopct="%1.1f%%"
)
plt.show()
