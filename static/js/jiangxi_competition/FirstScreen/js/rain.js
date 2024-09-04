(function() {
var dom = document.getElementById("rain");
var myChart = echarts.init(dom);
let option = {
  title: {
            text: '山东省各市历年降雨',
            x: 'center'
        },
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'line',
      lineStyle: {
        color: 'rgba(0,0,0,0.2)',
        width: 1,
        type: 'solid'
      }
    }
  },
  legend: {
    data: ['济南市', '青岛市', '淄博市', '枣庄市', '东营市', '烟台市', '潍坊市', '济宁市', '泰安市', '威海市', '日照市','临沂市','德州市','聊城市','滨州市','菏泽市'],
    top:30
  },
  singleAxis: {
    top: 70,
    bottom: 20,
    axisTick: {},
    axisLabel: {},
    type: 'time',
    axisPointer: {
      animation: true,
      label: {
        show: true
      }
    },
    splitLine: {
      show: true,
      lineStyle: {
        type: 'dashed',
        opacity: 0.2
      }
    }
  },
  color:['#EEE7A1','#E3F2B9','#C0E6AB','#8ECFA5','#f1dfd7','#EEE7A1','#d4e4ff','#A1AB74','#F3B274','#A1AB74','#A5BAE6'],
  series: [
    {
      type: 'themeRiver',
      emphasis: {
        itemStyle: {
          shadowBlur: 20,
          shadowColor: 'rgba(0, 0, 0, 0.8)'
        }
      },
      colorBy:{

      },
      data: [

      ]
    }
  ]
};
$.getJSON("static/js/jiangxi_competition/FirstScreen/json/rain.json",(data)=>{
   //console.log(data)
  // console.log(option)
  option.series[0].data = data
        myChart.setOption(option)
    })


})();