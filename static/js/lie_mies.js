function Lie_Mies(crossField) {
    const myChart = echarts.init(document.getElementById("col4"))
    myChart.showLoading();
    $.post("/mie", {"cross": crossField}).done(function (graph) {//graph后端处理好的数据
        // console.log(graph.categories)
        console.log(graph)
        myChart.hideLoading();
        graph.nodes.forEach(function (node) {
            node.label = {
                show: true
            };
        });
        const option = {
            title: {
            text: 'Introduction to Cross Fields',
            top: "0%",
        },
            tooltip: {},
            grid: [{
                left: '16%',
                bottom: '15%',
                top: '25%',
                right: '15%'
            }],
            legend: [
                {
                    y:30,
                    // selectedMode: 'single',
                    data: graph.categories.map(function (a) {
                        return a.name;
                    })
                },

            ],
            animationDuration: 1500,
            animationEasingUpdate: 'quinticInOut',
            series: [
                {
                    name: 'Les Miserables',
                    type: 'graph',
                    layout: 'force',
                    data: graph.nodes,
                    links: graph.links,
                    categories: graph.categories,
                    roam: true,
                    label: {
                        position: 'right',
                        formatter: '{b}'
                    },
                    lineStyle: {
                        color: 'source',
                        curveness: 0.3
                    },
                    emphasis: {
                        focus: 'adjacency',
                        lineStyle: {
                            width: 10
                        }
                    },
                    force: {
                        repulsion: 870,
                        // 节点之间的斥力因子，即连接线的长度
                        // edgeLength: 250,
                        // 节点受到的向中心的引力因子。该值越大节点越往中心点靠拢。
                        gravity: 0.02,
                    }
                }
            ]
        };
        myChart.setOption(option);

    })

}