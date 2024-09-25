import pandas as pd

df = pd.read_csv("Day25_CSVfileDistrictGame/data.csv")
data = df.District.to_list()
output = []

for dis in data:
    if dis[:4] == "Quận":
        output.append(dis[5:])
    if dis[:5] == "Huyện":
        output.append(dis[6:])
    if dis[:6] == "Thị xã":
        output.append(dis[7:])


#x, y coordinate of district from file export_coor_district.py
coor = [(-2.0, 43.0), (-25.0, 43.0), (25.0, 39.0), (29.0, 21.0), (23.0, -8.0), (3.0, 26.0), 
        (-4.0, 75.0), (-10.0, 12.0), (-47.0, 75.0), (-51.0, -21.0), (56.0, 47.0), (-48.0, 26.0), 
        (-355.0, 117.0), (-129.0, -84.0), (-115.0, 111.0), (15.0, 127.0), (108.0, 47.0), 
        (-96.0, 40.0), (-91.0, 165.0), (-87.0, -260.0), (70.0, -217.0), (-198.0, 120.0), 
        (-179.0, -18.0), (0.0, 248.0), (-227.0, 30.0), (-30.0, -106.0), (15.0, -41.0), 
        (38.0, -108.0), (-9.0, -229.0), (-277.0, 103.0)]

dic = {
    "District" : output,
    "x" : [ele[0] for ele in coor], 
    "y" : [ele[1] for ele in coor]
}

df_output = pd.DataFrame.from_dict(dic)
# df_output.to_csv("Day25_CSVfileDistrictGame/District.csv")