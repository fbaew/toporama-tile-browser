from owslib.wms import WebMapService

class TileGrabber:

    def __init__(self):
        self.wms = WebMapService('http://wms.ess-ws.nrcan.gc.ca/wms/toporama_en')
    
    
    def selfTest(self):

        print(self.wms.identification.type)
        print(self.wms.identification.version)
        print(self.wms.identification.title)
        print(list(self.wms.contents))
    
    
        print("Operations:")
        print([op.name for op in self.wms.operations])
    
        print("methods:")
        print(Wms.getOperationByName('GetMap').methods)
    
        print("formatOperations")
        print(Wms.getOperationByName('GetMap').formatOptions)


    def getImageSize(self, nad_size, target_size):

        (nad_x, nad_y) = nad_size
        (target_x, target_y) = target_size

        target_y = target_x / nad_y * nad_x

        return (target_y, target_x)
            
        
    
    def getTile(self, bbox, target_size): 

        (x1, y1, x2, y2) = bbox


        nad_width = x1-x2
        nad_height = y1-y2

        print("Attempting to get tile of size {}".format(target_size))
        image_size = self.getImageSize((nad_width, nad_height), target_size)
        print("Actual image size: {}".format(image_size))

        img = self.wms.getmap(
            layers=['WMS-Toporama'],
            srs='EPSG:3978',
            bbox=(x1, y1, x2, y2),
            size=image_size,
            format='image/png',
            transparent=False
        )
        return img
    
    def saveImage(self, imagedata, filename):

        image = open(filename, 'wb')
        image.write(imagedata.read())
        image.close()

    def subdivide(self, nad_bbox, viewport_size, segments):
        (x_segments, y_segments) = segments
        (x1,y1,x2,y2) = nad_bbox
        nad_width = x1 - x2
        nad_height = y1 - y2
        (view_w, view_h) = viewport_size

        segments = []

        for y_offset in range(y_segments):
            for x_offset in range(x_segments):
                tile_x1 = x1 + x_offset*nad_width/x_segments
                tile_y1 = y1 + y_offset*nad_height/y_segments
                tile_x2 = x2 + x_offset*nad_width/x_segments
                tile_y2 = y2 + y_offset*nad_height/y_segments
                tile_width = view_w/x_segments
                tile_height = view_h/y_segments
                segments.append(
                    ((tile_x1, tile_y1, tile_x2, tile_y2),
                    (tile_width, tile_height))
                )
        return segments


def main():

    x1 = -1345995
    y1 = 412199
    x2 = -1288466
    y2 = 439592

    tiler = TileGrabber()

    target_size = (320, 240)
    segments = (2, 2)

    tiles = tiler.subdivide((x1,y1,x2,y2), target_size, segments)

    tile_count = 0
    for tile in tiles:
        (bbox, tile_size) = tile
        img = tiler.getTile(bbox, tile_size)
        print("Requesting tile {}: ({})".format(tile_count, bbox))
        tiler.saveImage(img,'tile{}.png'.format(tile_count))
        tile_count += 1

if __name__ == '__main__':
    main()
