import create_film_params


res = [200]
pols = ["x","y","r","l"]
sx = [1]
sy =[1]
dx = [.05]
dy1 = [1.5]
dy2 = [0]
theta = [0]
freq_center = [.275]
freq_width = [.175]

fname = "params_single_nanoslit_ir.txt"
create_film_params.create_params_file(fname, res, pols, sx, sy, dx, dy1, dy2, theta, freq_center, freq_width)
