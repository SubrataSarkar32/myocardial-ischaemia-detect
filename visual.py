try:
    import wfdb
    import numpy as np
except ImportError:
    import pip
    pip.main(['install','matplotlib','wfdb'])
    import wfdb
record = wfdb.rdrecord('european-st-t-database/e0104') 
wfdb.plot_wfdb(record=record, title='Record e0104 from European st-t') 
#display(record.__dict__)
#print(record.p_signal[:240][1])
arr1=np.array(record.p_signal[:])
y, x = arr1.T
x=np.array([y for y in x])
x=x.reshape(-1, 1)
x_r = x[:240]
print(x[:240])
from matplotlib import pyplot as plt
ts=[y for y in range(240)]
plt.scatter(ts,x_r)
plt.show()
x_new=[[0.455],
 [0.46 ],
 [0.45 ],
 [0.425],
 [0.435],
 [0.455],
 [0.49 ],
 [0.5  ],
 [0.485],
 [0.5  ],
 [0.495],
 [0.5  ],
 [0.5  ],
 [0.515],
 [0.53 ],
 [0.56 ],
 [0.57 ],
 [0.56 ],
 [0.535],
 [0.535],
 [0.535],
 [0.525],
 [0.51 ],
 [0.5  ],
 [0.5  ],
 [0.49 ],
 [0.485],
 [0.465],
 [0.46 ],
 [0.45 ],
 [0.445],
 [0.44 ],
 [0.435],
 [0.44 ],
 [0.445],
 [0.475],
 [0.495],
 [0.5  ],
 [0.5  ],
 [0.48 ],
 [0.45 ],
 [0.43 ],
 [0.43 ],
 [0.445],
 [0.495],
 [0.63 ],
 [0.88 ],
 [1.29 ],
 [1.77 ],
 [2.19 ],
 [2.415],
 [2.32 ],
 [1.985],
 [1.535],
 [1.085],
 [0.75 ],
 [0.58 ],
 [0.52 ],
 [0.525],
 [0.525],
 [0.515],
 [0.49 ],
 [0.475],
 [0.465],
 [0.45 ],
 [0.455],
 [0.455],
 [0.465],
 [0.48 ],
 [0.475],
 [0.49 ],
 [0.475],
 [0.455],
 [0.46 ],
 [0.465],
 [0.475],
 [0.475],
 [0.46 ],
 [0.485],
 [0.485],
 [0.485],
 [0.485],
 [0.495],
 [0.495],
 [0.495],
 [0.495],
 [0.495],
 [0.49 ],
 [0.485],
 [0.5  ],
 [0.515],
 [0.53 ],
 [0.515],
 [0.54 ],
 [0.555],
 [0.57 ],
 [0.58 ],
 [0.595],
 [0.575],
 [0.585],
 [0.6  ],
 [0.62 ],
 [0.65 ],
 [0.665],
 [0.695],
 [0.71 ],
 [0.725],
 [0.73 ],
 [0.73 ],
 [0.75 ],
 [0.76 ],
 [0.765],
 [0.755],
 [0.76 ],
 [0.77 ],
 [0.775],
 [0.77 ],
 [0.76 ],
 [0.755],
 [0.735],
 [0.71 ],
 [0.685],
 [0.66 ],
 [0.62 ],
 [0.6  ],
 [0.57 ],
 [0.555],
 [0.54 ],
 [0.53 ],
 [0.52 ],
 [0.505],
 [0.5  ],
 [0.5  ],
 [0.495],
 [0.485],
 [0.495],
 [0.485],
 [0.485],
 [0.49 ],
 [0.465],
 [0.485],
 [0.485],
 [0.49 ],
 [0.48 ],
 [0.475],
 [0.475],
 [0.49 ],
 [0.475],
 [0.46 ],
 [0.455],
 [0.465],
 [0.475],
 [0.485],
 [0.48 ],
 [0.48 ],
 [0.485],
 [0.49 ],
 [0.49 ],
 [0.48 ],
 [0.465],
 [0.45 ],
 [0.445],
 [0.45 ],
 [0.45 ],
 [0.475],
 [0.465],
 [0.455],
 [0.45 ],
 [0.45 ],
 [0.475],
 [0.465],
 [0.48 ],
 [0.485],
 [0.475],
 [0.49 ],
 [0.48 ],
 [0.45 ],
 [0.465],
 [0.475],
 [0.485],
 [0.485],
 [0.465],
 [0.485],
 [0.475],
 [0.475],
 [0.465],
 [0.465],
 [0.475],
 [0.475],
 [0.475],
 [0.475],
 [0.455],
 [0.45 ],
 [0.44 ],
 [0.435],
 [0.43 ],
 [0.45 ],
 [0.455],
 [0.465],
 [0.465],
 [0.45 ],
 [0.445],
 [0.445],
 [0.45 ],
 [0.455],
 [0.45 ],
 [0.46 ],
 [0.455],
 [0.455],
 [0.465],
 [0.465],
 [0.475],
 [0.485],
 [0.49 ],
 [0.485],
 [0.475],
 [0.475],
 [0.455],
 [0.465],
 [0.465],
 [0.475],
 [0.465],
 [0.455],
 [0.44 ],
 [0.455],
 [0.475],
 [0.51 ],
 [0.53 ],
 [0.535],
 [0.54 ],
 [0.525],
 [0.5  ],
 [0.5  ],
 [0.525],
 [0.56 ],
 [0.57 ],
 [0.56 ],
 [0.54 ],
 [0.535],
 [0.54 ]]
ts=[y for y in range(240)]
plt.scatter(ts,x_new)
plt.show()
