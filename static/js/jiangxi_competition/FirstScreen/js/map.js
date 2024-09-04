(function() {
 var dom = document.getElementById("map");
  var myChart = echarts.init(dom);
  // var app = {};


  var geoCoordMap
  $.getJSON("static/js/jiangxi_competition/FirstScreen/json/map.json",(data)=>{
    $.getJSON("static/js/jiangxi_competition/FirstScreen/json/carbon1.json",(data1)=>{
    draw(data.list,data1['2000']);
  })
      })
  function draw(geoCoordMap,data){
    console.log(geoCoordMap)
    console.log(data)
    var convertData = function(data) {
      var res = [];
      for (var i = 0; i < data.length; i++) {
        var geoCoord = geoCoordMap[data[i].name];
        if (geoCoord) {
          res.push({
            name: data[i].name,
            value: geoCoord.concat(data[i].value)
          });
        }
      }
      // console.log(geoCoord)
      return res;
    };
    var option = {
      title: {
        text: '2000年全国城市碳排放',
        left: 'center'
      },
      tooltip: {
        trigger: 'item'
      },
      bmap: {
        center: [117.1263994, 36.6565542],
        zoom: 5,
        roam: false,
        mapStyle: {
          styleJson: [{
            'featureType': 'water',
            'elementType': 'all',
            'stylers': {
              'color': '#c4d7f5ff'
            }
          }, {
            'featureType': 'land',
            'elementType': 'all',
            'stylers': {
              'color': '#f3f3f3'
            }
          }, {
            'featureType': 'railway',
            'elementType': 'all',
            'stylers': {
              'visibility': 'off'
            }
          }, {
            'featureType': 'highway',
            'elementType': 'all',
            'stylers': {
              'color': '#fdfdfd'
            }
          }, {
            'featureType': 'highway',
            'elementType': 'labels',
            'stylers': {
              'visibility': 'off'
            }
          }, {
            'featureType': 'arterial',
            'elementType': 'geometry',
            'stylers': {
              'color': '#fefefe'
            }
          }, {
            'featureType': 'arterial',
            'elementType': 'geometry.fill',
            'stylers': {
              'color': '#fefefe'
            }
          }, {
            'featureType': 'poi',
            'elementType': 'all',
            'stylers': {
              'visibility': 'off'
            }
          }, {
            'featureType': 'green',
            'elementType': 'all',
            'stylers': {
              'visibility': 'off'
            }
          }, {
            'featureType': 'subway',
            'elementType': 'all',
            'stylers': {
              'visibility': 'off'
            }
          }, {
            'featureType': 'manmade',
            'elementType': 'all',
            'stylers': {
              'color': '#d1d1d1'
            }
          }, {
            'featureType': 'local',
            'elementType': 'all',
            'stylers': {
              'color': '#d1d1d1'
            }
          }, {
            'featureType': 'arterial',
            'elementType': 'labels',
            'stylers': {
              'visibility': 'off'
            }
          }, {
            'featureType': 'boundary',
            'elementType': 'all',
            'stylers': {
              'color': '#fefefe'
            }
          }, {
            'featureType': 'building',
            'elementType': 'all',
            'stylers': {
              'color': '#d1d1d1'
            }
          }, {
            'featureType': 'label',
            'elementType': 'labels.text.fill',
            'stylers': {
              'color': '#999999'
            }
          }]
        }
      },
      series: [{
        name: '碳排放量',
        type: 'scatter',
        coordinateSystem: 'bmap',
        data: convertData(data),
        symbolSize: function(val) {
          return val[2] / 8;
        },
        color:"#5572C6",
        encode: {
          value: 2
        },
        label: {
          formatter: '{b}',
          position: 'right',
          show: false
        },
        emphasis: {
          label: {
            show: true
          }
        }
      }
      ]
    };
    setInterval(() => {
    myChart.setOption({
    bmap:{
      zoom: 7
    }
  });
}, 5000);


    myChart.setOption(option);
  }
myChart.on('mousemove',(params)=>{
  draw_temperature(params.name)
})


})();