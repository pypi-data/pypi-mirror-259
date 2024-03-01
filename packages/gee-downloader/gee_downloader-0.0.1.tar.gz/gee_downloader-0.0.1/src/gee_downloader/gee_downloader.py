import geedim
import json
import click

def read_polygon(geojson):
    """Reads a polygon identifying an area of interest from a GeoJSON file.

    Parameters
    ----------
    geojson: str
        A path to a valid GeoJSON file with a single polygon identifying an 
        area of interest.
    
    Returns
    -------
    dict
        A dictionary with the polygon.
    """
    with open(geojson, 'r') as fd:
        data = json.load(fd)
    return data["features"][0]["geometry"]

def download_tiff(geojson, start_date, end_date, output_file):
    """Will download a cloud-free composite TIFF from GEE.

    Parameters
    ----------
    geojson: str
        A path to a valid GeoJSON file with a single polygon identifying an
        area of interest
    start_date: str
        Starting date for choosing images for the composite (in the yyyy-mm-dd format)
    end_date: str
        End date for choosing images for the composite (in the yyyy-mm-dd format)
    output_file: str
        Output file name
    """
    polygon = read_polygon(geojson)
    coll = geedim.MaskedCollection.from_name('COPERNICUS/S2')
    coll = coll.search(start_date=start_date, end_date=end_date, region=polygon, cloudless_portion=0.5)
    comp_im = coll.composite(method='mosaic', region=polygon)
    comp_im.download(output_file, region=polygon, crs="EPSG:4326", scale=10, overwrite=True,
                     bands=["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B8A", "B9", "B10", "B11", "B12"])
