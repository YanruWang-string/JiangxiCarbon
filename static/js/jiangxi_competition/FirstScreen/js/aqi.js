(function() {
 var myChart = echarts.init(document.getElementById('aqi'));
    let option = {
         title: {
            text: '山东省各市AQI',
            x: 'center'
        },
            tooltip: {
                position: "top"
            },

              animation: false,
              grid: {
                height: "80%",
                top: "10%"
              },
              xAxis: {
                type: "category",
                axisLabel:{
    		              interval: 1
    	            },
                data: [ 2000 , 2001 , 2002 , 2003 , 2004 , 2005 , 2006 , 2007 , 2008 , 2009 , 2010 , 2011 , 2012 , 2013 , 2014 , 2015 , 2016 , 2017 , 2018 , 2019 ],
                splitArea: {
                  show: true
                }

              },
              yAxis: {
                type: "category",
                data: ['济南', '青岛', '淄博', '枣庄', '东营', '烟台', '潍坊', '济宁', '泰安', '威海', '日照' , '滨州' ,'德州' , '聊城' , '临沂' , '菏泽'  ],
                splitArea: {
                  show: true
                }
              },
              visualMap: {
                // show:false,
                min: 50,
                max: 166,
                calculable: true,
                inRange:{
                    color:['#F2F2DF','#EEECC1','#C8D498','#BDC98B','#A6B376']
                },
                orient:"vertical",
                left: 480,
                bottom: 20,


              },

              series: [{
                name:"AQI",
                type: "heatmap",
                data: [
                ],
                label: {
                    show: true
                },
              },
              ]
        }
        $.getJSON("static/js/jiangxi_competition/FirstScreen/json/aqi.json", (data) => {
         myChart.setOption({
         series:[{
            data:data
        }
        ]
    })
    })

        myChart.setOption(option);
})();