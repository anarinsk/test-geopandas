from matplotlib import font_manager, rc
import matplotlib as mpl
import matplotlib.pyplot as plt 

mpl.font_manager._rebuild()

font_fname = '/usr/share/fonts/truetype/nanum/NanumGothicCoding.ttf'
font_name = font_manager.FontProperties(fname=font_fname).get_name()

print(f'{font_name} is set!')

#plt.rcParams['figure.figsize'] = [15, 7]
mpl.rcParams['axes.unicode_minus'] = False
plt.rcParams["font.size"] = 10
plt.rcParams['xtick.labelsize'] = 8
plt.rcParams['ytick.labelsize'] = 8
plt.rcParams['font.family'] = font_name