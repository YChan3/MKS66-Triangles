from display import *
from matrix import *


def add_polygon( polygons, x0, y0, z0, x1, y1, z1, x2, y2, z2 ):
    add_point(polygons, x0, y0, z0)
    add_point(polygons, x1, y1, z1)
    add_point(polygons, x2, y2, z2)

def draw_polygons( polygons, screen, color ):
    if len(polygons) < 3:
        print ('Need at least 3 points to draw')
        return

    point = 0
    while point < len(polygons) - 2:
        a = [polygons[point+1][0]-polygons[point][0],
            polygons[point+1][1]-polygons[point][1],
            polygons[point+1][2]-polygons[point][2]]

        b = [polygons[point+2][0]-polygons[point][0],
            polygons[point+2][1]-polygons[point][1],
            polygons[point+2][2]-polygons[point][2]]

        n = [a[1]*b[2]-a[2]*b[1],
             a[2]*b[0]-a[0]*b[2],
             a[0]*b[1]-a[1]*b[0]]

        v=[0,0,1]

        if n[0]*v[0]+n[1]*v[1]+n[2]*v[2] > 0:
            draw_line( int(polygons[point][0]),
                       int(polygons[point][1]),
                       int(polygons[point+1][0]),
                       int(polygons[point+1][1]),
                       screen, color)
            draw_line( int(polygons[point][0]),
                      int(polygons[point][1]),
                      int(polygons[point+2][0]),
                      int(polygons[point+2][1]),
                      screen, color)
            draw_line( int(polygons[point+2][0]),
                     int(polygons[point+2][1]),
                     int(polygons[point+1][0]),
                     int(polygons[point+1][1]),
                     screen, color)
        point+= 3


def add_box( polygons, x, y, z, width, height, depth ):
    x1 = x + width
    y1 = y - height
    z1 = z - depth

    #front
    add_polygon(polygons, x, y, z, x, y1, z, x1, y1, z)
    add_polygon(polygons, x1, y1, z, x1, y, z, x, y, z)
    #Top
    add_polygon(polygons, x, y, z1, x, y1, z1, x, y1, z)
    add_polygon(polygons, x, y1, z, x, y, z, x, y, z1)
    #Left
    add_polygon(polygons, x, y, z1, x, y, z, x1, y, z)
    add_polygon(polygons, x1, y, z, x1, y, z1, x, y, z1)
    #Right
    add_polygon(polygons, x1, y, z, x1, y1, z, x1, y1, z1)
    add_polygon(polygons, x1, y1, z1, x1, y, z1, x1, y, z)
    #back
    add_polygon(polygons, x1, y, z1, x1, y1, z1, x, y1, z1)
    add_polygon(polygons, x, y1, z1, x, y, z1, x1, y, z1)
    #bottom
    add_polygon(polygons, x, y1, z, x, y1, z1, x1, y1, z1)
    add_polygon(polygons, x1, y1, z1, x1, y1, z, x, y1, z)


def add_sphere(polygons, cx, cy, cz, r, step ):
    points = generate_sphere(cx, cy, cz, r, step)

    # lat_start = 0
    # lat_stop = step
    # longt_start = 0
    # longt_stop = step

    # step+= 1
    # for lat in range(lat_start, lat_stop):
    #     for longt in range(longt_start, longt_stop+1):
    #         index = lat * step + longt
    #
    #         add_polygon(polygons, points[index][0],
    #                  points[index][1],
    #                  points[index][2],
    #                  points[index][0]+1,
    #                  points[index][1]+1,
    #                  points[index][2]+1 )
    #

    circle = 0
    while circle < len(points):
        next_c = circle + 1
        if circle == len(points) - 1:
            next_c = 0
        i = 0
        while i < len(points[circle]):
            print (len(points[circle]))
            print (i)
            if i >= len(points[circle]) - 1:
                add_polygon(polygons, points[circle][i][0],
                                    points[circle][i][1],
                                    points[circle][i][2],
                                    points[next_c][0][0],
                                    points[next_c][0][1],
                                    points[next_c][0][2],
                                    points[circle][0][0],
                                    points[circle][0][1],
                                    points[circle][0][2])
            else:
                 add_polygon(polygons, points[circle][i][0],
                                    points[circle][i][1],
                                    points[circle][i][2],
                                    points[next_c][i+1][0],
                                    points[next_c][i+1][1],
                                    points[next_c][i+1][2],
                                    points[circle][i+1][0],
                                    points[circle][i+1][1],
                                    points[circle][i+1][2])
                add_polygon(polygons, points[next_c][i][0],
                                    points[next_c][i][1],
                                   points[next_c][i][2],
                                   points[circle][i+1][0],
                                   points[circle][i+1][1],
                                   points[circle][i+1][2],
                                   points[next_c][i+1][0],
                                   points[next_c][i+1][1],
                                   points[nextc][i+1][2])
            i += 1 #try 1 --------------------------------------
        circle+= 1

