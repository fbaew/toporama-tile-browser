from owslib.wms import WebMapService
wms = WebMapService('http://wms.ess-ws.nrcan.gc.ca/wms/toporama_en')
wms.identification.type
wms.identification.version
wms.identification.title
list(wms.contents)
list(wms.contents)
[op.name for op in wms.operations]
wms.getOperationByName('GetMap')
wms.getOperationByName('GetMap').methods
wms.getOperationByName('GetMap').formatOptions
img = wms.getmap( layers=['WMS-Toporama'], srs='EPSG:3978',bbox=(-1345995, 412199, -1288466, 439592), size=(1024,768), format='image/png', transparent=False)

image = open('img1.png', 'wb')
image.write(img.read())
image.close()

