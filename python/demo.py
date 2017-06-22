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
            
        
    
    def getTile(self, bbox): 

        (x1, y1, x2, y2) = bbox


        nad_width = x1-x2
        nad_height = y1-y2
        target_size = (2850, 1000)

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


def main():

    x1 = -1345995
    y1 = 412199
    x2 = -1288466
    y2 = 439592

    tiler = TileGrabber()

    img = tiler.getTile((x1,y1,x2,y2))
    tiler.saveImage(img,'tile1.png')

if __name__ == '__main__':
    main()