def generate_sphere( cx, cy, cz, r, step ):
    points = []

    rot_start = 0
    rot_stop = step
    circ_start = 0
    circ_stop = step

    for rotation in range(rot_start, rot_stop):
        rot = rotation/float(step)
        c_points = []
        for circle in range(circ_start, circ_stop+1):
            circ = circle/float(step)

            x = r * math.cos(math.pi * circ) + cx
            y = r * math.sin(math.pi * circ) * math.cos(2*math.pi * rot) + cy
            z = r * math.sin(math.pi * circ) * math.sin(2*math.pi * rot) + cz

            c_points.append([x, y, z])
            #print 'rotation: %d\tcircle%d'%(rotation, circle)
        points.append(c_points)
    return points

def add_torus(polygons, cx, cy, cz, r0, r1, step ):
    points = generate_torus(cx, cy, cz, r0, r1, step)
    #
    # lat_start = 0
    # lat_stop = step
    # longt_start = 0
    # longt_stop = step
    #
    # for lat in range(lat_start, lat_stop):
    #     for longt in range(longt_start, longt_stop):
    #         index = lat * step + longt
    #
    #         add_polygon(polygons, points[index][0],
    #                  points[index][1],
    #                  points[index][2],
    #                  points[index][0]+1,
    #                  points[index][1]+1,
    #                  points[index][2]+1 )

    circle = 0
    while circle < len(points):
        next_c = circle + 1
        if circle == len(points) - 1:
            next_c = 0
        i = 0
        while i < len(points[circle]):
            print (len(points[circle]))
            print (i)
            if i >= len(points[circle]) - 1:
                add_polygon(polygons, points[circle][i][0],
                                    points[circle][i][1],
                                    points[circle][i][2],
                                    points[next_c][0][0],
                                    points[next_c][0][1],
                                    points[next_c][0][2],
                                    points[circle][0][0],
                                    points[circle][0][1],
                                    points[circle][0][2])
            else:
                 add_polygon(polygons, points[circle][i][0],
                                    points[circle][i][1],
                                    points[circle][i][2],
                                    points[next_c][i+1][0],
                                    points[next_c][i+1][1],
                                    points[next_c][i+1][2],
                                    points[circle][i+1][0],
                                    points[circle][i+1][1],
                                    points[circle][i+1][2])
            i += 1 #try 1 --------------------------------------
        circle+= 1

def generate_torus( cx, cy, cz, r0, r1, step ):
    points = []
    rot_start = 0
    rot_stop = step
    circ_start = 0
    circ_stop = step

    for rotation in range(rot_start, rot_stop):
        rot = rotation/float(step)
        c_points = []
        for circle in range(circ_start, circ_stop):
            circ = circle/float(step)

            x = math.cos(2*math.pi * rot) * (r0 * math.cos(2*math.pi * circ) + r1) + cx;
            y = r0 * math.sin(2*math.pi * circ) + cy;
            z = -1*math.sin(2*math.pi * rot) * (r0 * math.cos(2*math.pi * circ) + r1) + cz;

            c_points.append([x, y, z])
        points.append(c_points)
    return points


def add_circle( points, cx, cy, cz, r, step ):
    x0 = r + cx
    y0 = cy
    i = 1

    while i <= step:
        t = float(i)/step
        x1 = r * math.cos(2*math.pi * t) + cx;
        y1 = r * math.sin(2*math.pi * t) + cy;

        add_edge(points, x0, y0, cz, x1, y1, cz)
        x0 = x1
        y0 = y1
        t+= step

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):

    xcoefs = generate_curve_coefs(x0, x1, x2, x3, curve_type)[0]
    ycoefs = generate_curve_coefs(y0, y1, y2, y3, curve_type)[0]

    i = 1
    while i <= step:
        t = float(i)/step
        x = t * (t * (xcoefs[0] * t + xcoefs[1]) + xcoefs[2]) + xcoefs[3]
        y = t * (t * (ycoefs[0] * t + ycoefs[1]) + ycoefs[2]) + ycoefs[3]
        #x = xcoefs[0] * t*t*t + xcoefs[1] * t*t + xcoefs[2] * t + xcoefs[3]
        #y = ycoefs[0] * t*t*t + ycoefs[1] * t*t + ycoefs[2] * t + ycoefs[3]

        add_edge(points, x0, y0, 0, x, y, 0)
        x0 = x
        y0 = y
        t+= step


def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print ('Need at least 2 points to draw')
        return

    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   screen, color)
        point+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )




def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
