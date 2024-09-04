function scatter() {
    var myChart = echarts.init(document.getElementById("col1"));

    const data = [];

    // 指定图表的配置项和数据
    const option = {
        dataset: [
            {
                source: [
                    ["Tatti Nikolaj ", 32, 29],
                    ["Gren Lucas ", 28, 22],
                    ["Liu Yang ", 71, 20],
                    ["Zhao Jun ", 37, 18],
                    ["Li Yang ", 31, 18],
                    ["Yang Fan ", 31, 15],
                    ["Wang Hao ", 39, 14],
                    ["Gan Wensheng ", 13, 13],
                    ["Amarilli Antoine ", 14, 13],
                    ["Chatterjee Krishnendu ", 19, 13],
                    ["Li Hui ", 18, 12],
                    ["Tang Hao ", 21, 12],
                    ["Farooq Muhammad Junaid ", 15, 12],
                    ["André Étienne ", 14, 12],
                    ["Tsur Dekel ", 11, 11],
                    ["Chen Xi ", 31, 11],
                    ["Choi Jinho ", 12, 11],
                    ["Zhang Zhao ", 20, 10],
                    ["Zhang Rui ", 57, 10],
                    ["Diakonikolas Ilias ", 13, 10],
                    ["Sliwa Benjamin ", 11, 10],
                    ["Abramo Giovanni ", 11, 10],
                    ["Al-Fedaghi Sabah ", 9, 9],
                    ["Chen Yu ", 26, 9],
                    ["Xu Peng ", 22, 9],
                    ["Wang Dong ", 29, 9],
                    ["Li Jia ", 21, 9],
                    ["Haberland René ", 9, 9],
                    ["Li Xiang ", 33, 9],
                    ["Wang Qi ", 28, 9],
                    ["Aziz Haris ", 10, 9],
                    ["Zhang Chi ", 22, 9],
                    ["Zhang Wei ", 48, 9],
                    ["Li Chao ", 35, 9],
                    ["Zhang Jiawei ", 18, 9],
                    ["Biedl Therese ", 10, 9],
                    ["Hosseini Babak ", 9, 9],
                    ["Cao Yuan ", 18, 9],
                    ["Liu Bin ", 17, 9],
                    ["Charlier Jeremy ", 9, 9],
                    ["Gabora Liane ", 14, 8],
                    ["Li Yu ", 17, 8],
                    ["Doerr Benjamin ", 10, 8],
                    ["Yang Carl ", 10, 8],
                    ["Wang Tao ", 16, 8],
                    ["Ogura Masaki ", 8, 8],
                    ["Kong Qiuqiang ", 12, 8],
                    ["Wang Yue ", 27, 8],
                    ["Lee Chang-Shing ", 8, 8],
                    ["Liu Yong ", 26, 8],
                ],
            },
            {
                source: [
                    ["Tao Dacheng ", 87, 0],
                    ["Liu Yang ", 71, 20],
                    ["Wang Wei ", 62, 7],
                    ["Levine Sergey ", 59, 0],
                    ["Liu Wei ", 57, 5],
                    ["Zhang Rui ", 57, 10],
                    ["Yu Philip S. ", 52, 0],
                    ["Nakov Preslav ", 49, 7],
                    ["Zhang Wei ", 48, 9],
                    ["Alouini Mohamed-Slim ", 47, 0],
                    ["Zhang Lei ", 46, 5],
                    ["Wang Jun ", 45, 3],
                    ["Bengio Yoshua ", 44, 2],
                    ["Li Bo ", 42, 4],
                    ["Wang Xin ", 40, 4],
                    ["Navab Nassir ", 40, 0],
                    ["Chen Wei ", 40, 5],
                    ["Neubig Graham ", 40, 1],
                    ["Wang Hao ", 39, 14],
                    ["Liu Ming ", 39, 1],
                    ["Van Gool Luc ", 38, 0],
                    ["Luo Jiebo ", 38, 0],
                    ["Wang Rui ", 37, 7],
                    ["Zhao Jun ", 37, 18],
                    ["Tian Qi ", 36, 0],
                    ["Wang Yang ", 36, 4],
                    ["Saad Walid ", 36, 1],
                    ["Gao Jianfeng ", 36, 2],
                    ["Bennis Mehdi ", 36, 0],
                    ["Li Chao ", 35, 9],
                ],
            },
        ],
        grid: [{
            left: '16%',
            bottom: '15%',
            top: '25%',
            right: '15%'
        }],

        xAxis: {
            name: "All",
        },
        yAxis: {
            name: "Fisrt Author Only",
        },
        dataZoom: [
            // ...
        ],
        title: {
            text: "The Highest Production Authors",
            // left: "0%",
            top: "0%",
        },
        legend: {
            right: "10%",
            top: "3%",
            data: ["First", "All"],
        },
        series: [
            {
                name: "First",
                datasetIndex: 0,
                type: "scatter",
                encode: {x: 1, y: 2},
                symbolSize: 15,
                emphasis: {
                    focus: "series",
                    label: {
                        show: true,
                        formatter: function (param) {
                            return (
                                param.data[0] +
                                "(" +
                                param.data[1] +
                                "," +
                                param.data[2] +
                                ")"
                            );
                        },
                        position: "top",
                    },
                },
            },
            {
                name: "All",
                datasetIndex: 1,
                type: "scatter",
                encode: {x: 1, y: 2},
                symbolSize: 15,
                emphasis: {
                    focus: "series",
                    label: {
                        show: true,
                        formatter: function (param) {
                            return (
                                param.data[0] +
                                "(" +
                                param.data[1] +
                                "," +
                                param.data[2] +
                                ")"
                            );
                        },
                        position: "top",
                    },
                },
            },
        ],
    };

    myChart.setOption(option);
    window.addEventListener('resize', () => {
        myChart.resize();
    }, false);

}

scatter()