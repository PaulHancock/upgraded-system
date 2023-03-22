"""
A script to simulate a population of stars around the Andromeda galaxy
"""

# convert to decimal degrees
import math
import random
import argparse
import numpy as np

NSRC = 1_000_000

def get_radec():
    """
    Determine Andromeda location in ra/dec degrees
    """
    # from wikipedia
    RA = '00:42:44.3'
    DEC = '41:16:09'

    d, m, s = DEC.split(':')
    dec = int(d)+int(m)/60+float(s)/3600

    h, m, s = RA.split(':')
    ra = 15*(int(h)+int(m)/60+float(s)/3600)
    ra = ra/math.cos(dec*math.pi/180)
    
    return (ra, dec)


def make_stars(ra, dec, num_stars):
    """
    make 1000 stars within 1 degree of Andromeda
    """
    ras = np.random.uniform(size=num_stars, low=ra-1, high=ra+1)
    decs = np.random.uniform(size=num_stars, low=dec-1, high=dec+1)
    #ras = []
    #decs = []
    #for i in range(num_stars):
    #    ras.append(ra + random.uniform(-1,1))
    #    decs.append(dec + random.uniform(-1,1))
    return (ras, decs)


def skysim_parser():
    """
    Configure the argparse for skysim

    Returns
    -------
    parser : argparse.ArgumentParser
        The parser for skysim.
    """
    parser = argparse.ArgumentParser(prog='sky_sim', prefix_chars='-')
    parser.add_argument('--ra', dest = 'ra', type=float, default=None,
                        help="Central ra (degrees) for the simulation location")
    parser.add_argument('--dec', dest = 'dec', type=float, default=None,
                        help="Central dec (degrees) for the simulation location")
    parser.add_argument('--out', dest='out', type=str, default='catalog.csv',
                        help='destination for the output catalog')
    return parser


def main():
    parser = skysim_parser()
    options = parser.parse_args()
    # if ra/dec are not supplied the use a default value
    if None in [options.ra, options.dec]:
        ra, dec = get_radec()
    else:
        ra = options.ra
        dec = options.dec
    with open(options.out,'w', encoding='utf-8') as f:
              print("id,ra,dec", file=f)
              ras, decs = make_stars(ra, dec, NSRC)
              ids = np.arange(NSRC).astype(str).astype(object)
              ids = np.char.zfill(ids, 7)
              data = np.column_stack((ids, ras, decs))
              np.savetxt(f, data, fmt="%s, %12f, %12f")
    #ras, decs = make_stars(ra, dec, NSRC)

    # now write these to a csv file for use by my other program
    #with open(options.out,'w', encoding='utf-8') as f:
    #    print("id,ra,dec", file=f)
    #    for i in range(NSRC):
    #        print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f)
    return

    
if __name__ == '__main__':
    main()
