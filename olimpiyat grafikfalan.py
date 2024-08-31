import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Excel dosyasını oku
oku = pd.read_excel('C:\\Users\\buğra\\Desktop\\olimpiyat_verisi (1).xlsx')

print(oku.head())
xx = oku.dropna()
print(oku.describe())
print(oku.info())
print(oku.columns)

boy=oku['boy']
kilo=oku['kilo']
cinsiyet=oku['cinsiyet']
madalya=oku['madalya']
sezon=oku['sezon']
yaş=oku['yas']
sns.set_style("whitegrid")
sns.scatterplot(x='boy', y='kilo' , hue=cinsiyet , style=madalya , size=yaş   ,  data=oku )
plt.xlabel("boy")
plt.ylabel("kilo")
plt.title("boy-kilo")
plt.ylim(25, 180)
plt.xlim(130, 230)
plt.show()



sns.displot(oku ,x='boy', hue='cinsiyet')
sns.set_style=("whitegrid")
plt.xlabel("kilo")
plt.legend()
plt.show()

sns.barplot(x='madalya' , y='boy' , hue='sezon' , data=oku )
plt.xlabel("cinsiyet")
plt.ylabel("kilo")
plt.show()
