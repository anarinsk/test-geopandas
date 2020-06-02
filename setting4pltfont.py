from matplotlib import font_manager, rc
import matplotlib as mpl
import matplotlib.pyplot as plt 

font_fname = '/usr/share/fonts/truetype/nanum/NanumGothicCoding.ttf'
font_name = font_manager.FontProperties(fname=font_fname).get_name()
#plt.rcParams['figure.figsize'] = [15, 7]
plt.rcParams['figure.dpi'] = 100
mpl.rcParams['axes.unicode_minus'] = False
plt.rcParams["font.size"] = 10
plt.rcParams['xtick.labelsize'] = 8
plt.rcParams['ytick.labelsize'] = 8
plt.rcParams['font.family'] = font_name

print(f'{font_name} is set!')