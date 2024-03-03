import otpsy as ot
import pandas as pd

df = pd.read_csv("./tests/data.csv", sep = ";")
a = ot.Sample(df, columns_to_test=["art_looking_time", "discrimination_performance",],
              participant_column="index_participant").method_IQR(2.4, True)
a.add("P4")
print(a.dict_col)

print(a.threshold)