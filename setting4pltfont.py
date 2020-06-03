import matplotlib 
import matplotlib.pyplot as plt 
matplotlib.font_manager._rebuild()
font_name = 'NanumGothicCoding'
#plt.rcParams['figure.figsize'] = [15, 7]
matplotlib.rcParams['axes.unicode_minus'] = False
plt.rcParams["font.size"] = 10
plt.rcParams['xtick.labelsize'] = 8
plt.rcParams['ytick.labelsize'] = 8
plt.rcParams['font.family'] = font_name
print(f'{font_name} is set!')