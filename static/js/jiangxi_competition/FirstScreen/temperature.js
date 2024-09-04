function update_temperature(city, cityData) {
    var dom = document.getElementById("temperature");
    var myChart = echarts.init(dom);
    let option = {
        title: {
            text: city + '温度和碳排放关系',
            left: 'center'
        },
        grid: {
            bottom: 67
        },

        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'cross',
                animation: false,
                label: {
                    backgroundColor: '#505765'
                }
            }
        },
        legend: {
            data: ['温度', '碳排放量'],
            left: 380,
            top: 10
        },
        dataZoom: [
            {
                show: true,
                realtime: true,
                start: 20,
                end: 80
            },
            {
                type: 'inside',
                realtime: true,
                start: 65,
                end: 85
            }
        ],
        xAxis: [
            {
                type: 'category',
                boundaryGap: false,
                axisLine: {onZero: false},
                // prettier-ignore
                data: [
                    '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'
                ].map(function (str) {
                    return str.replace(' ', '\n');
                })
            }
        ],
        yAxis: [
            {
                name: '温度(°C)',
                type: 'value'
            },
            {
                name: '碳排放量(万吨)',
                nameLocation: 'start',
                alignTicks: true,
                type: 'value',
                inverse: true
            }
        ],
        series: [
            {
                name: '温度',
                type: 'line',
                areaStyle: {},
                color: '#fada95',
                lineStyle: {
                    width: 1
                },
                emphasis: {
                    focus: 'series'
                },
                markArea: {
                    silent: true,
                    itemStyle: {
                        opacity: 0.3
                    },
                    data: [
                        [
                            {
                                xAxis: '2009/9/12\n7:00'
                            },
                            {
                                xAxis: '2009/9/22\n7:00'
                            }
                        ]
                    ]
                },
                // prettier-ignore
                data: cityData.data1
            },
            {
                name: '碳排放量',
                color: '#84C2B7',
                type: 'line',
                yAxisIndex: 1,
                areaStyle: {},
                lineStyle: {
                    width: 1
                },
                emphasis: {
                    focus: 'series'
                },
                markArea: {
                    silent: true,
                    itemStyle: {
                        opacity: 0.3
                    },
                    data: [
                        [
                            {
                                xAxis: '2009/9/10\n7:00'
                            },
                            {
                                xAxis: '2009/9/20\n7:00'
                            }
                        ]
                    ]
                },
                // prettier-ignore
                data: cityData.data2
            }
        ]
    };
    myChart.setOption(option)
}

function draw_temperature(city = '青岛市') {
    $.get("temperature", {
        city: city
    }, (data) => {//这里的data是用来将后台数据传过来
      // console.log(data)
        update_temperature(city, data)
    })
}

draw_temperature()
