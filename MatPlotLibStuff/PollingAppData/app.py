import matplotlib.pyplot as plt
import database
import charts

charts.create_bar_chart(database.get_polls_and_votes())
plt.show()
