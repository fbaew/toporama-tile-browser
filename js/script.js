var baseURL = 'http://wms.ess-ws.nrcan.gc.ca/wms/toporama_en?'
var service = 'WMS'
var request = 'GetMap'
var format = 'image/png'
var transparent = 'TRUE'
var styles = ''
var version = '1.3.0'
var layers = 'WMS-Toporama'
var width = '2558'
var height = '1218'
var crs = 'EPSG:3978'
var bbox1 = '-1345995.118184133'
var bbox2 = '412199.8130403995'
var bbox3 = '-1288466.648960528'
var bbox4 = '439592.18032513413'


var wct = '-2171423.554201498,442175.47201896046,-2073286.7537612305,494236.3157239812'

function mapURL() {
    var url = baseURL
    url += 'SERVICE=' + service + '&'
    url += 'REQUEST=' + request + '&'
    url += 'FORMAT=' + format + '&'
    url += 'TRANSPARENT=' + transparent + '&'
    url += 'STYLES=' + styles + '&'
    url += 'VERSION=' + version + '&'
    url += 'LAYERS=' + layers + '&'
    url += 'WIDTH=' + width + '&'
    url += 'HEIGHT=' + height + '&'
    url += 'CRS=' + crs + '&'
    url += 'BBOX='
    url += bbox1 + ','
    url += bbox2 + ','
    url += bbox3 + ','
    url += bbox4

    return url
}

function mapURLWithBox(x1, y1, x2, y2, imgwidth, imgheight) {
    var url = baseURL
    url += 'SERVICE=' + service + '&'
    url += 'REQUEST=' + request + '&'
    url += 'FORMAT=' + format + '&'
    url += 'TRANSPARENT=' + transparent + '&'
    url += 'STYLES=' + styles + '&'
    url += 'VERSION=' + version + '&'
    url += 'LAYERS=' + layers + '&'
    url += 'WIDTH=' + width + '&'
    url += 'HEIGHT=' + height + '&'
    url += 'CRS=' + crs + '&'
    url += 'BBOX='
    url += x1 + ','
    url += y1 + ','
    url += x2+ ','
    url += y2 

    return url
}



function setbbox() {
    bbox1 = document.getElementById('bboxval1').value + '.000000000'
}

function update() {
    document.getElementById('mapimage').src = mapURL()
}

function coast() {

    var url = baseURL
    url += 'SERVICE=' + service + '&'
    url += 'REQUEST=' + request + '&'
    url += 'FORMAT=' + format + '&'
    url += 'TRANSPARENT=' + transparent + '&'
    url += 'STYLES=' + styles + '&'
    url += 'VERSION=' + version + '&'
    url += 'LAYERS=' + layers + '&'
    url += 'WIDTH=' + width + '&'
    url += 'HEIGHT=' + height + '&'
    url += 'CRS=' + crs + '&'

    coastURL = url + 'BBOX=' + wct
    document.getElementById('mapimage').src = coastURL
}

function split() {
    var xPartitions = 2
    var yPartitions = 2
    var nadWidth = parseFloat(bbox1)- parseFloat(bbox3)
    var nadHeight = parseFloat(bbox2) - parseFloat(bbox3)

    var box = [parseFloat(bbox1),
                parseFloat(bbox2),
                parseFloat(bbox1) + nadWidth/xPartitions,
                parseFloat(bbox2) + nadHeight/yPartitions]

    document.getElementById('tile').src = mapURLWithBox(
        box[0], box[1], box[2], box[3], nadWidth, nadHeight)
}

/*

http://wms.ess-ws.nrcan.gc.ca/wms/toporama_en?
SERVICE=WMS&
REQUEST=GetMap
FORMAT=image/png
TRANSPARENT=TRUE
STYLES=
VERSION=1.3.0
LAYERS=WMS-Toporama
WIDTH=2558
HEIGHT=1218
CRS=EPSG:3978
BBOX=-1345995.118184133,412199.8130403995,-1288466.648960528,439592.18032513413

http://wms.ess-ws.nrcan.gc.ca/wms/toporama_en?SERVICE=WMS&REQUEST=GetMap&FORMAT=image/png&TRANSPARENT=TRUE&STYLES=&VERSION=1.3.0&LAYERS=WMS-Toporama&WIDTH=2558&HEIGHT=1218&CRS=EPSG:3978&BBOX=-1345995.118184133,412199.8130403995,-1374759.3527959355,1262533.0440408632


http://wms.ess-ws.nrcan.gc.ca/wms/toporama_en?SERVICE=WMS&REQUEST=GetMap&FORMAT=image/png&TRANSPARENT=TRUE&STYLES=&VERSION=1.3.0&LAYERS=WMS-Toporama&WIDTH=2558&HEIGHT=1218&CRS=EPSG:3978&BBOX=-1345995,412199,-1288466,439592

*/

