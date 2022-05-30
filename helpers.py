import getgfs

def get_wind_speed(lat, lon):
  f=getgfs.Forecast("0p25")
  res1=f.get(["ugrd10m"],"20220526 06:30", f"{lat}",f"{lon}")
  res2=f.get(["vgrd10m"],"20220526 06:30", f"{lat}",f"{lon}")

  u = res1.variables["ugrd10m"].data[0]
  v = res2.variables["vgrd10m"].data[0]

  return [u, v]


# for d in f.search("wind"):
#   print(d)
