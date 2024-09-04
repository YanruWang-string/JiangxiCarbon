function drawGDP(time = "2000") {
        $.getJSON("static/js/jiangxi_competition/FirstScreen/json/gdp.json", (data) => {
           //console.log(data[time])//拿到2000年的数据
           draw_gdp(data[time], time)
        })
}


function draw_gdp(data, time) {
    var dom = document.getElementById("gdp");
    var myChart = echarts.init(dom);
    let heightdata = data.map((d)=>{//遍历出里面的每一个元素
        return d.value;
    })
    let citys = data.map((d)=>{
      return d.name
    })
    let option = {
        title: {
            text: '山东省各市'+time+'GDP',
            x: 'center'
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data: ['Rainfall', 'Evaporation'],
            x: 500,
            show: false
        },

        calculable: true,
        xAxis: [
            {
                type: 'category',
                // prettier-ignore
                data: citys,
                axisLabel: {
                    interval: 0,    //强制文字产生间隔
                    rotate: 45,     //文字逆时针旋转45°
                }
            }

        ],
        grid: [{
            left: 70
        }],
        yAxis: [
            {
                type: 'value',
                axisLabel: {
                    formatter: '{value} 亿元'
                }
            }
        ],
        series: [
            {
                name: 'GDP',
                type: 'bar',
                data: heightdata,
                color: '#C8E0E6',
                markLine: {
                    lineStyle: {
                        color: 'green',

                    },
                    data: [
                        //     {
                        // name: '全国平均GDP',
                        // yAxis: 2000},
                        {
                            name: '江西省平均GDP',
                            type: 'average'
                        }]

                }
            }
        ]
    };
    // $.getJSON("static/js/jiangxi_competition/FirstScreen/gdp.json", (data) => {
    //    // console.log(data)
    // let citys = data['2000'].map((d)=>{
    //   return d.name
    // })
    //     myChart.setOption({
    //     xAxis: [
    //         {
    //             type: 'category',
    //             // prettier-ignore
    //             data: citys,
    //             axisLabel: {
    //                 interval: 0,    //强制文字产生间隔
    //                 rotate: 45,     //文字逆时针旋转45°
    //             }
    //         }
    //
    //     ],
    //         series: [{
    //             name: 'GDP',
    //             data: data['2000']
    //         }]
    //     })
    // })

    myChart.setOption(option);
    myChart.on('click', (params) => {
        // console.log(params)
        draw_temperature(params.name)
    })

}
drawGDP();