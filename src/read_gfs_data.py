import getgfs
import matplotlib.pyplot as plt
f=getgfs.Forecast("0p25")
res1=f.get(["ugrd10m"],"20220520 06:30", "[32:36]","[142.0:146.0]")
res2=f.get(["vgrd10m"],"20220520 06:30", "[32:36]","[142.0:146.0]")

u = res1.variables["ugrd10m"].data[0]
v = res2.variables["vgrd10m"].data[0]

plt.quiver(u, v)

# for d in f.search("wind"):
#   print(d)
