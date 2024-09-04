function drawNet(time = "2000") {
        $.getJSON("static/js/jiangxi_competition/FirstScreen/json/net.json", (data) => {
           //console.log(data[time])//拿到2000年的数据
           draw_net(data[time], time)
        })
}

function draw_net(data, time) {
    var dom = document.getElementById("net");
var myChart = echarts.init(dom);

option = {
    title: {
        text: time+'年山东省各市县碳排放',
         x: 'center',

    },
color:['#EEE7A1','#E3F2B9','#C0E6AB','#8ECFA5','#f1dfd7','#EEE7A1','#d4e4ff','#F3B274','#A5BAE6','#7E88AC','#ABE1D3','#C0D7D1','#F2FEE6','#F2D1D3','#E09DBF','#E3BACF'],
    series: {
        center: ['50%', '53%'],
        name:'返回',
        type: 'sunburst',
        data: data,
        radius: [0, '100%'],
        sort: null,
         label:{
                fontSize:10
            },
        emphasis: {
            focus: 'ancestor',
        },

        levels: [
            {},
            {
                r0: '20%',
                r: '60%',
                itemStyle: {
                    borderWidth: 2,
                },
                label: {
                    // rotate: 'tangential',
                },
            },
            {
                r0: '60%',
                r: '90%',
                label: {
                    align: 'right',
                },
            },

        ],
    },
      tooltip:{
            trigger:'item',
            triggerOn:'mousemove',
            formatter:'{b}:{c}万吨'
        },
     toolbox:{
            feature:{
                restore:{}
            }
        },
};
// $.getJSON("static/js/jiangxi_competition/FirstScreen/net.json",(data)=>{
//     console.log(data['2000'])
//     myChart.setOption({
//         series:[{
//             name:'net',
//             data:data['2000']
//         }
//         ]
//     })
//
// })
 myChart.setOption(option);
}
drawNet();