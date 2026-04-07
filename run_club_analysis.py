import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("run_club_dataset.xlsx")

plt.plot(df['Date'], df['Participants'])
plt.xticks(rotation=45)
plt.title("Run Club Participation Trend")
plt.xlabel("Date")
plt.ylabel("Participants")

plt.tight_layout()

#save
plt.savefig("participants_trend.png")

plt.show()
