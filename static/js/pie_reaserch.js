

function Pie_reaserch() {
    let crossField = []
    const suo = {
        'cs.AI': 'Artificial Intelligence',
        'cs.AR': 'Hardware Architecture',
        'cs.CC': 'Computational Complexity',
        'cs.CE': 'Computational Engineering, Finance, and Science',
        'cs.CG': 'Computational Geometry',
        'cs.CL': 'Computation and Language',
        'cs.CR': 'Cryptography and Security',
        'cs.CV': 'Computer Vision and Pattern Recognition',
        'cs.CY': 'Computers and Society',
        'cs.DB': 'Databases',
        'cs.DC': 'Distributed, Parallel, and Cluster Computing',
        'cs.DL': 'Digital Libraries',
        'cs.DM': 'Discrete Mathematics',
        'cs.DS': 'Data Structures and Algorithms',
        'cs.ET': 'Emerging Technologies',
        'cs.FL': 'Formal Languages and Automata Theory',
        'cs.GL': 'General Literature',
        'cs.GR': 'Graphics',
        'cs.GT': 'Computer Science and Game Theory',
        'cs.HC': 'Human-Computer Interaction',
        'cs.IR': 'Information Retrieval',
        'cs.IT': 'Information Theory',
        'cs.LG': 'Machine Learning',
        'cs.LO': 'Logic in Computer Science',
        'cs.MA': 'Multiagent Systems',
        'cs.MM': 'Multimedia',
        'cs.MS': 'Mathematical Software',
        'cs.NA': 'Numerical Analysis',
        'cs.NE': 'Neural and Evolutionary Computing',
        'cs.NI': 'Networking and Internet Architecture',
        'cs.OH': 'Other Computer Science',
        'cs.OS': 'Operating Systems',
        'cs.PF': 'Performance',
        'cs.PL': 'Programming Languages',
        'cs.RO': 'Robotics',
        'cs.SC': 'Symbolic Computation',
        'cs.SD': 'Sound',
        'cs.SE': 'Software Engineering',
        'cs.SI': 'Social and Information Networks',
        'cs.SY': 'Systems and Control',
        'econ.EM': 'Econometrics',
        'econ.GN': 'General Economics',
        'econ.TH': 'Theoretical Economics',
        'eess.AS': 'Audio and Speech Processing',
        'eess.IV': 'Image and Video Processing',
        'eess.SP': 'Signal Processing',
        'eess.SY': 'Systems and Control',
        'math.AC': 'Commutative Algebra',
        'math.AG': 'Algebraic Geometry',
        'math.AP': 'Analysis of PDEs',
        'math.AT': 'Algebraic Topology',
        'math.CA': 'Classical Analysis and ODEs',
        'math.CO': 'Combinatorics',
        'math.CT': 'Category Theory',
        'math.CV': 'Complex Variables',
        'math.DG': 'Differential Geometry',
        'math.DS': 'Dynamical Systems',
        'math.FA': 'Functional Analysis',
        'math.GM': 'General Mathematics',
        'math.GN': 'General Topology',
        'math.GR': 'Group Theory',
        'math.GT': 'Geometric Topology',
        'math.HO': 'History and Overview',
        'math.IT': 'Information Theory',
        'math.KT': 'K-Theory and Homology',
        'math.LO': 'Logic',
        'math.MG': 'Metric Geometry',
        'math.MP': 'Mathematical Physics',
        'math.NA': 'Numerical Analysis',
        'math.NT': 'Number Theory',
        'math.OA': 'Operator Algebras',
        'math.OC': 'Optimization and Control',
        'math.PR': 'Probability',
        'math.QA': 'Quantum Algebra',
        'math.RA': 'Rings and Algebras',
        'math.RT': 'Representation Theory',
        'math.SG': 'Symplectic Geometry',
        'math.SP': 'Spectral Theory',
        'math.ST': 'Statistics Theory',
        'astro-ph.CO': 'Cosmology and Nongalactic Astrophysics',
        'astro-ph.EP': 'Earth and Planetary Astrophysics',
        'astro-ph.GA': 'Astrophysics of Galaxies',
        'astro-ph.HE': 'High Energy Astrophysical Phenomena',
        'astro-ph.IM': 'Instrumentation and Methods for Astrophysics',
        'astro-ph.SR': 'Solar and Stellar Astrophysics',
        'cond-mat.dis-nn': 'Disordered Systems and Neural Networks',
        'cond-mat.mes-hall': 'Mesoscale and Nanoscale Physics',
        'cond-mat.mtrl-sci': 'Materials Science',
        'cond-mat.other': 'Other Condensed Matter',
        'cond-mat.quant-gas': 'Quantum Gases',
        'cond-mat.soft': 'Soft Condensed Matter',
        'cond-mat.stat-mech': 'Statistical Mechanics',
        'cond-mat.str-el': 'Strongly Correlated Electrons',
        'cond-mat.supr-con': 'Superconductivity',
        'gr-qc': 'General Relativity and Quantum Cosmology',
        'hep-ex': 'High Energy Physics - Experiment',
        'hep-lat': 'High Energy Physics - Lattice',
        'hep-ph': 'High Energy Physics - Phenomenology',
        'hep-th': 'High Energy Physics - Theory',
        'math-ph': 'Mathematical Physics',
        'nlin.AO': 'Adaptation and Self-Organizing Systems',
        'nlin.CD': 'Chaotic Dynamics',
        'nlin.CG': 'Cellular Automata and Lattice Gases',
        'nlin.PS': 'Pattern Formation and Solitons',
        'nlin.SI': 'Exactly Solvable and Integrable Systems',
        'nucl-ex': 'Nuclear Experiment',
        'nucl-th': 'Nuclear Theory',
        'physics.acc-ph': 'Accelerator Physics',
        'physics.ao-ph': 'Atmospheric and Oceanic Physics',
        'physics.app-ph': 'Applied Physics',
        'physics.atm-clus': 'Atomic and Molecular Clusters',
        'physics.atom-ph': 'Atomic Physics',
        'physics.bio-ph': 'Biological Physics',
        'physics.chem-ph': 'Chemical Physics',
        'physics.class-ph': 'Classical Physics',
        'physics.comp-ph': 'Computational Physics',
        'physics.data-an': 'Data Analysis, Statistics and Probability',
        'physics.ed-ph': 'Physics Education',
        'physics.flu-dyn': 'Fluid Dynamics',
        'physics.gen-ph': 'General Physics',
        'physics.geo-ph': 'Geophysics',
        'physics.hist-ph': 'History and Philosophy of Physics',
        'physics.ins-det': 'Instrumentation and Detectors',
        'physics.med-ph': 'Medical Physics',
        'physics.optics': 'Optics',
        'physics.plasm-ph': 'Plasma Physics',
        'physics.pop-ph': 'Popular Physics',
        'physics.soc-ph': 'Physics and Society',
        'physics.space-ph': 'Space Physics',
        'quant-ph': 'Quantum Physics',
        'q-bio.BM': 'Biomolecules',
        'q-bio.CB': 'Cell Behavior',
        'q-bio.GN': 'Genomics',
        'q-bio.MN': 'Molecular Networks',
        'q-bio.NC': 'Neurons and Cognition',
        'q-bio.OT': 'Other Quantitative Biology',
        'q-bio.PE': 'Populations and Evolution',
        'q-bio.QM': 'Quantitative Methods',
        'q-bio.SC': 'Subcellular Processes',
        'q-bio.TO': 'Tissues and Organs',
        'q-fin.CP': 'Computational Finance',
        'q-fin.EC': 'Economics',
        'q-fin.GN': 'General Finance',
        'q-fin.MF': 'Mathematical Finance',
        'q-fin.PM': 'Portfolio Management',
        'q-fin.PR': 'Pricing of Securities',
        'q-fin.RM': 'Risk Management',
        'q-fin.ST': 'Statistical Finance',
        'q-fin.TR': 'Trading and Market Microstructure',
        'stat.AP': 'Applications',
        'stat.CO': 'Computation',
        'stat.ME': 'Methodology',
        'stat.ML': 'Machine Learning',
        'stat.OT': 'Other Statistics',
        'stat.TH': 'Statistics Theory',
        'CS': 'Computer Science',
        // 'q-fh':,
        "STAT": "Statistics",
        // "Q_FH":"",
        "PH": "Physics",
        "EESS": "Electrical Engineering and Systems Science",
        "Q-BIO": "Quantitative Biology",
        "MATH": "Mathematics",
        "Q-FIN": "Quantitative Finance",
        "ECON": "Econometrics"

    }
    const option = {
        tooltip: {
            formatter: function (v) {
                //console.log(v)
                // return suo[v.]
                let forma = "";
                // console.log(suo[v['data']['name']])
                if (suo[v['data']['name']] === undefined) {
                    return v["data"]['name'] + ": " + v['value']
                } else
                    return suo[v["data"]['name']] + ": " + v['value']
                // console.log(v)
            }
        },

        title: {
            text: 'Introduction to Hot Areas',
            top: "0%",
        },

        series: {
            type: 'sunburst',
            data: [],
            radius: [0, '95%'],
            sort: function (nodeA, nodeB) {//做排序
                return -nodeA.getValue() + nodeB.getValue()
            },
            emphasis: {
                focus: 'ancestor'
            },
            // sort:
            levels: [
                {},
                {
                    r0: '10%',
                    r: '50%',
                    label: {
                        align: 'right'
                    }
                },
                {
                    r0: '50%',
                    r: '60%',
                    label: {
                        position: 'outside',
                        padding: 3,
                        silent: false,
                    },
                    itemStyle: {
                        borderWidth: 2


                    }
                }
            ]
        }
    };
    const chart = echarts.init(document.getElementById("col2"))
    $.getJSON("static/json/data_paper.json", (data) => {
        option['series']['data'] = data
        // console.log(option)
        chart.setOption(option)
    })
    chart.on('click', function (params) {
        if (params.treePathInfo.length === 3 && $.inArray(params.name,crossField)<0) {
            crossField.push(params.name)
            Lie_Mies(crossField)
        }
        else if($.inArray(params.name,crossField)>=0){
            crossField.remove(params.name)
            console.log(crossField)
            Lie_Mies(crossField)
        }

    });
    chart.on('dblclick', function (params) {
        wordCloud(params.name)
    });
    chart.getZr().on('click', function (event) {
        // 没有 target 意味着鼠标/指针不在任何一个图形元素上，它是从“空白处”触发的。
        if (!event.target) {
            crossField = []
            Lie_Mies(crossField)
            // console.log(crossField)
        }
    });

}


Array.prototype.remove = function(val) {
    var index = this.indexOf(val);
    if (index > -1) {
        this.splice(index, 1);
    }
};