def mapping(M):
    def f(X):
        return M*X
    return f

image = cap.read()
M = calibrate( 'screen_img', image )
find_laser = mapping(M)
canvas = np.full(...)

while True:
    image = cap.read()
    x, y = get_laser( image )
    lx, ly = find_laser(x, y)
    canvas = draw_point( canvas, (lx, ly) )
    out = mix_img(image, canvas)
    imshow(out)
    k = waitkey(10)
    if k == ord( 'c' ):
        calibrate again
    else if  k == ord( 'r' ):
        canvas = np.full(...)