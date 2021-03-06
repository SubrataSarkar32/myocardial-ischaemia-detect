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
x_new=[[-1.56 ],
 [-1.54 ],
 [-1.525],
 [-1.5  ],
 [-1.5  ],
 [-1.5  ],
 [-1.51 ],
 [-1.53 ],
 [-1.545],
 [-1.545],
 [-1.545],
 [-1.55 ],
 [-1.585],
 [-1.58 ],
 [-1.595],
 [-1.605],
 [-1.62 ],
 [-1.625],
 [-1.62 ],
 [-1.62 ],
 [-1.61 ],
 [-1.615],
 [-1.62 ],
 [-1.605],
 [-1.605],
 [-1.595],
 [-1.59 ],
 [-1.585],
 [-1.595],
 [-1.63 ],
 [-1.715],#q point
 [-1.705],
 [-1.58 ],
 [-1.37 ],
 [-0.965],
 [-0.57 ],
 [-0.405],#r peak
 [-0.405],
 [-0.46 ],
 [-0.54 ],
 [-0.73 ],
 [-1.055],
 [-1.335],
 [-1.55 ],
 [-1.62 ],#s point
 [-1.615],
 [-1.59 ],
 [-1.545],
 [-1.55 ],
 [-1.56 ],
 [-1.57 ],
 [-1.575],
 [-1.57 ],
 [-1.565],
 [-1.58 ],
 [-1.57 ],
 [-1.565],
 [-1.57 ],
 [-1.565],
 [-1.56 ],
 [-1.555],
 [-1.555],
 [-1.56 ],
 [-1.545],
 [-1.53 ],#t starrt
 [-1.53 ],
 [-1.53 ],
 [-1.525],
 [-1.515],
 [-1.515],
 [-1.515],
 [-1.505],
 [-1.5  ],
 [-1.475],
 [-1.465],
 [-1.47 ],
 [-1.465],
 [-1.45 ],
 [-1.44 ],
 [-1.435],
 [-1.415],
 [-1.415],
 [-1.415],
 [-1.41 ],
 [-1.395],
 [-1.395],
 [-1.395],
 [-1.39 ],
 [-1.385],
 [-1.365],
 [-1.38 ],
 [-1.39 ],
 [-1.39 ],
 [-1.385],
 [-1.39 ],
 [-1.4  ],
 [-1.4  ],
 [-1.405],
 [-1.405],
 [-1.42 ],
 [-1.415],
 [-1.415],
 [-1.41 ],
 [-1.405],
 [-1.405],
 [-1.39 ],
 [-1.41 ],
 [-1.42 ],
 [-1.44 ],
 [-1.435],
 [-1.445],
 [-1.45 ],
 [-1.465],
 [-1.475],
 [-1.485],
 [-1.49 ],
 [-1.5  ],
 [-1.5  ],
 [-1.51 ],
 [-1.525],
 [-1.53 ],#t end
 [-1.54 ],
 [-1.535],
 [-1.54 ],
 [-1.555],
 [-1.56 ],
 [-1.555],
 [-1.56 ],
 [-1.56 ],
 [-1.56 ],
 [-1.55 ],
 [-1.56 ],
 [-1.56 ],
 [-1.56 ],
 [-1.55 ],
 [-1.55 ],
 [-1.545],
 [-1.56 ],
 [-1.545],
 [-1.545],
 [-1.54 ],
 [-1.545],
 [-1.54 ],
 [-1.54 ],
 [-1.54 ],
 [-1.53 ],
 [-1.53 ],
 [-1.53 ],
 [-1.515],
 [-1.52 ],
 [-1.525],
 [-1.53 ],
 [-1.525],
 [-1.53 ],
 [-1.525],
 [-1.53 ],
 [-1.53 ],
 [-1.53 ],
 [-1.53 ],
 [-1.53 ],
 [-1.53 ],
 [-1.53 ],
 [-1.54 ],
 [-1.53 ],
 [-1.56 ],
 [-1.54 ],
 [-1.545],
 [-1.56 ],
 [-1.555],
 [-1.545],
 [-1.56 ],
 [-1.56 ],
 [-1.545],
 [-1.545],
 [-1.545],
 [-1.56 ],
 [-1.555],
 [-1.56 ],
 [-1.56 ],
 [-1.56 ],
 [-1.555],
 [-1.56 ],
 [-1.575],
 [-1.565],
 [-1.565],
 [-1.56 ],
 [-1.565],
 [-1.57 ],
 [-1.575],
 [-1.56 ],
 [-1.55 ],
 [-1.56 ],
 [-1.55 ],
 [-1.535],
 [-1.53 ],
 [-1.53 ],
 [-1.525],
 [-1.51 ],
 [-1.49 ],
 [-1.475],
 [-1.465],
 [-1.46 ],
 [-1.48 ],
 [-1.51 ],
 [-1.53 ],
 [-1.525],
 [-1.53 ],
 [-1.55 ],
 [-1.545],
 [-1.56 ],
 [-1.575],
 [-1.59 ],
 [-1.59 ],
 [-1.59 ],
 [-1.595],
 [-1.59 ],
 [-1.59 ],
 [-1.59 ],
 [-1.585],
 [-1.575],
 [-1.575],
 [-1.575],
 [-1.565],
 [-1.575],
 [-1.595],
 [-1.675],
 [-1.715],
 [-1.6  ],
 [-1.405],
 [-1.04 ],
 [-0.59 ],
 [-0.375],
 [-0.355],
 [-0.395],
 [-0.455],
 [-0.555],
 [-0.83 ],
 [-1.155],
 [-1.425],
 [-1.58 ]]
ts=[y for y in range(240)]
plt.scatter(ts,x_new)
plt.show()

